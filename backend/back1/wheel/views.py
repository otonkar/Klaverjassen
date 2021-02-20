#coinflip/views.py

from django.http import Http404

import json

from rest_framework import filters, generics, status        # to use the generic views
from rest_framework.response import Response
from rest_framework.views import APIView

from wheel import serializers
from wheel.models import WheelSettings
from my_auth.models import User

from base.logging.my_logging import logger
from base.lib.my_lib import get_client_ip

from django.conf import settings


class WheelSettingsListCreateView(APIView):
	'''
	List and Create Settings for a user
	'''

	def get(self, request, format=None):
		'''
		Get the list of Settings
		'''

		try: 

			# filter based in the user doing the request
			user_obj 	= request.user

			model       = WheelSettings.objects.filter(user = user_obj)
			serializer  = serializers.WheelSettingsSerializer(model, many=True)

			content = {'success': True, 
						'message': 'OK',
						'data': serializer.data,
						'errors': {} 
						}
			
			return Response(content, status=status.HTTP_200_OK)

		except:

			content = {'success': False, 
						'message': 'Exception occured',
						'data': {},
						'errors': ['Error handling the get request']
						}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)


	def post(self, request, format=None):
		'''
		Create new Settings

		{"name": "Testname", "userSettings": "test", "userInput": "test1" }

		'''

		try:

			request.data['user'] = request.user.id

			# store in json format
			request.data['userSettings']= json.dumps( request.data['userSettings'])
			request.data['userInput']= json.dumps( request.data['userInput'])

			serializer  = serializers.WheelSettingsSerializer(data = request.data)
			if serializer.is_valid():
				serializer.save()
				content = {'success': True, 
						'message': 'OK, created wheelSettings',
						'data': serializer.data,
						'errors': {} 
						}
			
				return Response(content, status=status.HTTP_201_CREATED)

			else:
				content = {
					'success': False, 
					'message': 'serializer validation error',
					'data': {}, 
					'errors': serializer.errors 
					}

				return Response(content, status=status.HTTP_400_BAD_REQUEST )

			
		except:
			content = {'success': False, 
						'message': 'Exception occured',
						'data': {},
						'errors': ['Error handling the post request']
						}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)


class WheelSettingsRetreiveUpdateDeleteView(APIView):
	'''
	Retreive and Update Settings for a user
	'''

	def get_object(self, ID):
		'''
		Get the object based on the ID
		'''
		try:
			model 		= WheelSettings.objects.get(ID = ID)
			serializer  = serializers.WheelSettingsSerializer(model)

			return model

		except:
			raise Http404
			

	def get(self, request, ID, format=None):
		'''
		Retreive a wheeSettings object
		'''
		try:

			model 		= self.get_object(ID)
			serializer  = serializers.WheelSettingsSerializer(model)

			content = {'success': True, 
						'message': 'OK, retreived a wheelSettings object ',
						'data': serializer.data,
						'errors': {} 
						}
			
			return Response(content, status=status.HTTP_200_OK)

		except: 
			content = {'success': False, 
						'message': f'wheelSettings object with ID = {ID} does not exist',
						'data': {},
						'errors': ['Error handling the get objects function']
						}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, ID, format=None):
		'''
		Update a wheeSettings object
		{"name": "ole",  "userSettings": "test updated","userInput": "test1 updated", "user": "3"}
		'''
		try:

			request.data['user'] = request.user.id

			model 		= self.get_object(ID)
			print('XX1')

			# store in json format
			request.data['userSettings']= json.dumps( request.data['userSettings'])
			request.data['userInput']= json.dumps( request.data['userInput'])

			print('XX2', request.data)

			serializer  = serializers.WheelSettingsSerializer(model, data=request.data)

			if serializer.is_valid():
				serializer.save()
				content = {'success': True, 
						'message': 'OK, updated wheelSettings',
						'data': serializer.data,
						'errors': {} 
						}
			
				return Response(content, status=status.HTTP_201_CREATED)

			else:
				content = {
					'success': False, 
					'message': 'serializer validation error',
					'data': {}, 
					'errors': serializer.errors 
					}

				return Response(content, status=status.HTTP_400_BAD_REQUEST )

		except: 
			content = {'success': False, 
						'message': 'Exception error',
						'data': {},
						'errors': ['Error handling the get objects function']
						}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, ID, format=None):
		'''
		Delete a wheeSettings object
		'''
		try:


			model 		= self.get_object(ID).delete()
			
			content = {'success': True, 
					'message': 'OK, deleted a wheelSettings instance',
					'data': {},
					'errors': {} 
					}
		
			return Response(content, status=status.HTTP_201_CREATED)


		except: 
			content = {'success': False, 
						'message': 'Exception error',
						'data': {},
						'errors': ['Error handling the delete objects function']
						}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)






	






