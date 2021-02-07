#coinflip/views.py

from rest_framework import filters, generics, status        # to use the generic views
from rest_framework.response import Response
from rest_framework.views import APIView

from coinflip import serializers
from coinflip.coinflip_lib import pascal_triangle, calc_chance
from coinflip.models import CoinFlipResults
from my_auth.models import User

from base.logging.my_logging import logger
from base.lib.my_lib import get_client_ip

from django.conf import settings



class CoinFlipResultsView(APIView):
	'''
	View for retreiving, creating and updating coinflip experiments.

	Log the result of an coin flip experiment. Each experiment for a user is a separate row in the DB.
	This row is overwritten when a next coinflip is done. 
	The field 'in_play' can be set to indicate that this experiment has stoppen. 
	A new experiment can be started.

	Support the following actions
	 * Log  : log the flipcoin result and send back the calculated chance
	          When there is no open experiment a new experiment is opened.
			  {"action": "Log", "nToss": 7, "nHeads": 6}

	 * Stop : Close the open experiment for the user.
	          In this request only the 'in_play' field is set to False.
			  {"action": "Stop"}

	 * List : Get the list of experiments for a user.
	 		  {"action": "List"}

	 * Get	: Get the data of the current open experiment.
	 		  When it doen not exist, create a new experiment with reset data.
			  {"action": "Get"}

	Note that only logged in users can do these request, because the username is extracted
	from the request.
	
	'''

	def post(self, request):
		"""
		Support the posts for actionTypes: ['Log', 'Stop', 'List', 'Get']

		"""
		# print(settings.DEBUG)

		try:

			## User must be in the request
			user        = request.user
			user_obj	= User.objects.get(username = user)

			## Set key names of the input data
			key1 = 'action'
			key2 = 'nToss'
			key3 = 'nHeads'
			key4 = 'in_play'

			## Initial values
			action = ''
			actionTypes = ['Log', 'Stop', 'List', 'Get']

			## Determine the type of action
			## and validate that a pre-defined actiontype is used.
			if key1 in request.data:
				action = request.data[key1]
				if not (action in actionTypes):
					content = {'success': False, 'message': 'No valid action type is used in request'}
					return Response(content, status=status.HTTP_400_BAD_REQUEST)

			else: 
				content = {'success': False, 'message': 'Action is not defined in request'}
				return Response(content, status=status.HTTP_400_BAD_REQUEST)


			##############################################################################
			### Log action
			### Log to an open experiment or else create a new experiment
			### INPUT:  {"action": "Log", "nToss": 1580, "nHeads": 790}

			if action == actionTypes[0]:

				## Check that input contains the fields needed
				if key2 in request.data:
					nToss = request.data[key2]
				else: 
					content = {'success': False, 'message': 'nToss must be present in input data'}
					return Response(content, status=status.HTTP_400_BAD_REQUEST)

				if key3 in request.data:
					nHeads = request.data[key3]
				else: 
					content = {'success': False, 'message': 'nHeads must be present in input data'}
					return Response(content, status=status.HTTP_400_BAD_REQUEST)

				if type(nToss) != int or type(nHeads) != int:
					content = {'success': False, 'message': 'nHeads and nToss must be integers'}
					return Response(content, status=status.HTTP_400_BAD_REQUEST)


				## Calculate the chance
				chance = calc_chance(nToss, nHeads)

				## Get the open experiment for this user
				qs = CoinFlipResults.objects.filter(user__username = user, in_play = True)

				data = { 
					'user': user_obj.id,
					'nToss': nToss,
					'nHeads': nHeads,
					'in_play': True,
					'chance' : chance
				}

				if len(qs) == 0:
					# Need to create a new experiment

					serializer = serializers.CoinFlipResultsSerializerUpdate(data = data)
					if serializer.is_valid():
						serializer.save()

						content = {
							'success': True, 
							'message': 'OK, calculated the chance and created a new experiment',
							'data': serializer.data,
							'errors': {} }

						return Response(content, status=status.HTTP_201_CREATED )

					else:
						content = {
							'success': False, 
							'message': 'serializer validation error',
							'data': {}, 
							'errors': serializer.errors }

						return Response(content, status=status.HTTP_400_BAD_REQUEST )

				else: 
					# Need to update the existing experiment

					# Validate that nToss is allowed to be increased by only 1
					if (qs[0].nToss + 1 != nToss ):
						content = {
							'success': False, 
							'message': f'nToss {qs[0].nToss} only allowed to be increased by 1',
							'data': {},
							'errors': {} }

						return Response(content, status=status.HTTP_400_BAD_REQUEST )

					# Validate that nHeads is allowed to be increased only by 0 or 1:
					if not ( (qs[0].nHeads == nHeads ) or (qs[0].nHeads + 1 == nHeads )  ):
						content = {
							'success': False, 
							'message': f'nHeads {qs[0].nHeads} only allowed to be increased by 0 or 1',
							'data': {},
							'errors': {} }

						return Response(content, status=status.HTTP_400_BAD_REQUEST )



					serializer = serializers.CoinFlipResultsSerializerUpdate(qs[0], data = data)
					if serializer.is_valid():
						serializer.save()
						# obj.save()

						content = {'success': True, 
									'message': 'OK, calculated the chance and updated the experiment',
									'data': serializer.data,
									'errors': {} }
				
						return Response(content, status=status.HTTP_200_OK)

					else:
						content = {
							'success': False, 
							'message': 'serializer validation error',
							'data': {},
							'errors': serializer.errors }

						return Response(content, status=status.HTTP_400_BAD_REQUEST )


			##############################################################################
			### Stop action
			### Set an open experiment to in_play = False
			### INPUT:  {"action": "Stop"}

			if action == actionTypes[1]:
				
				## Check that there exist an open experiment for this user
				qs = CoinFlipResults.objects.filter(user__username = user, in_play = True)

				if len(qs) == 0:
					content = {
							'success': False, 
							'message': 'No open experiments to close',
							'data': {},
							'errors': {} }

					return Response(content, status=status.HTTP_400_BAD_REQUEST )

				else:
					data = { 
						'user'		: user_obj.id,
						'nToss'		: qs[0].nToss,
						'nHeads'	: qs[0].nHeads,
						'in_play'	: False,
						'chance' 	: qs[0].chance
					}

					serializer = serializers.CoinFlipResultsSerializerUpdate(qs[0], data = data)
					if serializer.is_valid():
						serializer.save()

						content = {'success': True, 
									'message': 'OK, stopped the experiment',
									'data': serializer.data,
									'errors': serializer.errors }
				
						return Response(content, status=status.HTTP_200_OK)

					else:
						content = {
							'success': False, 
							'message': 'serializer validation error',
							'data': {},
							'errors': serializer.errors }

						return Response(content, status=status.HTTP_400_BAD_REQUEST )


			##############################################################################
			### List action
			### Get all closed experiments for the user
			### INPUT:  {"action": "List"}

			if action == actionTypes[2]:
				
				## get all experiments that are closed
				qs = CoinFlipResults.objects.filter(in_play = False).order_by('chance')[:50]
				# qs = CoinFlipResults.objects.filter(user__username = user, in_play = False)

				serializer = serializers.CoinFlipResultsSerializer(qs, many=True)
				content = {'success': True, 
							'message': 'OK, list of stopped experiments',
							'data': serializer.data,
							'errors': {} }
		
				return Response(content, status=status.HTTP_200_OK)

			
			##############################################################################
			### Get action
			### Get data for an open experiment or else create a new experiment
			### INPUT:  {"action": "Get"}

			if action == actionTypes[3]:

				## Get the open experiment for this user
				qs = CoinFlipResults.objects.filter(user__username = user, in_play = True)

				data = { 
					'user': user_obj.id,
					'nToss': 0,
					'nHeads': 0,
					'in_play': True,
					'chance' : 0.00
				}

				if len(qs) == 0:

					# Need to create a new experiment
					serializer = serializers.CoinFlipResultsSerializerUpdate(data = data)
					if serializer.is_valid():
						serializer.save()

						content = {
							'success': True, 
							'message': 'Created a new experiment',
							'data': serializer.data,
							'errors': {} }

						return Response(content, status=status.HTTP_201_CREATED )

					else:
						serializer = serializers.CoinFlipResultsSerializerUpdate(qs[0], many=False)
						content = {
							'success': False, 
							'message': 'serializer validation error',
							'data': {}, 
							'errors': serializer.errors }

						return Response(content, status=status.HTTP_400_BAD_REQUEST )

				else: 
					# Need to get the data of the existing experiment
					serializer = serializers.CoinFlipResultsSerializerUpdate(qs[0], many=False)
					content = {'success': True, 
								'message': 'Get the data of an open experiment',
								'data': serializer.data,
								'errors': {} }
			
					return Response(content, status=status.HTTP_200_OK)

		except:
			content = {'success': False, 'message': 'Exception occured'}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)

