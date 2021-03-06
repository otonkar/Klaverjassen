# my_auth/views.py

import random
from django.utils import timezone

from django.core import exceptions

from django.core.mail import send_mail                          # EmailMultiAlternatives, 
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib.auth.password_validation import validate_password

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt import views as jwt_views

from my_auth.models import User, BlackListedToken
from my_auth.authentication import JWTAuthenticationBlacklist

from my_auth import serializers
from my_auth.models import User

from base.logging.my_logging import logger


def createResetCode(N):
    '''
    Function to create a random reset code with length N to reset the passwords
    '''

    # Create a list of characters that can be used in the code
    # avoid characters that can be confusing like, i,I,l,1,o,O,0,Q
    char_list = ['a','b','c','d','e','f','h','j','k','m','n','p','q','r','s','t', \
        'u','v','w','x','y','z','A','B','C','D','E','F','G','H','J','K','M','N','P','R', \
        'S','T','U','V','W','X','Y','Z','2','3','4','5','6','7','8','9']
    ll = len(char_list)

    code = ''
    for i in range(0, N):
        index = random.randint(0, ll-1)
        char = char_list[index]
        code = code + char

    return code


class OleTokenObtainPairView(jwt_views.TokenObtainPairView):
    '''
    Change the standaard TokeObtainPairView so that it is logged
    when a user logs in
    '''
    serializer_class = serializers.OleTokenObtainPairSerializer



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

            #Log the logout
            logger('authentication').info(f'[{user_id}] has logged out')

            # see: https://www.django-rest-framework.org/api-guide/status-codes/
            content = {'logout': 'success'}
            return Response(content, status=status.HTTP_200_OK)
        
        except:
            logger('errors').error(f'User {user_id} failed to logout')
            content = {'logout': 'not succeeded'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class ResetCode(APIView):
    """
    A non-authenticated user can request a code in case of
    forgotten password. 
    This view will receive a username and/or mailaddress.
    Based on this input a user is looked up in the database and a code is generated
    and sent to the mail address.

        INPUT: {"username": "ole", "email": "ole.karlsen@gmail.com"}
        when no email or username is used then this must be an empty string

        OUTPUT: {"reset_code": "xxxxxx"}
    """
    permission_classes = ( )                # Everybody is allowed use the forgotten password function

    def post(self, request):
        """
        Receive username and/or email address.
        When all validated, return a reset code
        """

        # Set the length to the reset code
        code_length = 8

        try:
            username    = request.data['username']
            email       = request.data['email']
            ip_address  = request.META.get("REMOTE_ADDR")

            if username != '':
                # When username is given, only use username to check the existence of this user
                qs = User.objects.filter(username=username)

                if len(qs) != 1:
                    # When there is not a single result, then create then error
                    content = {'message': 'Deze gebruikersnaam is niet in gebruik'}
                    logger('authentication').warning(f'Non existent user [{username}] requested password reset from IP [{ip_address}]')
                    return Response(content, status=status.HTTP_404_NOT_FOUND)

            else:
                # When no username is given check the email

                if email != '':
                    qs = User.objects.filter(email=email).order_by('username')

                    if len(qs) == 1:
                        # When there is a single account with this email address this can be used
                        # Do nothing, and create the code and email at the end
                        pass

                    elif len(qs) == 0:
                        # No  email adresses are using this email address,
                        # so so unique user can be determined
                        content = {'message': 'Geen gebruikersnamen gevonden die horen bij dit email adres.'}
                        logger('authentication').warning(f'Non existent mail address [{email}] requested password reset from IP [{ip_address}]')
                        return Response(content, status=status.HTTP_404_NOT_FOUND)

                    else:
                        # multiple accounts have been found for the email address

                        # Put the usernames in a list
                        list_names = list()
                        for item in qs:
                            list_names.append(item.username)

                        # send a mail with these usernames
                        mailVars = {
                            "users": list_names, 
                            "email": email
                        }
                        subject = 'Klaverjasfun.nl,  gebruikersnamen voor email adres'
                        from_email = 'klaverjasfun@gmail.com'
                        to = [email]
                        bcc = ['klaverjasfun@gmail.com']
                        cc = []
                        html_message = render_to_string('mail_template_multiple_usernames.html', mailVars )
                        plain_message = strip_tags(html_message)
                        send_mail(subject, plain_message, from_email, to, html_message=html_message)

                        #Log sending the reset code
                        logger('authentication').info(f'Send reset code mail for multiple users for mail [{email}] from IP [{ip_address}]')


                        content = {'message': 'Meerdere gebruikersnamen horen bij dit email adres. Er is een mail verstuurd met de verschillende gebruikersnamen.'}
                        return Response(content, status=status.HTTP_404_NOT_FOUND)

                else:
                    # No username and no email
                    content = {'message': 'Gebruikersnaam of email adres moet worden gebruikt'}
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)

            #############################################################################
            #  When a unique user has been found, create the reset_code 
            user_obj = User.objects.get(username=qs[0].username)
            reset_code = createResetCode(code_length)  
            user_obj.reset_code = reset_code

            # Set the Valid until to now + 15 minutes for the reset code
            user_obj.reset_code_valid_until = timezone.now() + timezone.timedelta(minutes=15)
            user_obj.save()

            # Send a mail to the user
            mailVars = {
                "username": user_obj.username, 
                "email": user_obj.email,
                "reset_code": reset_code
            }
            subject = 'Klaverjasfun.nl,  code voor reset wachtwoord'
            from_email = 'klaverjasfun@gmail.com'
            to = [user_obj.email]
            bcc = ['klaverjasfun@gmail.com']
            cc = []
            html_message = render_to_string('mail_template_reset_code.html', mailVars )
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, from_email, to, html_message=html_message)

            #Log sending the reset code
            logger('authentication').info(f'Send reset code mail for user [{user_obj.username}] and mail [{user_obj.email}] on IP [{ip_address}]')
 
            content = {'reset_code': reset_code}
            return Response(content, status=status.HTTP_200_OK)

        except:
            logger('authentication').exception(f'Error creating resetcode for user [{username}] and mail [{email}] from IP [{ip_address}]')
            content = {'reset_code': 'XXXXXXX'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class ResetPassword(APIView):
    """
    A non-authenticated user can set a new password using the reset_code.
    The reset_code is validated to be less than 15 minutes old.

        INPUT: {"username": "ole", "reset_code": "xxxxxxx", "password":"aaaaa"}
        All these input keys should contain valid values

        OUTPUT: No json.
    """
    permission_classes = ( )                # Everybody is allowed use the forgotten password function

    def post(self, request):
        """
        Receive username, reset_code and password.
        These will be validated. When Ok then the new password will be set
        """

        try:
            username    = request.data['username']
            reset_code  = request.data['reset_code']
            password    = request.data['password']

            # Validate username
            # - exists, is unique, is active, 

            try:
                # Get the user, when this fails this will go to except
                user_obj = User.objects.get(username=username)

                # validate that user is active
                if user_obj.is_active == False:
                    content = {'message': 'Wachtwoord reset niet gelukt','username': ['Opgegeven gebruikersnaaam is niet meer actief.']}
                    logger('authentication').warning(f'Reset password failed. User [{username}] is not active anymore')
                    return Response(content, status=status.HTTP_404_NOT_FOUND)

            except:
                logger('authentication').warning(f'Reset password failed. Used incorrect username [{username}]')
                content = {'message': 'Wachtwoord reset niet gelukt','username': ['Incorrecte gebruikersnaam opgegeven.']}
                return Response(content, status=status.HTTP_404_NOT_FOUND)

            # When there is a correct user next validate the reset_code
            # - is not expired, belongs to given username
            # print('DUMMY1',user_obj.reset_code_valid_until.strftime('%Y-%m-%d %H:%M:%S'), timezone.now().strftime('%Y-%m-%d %H:%M:%S'))
            # print(user_obj.reset_code_valid_until.strftime('%Y-%m-%d %H:%M:%S') < timezone.now().strftime('%Y-%m-%d %H:%M:%S'))

            if reset_code != user_obj.reset_code:
                logger('authentication').warning(f'Reset password failed. User [{username}] used incorrect reset code')
                content = {'message': 'Wachtwoord reset niet gelukt','reset_code': ['Opgegeven resetcode is niet correct.']}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                # code is correct, now validate the expiration of code
                if user_obj.reset_code_valid_until.strftime('%Y-%m-%d %H:%M:%S') < timezone.now().strftime('%Y-%m-%d %H:%M:%S'):
                    logger('authentication').warning(f'Reset password failed. User [{username}] used expired reset code')
                    logger('authentication').warning(f"{user_obj.reset_code_valid_until.strftime('%Y-%m-%d %H:%M:%S')} versus {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    content = {'message': 'Wachtwoord reset niet gelukt','reset_code': ['De reset_code is niet meer geldig']}
                    return Response(content, status=status.HTTP_404_NOT_FOUND)

            # Now the reset_code is valid, so the password can be set.
            # First validate the password
            try:
                # validate the password and catch the exception
                validate_password(password=password)

            # the exception raised here is different than serializers.ValidationError
            except exceptions.ValidationError as e:
                content = {'message': 'Wachtwoord reset niet gelukt','password': list(e.messages)}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            user_obj.set_password(password)

            # Also set the reset_code to exipred
            user_obj.reset_code_valid_until = timezone.now() - timezone.timedelta(minutes=1)

            # Save the user object
            user_obj.save()

            logger('authentication').info(f'Reset password completed for user [{username}]')
            content = {'message': 'Wachtwoord van gebruiker is aangepast'}
            return Response(content, status=status.HTTP_201_CREATED)


        except:
            logger('authentication').error(f'Reset password for user [{username}] failed due to internal error.')
            content = {'message': 'Interne fout opgetreden bij het afhandelen van dit verzoek'}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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