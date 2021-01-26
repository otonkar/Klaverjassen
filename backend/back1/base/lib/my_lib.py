# base/lib/my_lib.py

#######################################################################################
##
## This is a module to support functions in the klaverjas game.
## It contains the following functions/classes
##
##  - get_client_ip              ; to get the IP address from the original user 
##
#######################################################################################


def get_client_ip(request):
	'''
	Based on a request that is forwarded by Nginx, get the IP address of the original sender

	https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
	'''

	try: 
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[-1].strip()
		else:
			ip = request.META.get('REMOTE_ADDR')
		return ip
	except:
		ip = request.META.get('REMOTE_ADDR')
		return ip