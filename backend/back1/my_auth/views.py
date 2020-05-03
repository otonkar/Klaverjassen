# my_auth/views.py

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from my_auth.models import User, BlackListedToken
from my_auth.authentication import JWTAuthenticationBlacklist

from my_auth import serializers
from my_auth.models import User


class UserSignUp(generics.CreateAPIView):    # Post API View to create new users
    queryset = User.objects.all()
    serializer_class = serializers.UserSignUpSerializer
    permission_classes = ( )                # Everybody is allowed to sign up

    # def perform_create(self, serializer):
        # print('***',self.request.__dict__)
        # user = User(username = self.request.data.username)
        # user.set_password(self.request.data.password)
        # user.first_name = self.request.data.first_name
        # user.last_name = self.request.data.last_name
        # user.email = self.request.data.email
        # user.save()
        

class Logout(APIView):
    """
    Logout a user by placing the user +  token on a blacklist.
    This request uses the default authentication, so that only
    authenticated (logged in) users can use the Logout request.
    """

    def post(self, request):
        """
        Based on token in the header get the user_id
        Put the user_id and token on the Blacklist, so that 
        this token is not allowed anymore.
        """

        try: 
            user_id = JWTAuthenticationBlacklist().authenticate(request)[0]
            access_token = JWTAuthenticationBlacklist().authenticate(request)[1]

            # Add user + token to the Blacklist
            user_obj = User.objects.get(username=user_id)
            item = BlackListedToken(
                        token   = access_token,
                        user    = user_obj
                   )
            item.save()

            # see: https://www.django-rest-framework.org/api-guide/status-codes/
            content = {'logout': 'success'}
            return Response(content, status=status.HTTP_200_OK)
        
        except:
            content = {'logout': 'not succeeded'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

# class CheckUserExists(APIView):
#     """
#     View to check that a username already exists in the database
#     The requester doen not need to be authenticated to do this reqeuest.
#     This will be used at registration.
#     """
#     def post(self, request):
#         return Response({'test': 'ok'})

class Test(APIView):
    """
    View to test a post request
    The requester must be authenticated for a correct response.
    """
    def post(self, request):
        return Response({'test': 'ok'})