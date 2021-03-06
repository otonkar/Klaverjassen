# my_auth/serializers.py

from django.utils import timezone

from django.core.mail import send_mail                                  # EmailMultiAlternatives, 

from django.core import exceptions
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from my_auth.models import User, LogUser

from base.logging.my_logging import logger


class OleTokenObtainPairSerializer(TokenObtainSerializer):
    '''
    Change the standaard TokenobtainPairSerializer to include
    logging of users that get a token
    '''

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        #@Ole Add the logging 
        now = timezone.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        # f = open("/apps/Klaverjassen/log/klaverjas_login.txt", "a")
        # log_text = "*** " + dt_string + ',   Username : ' +  str(self.user) + "\n"  
        # f.write(log_text)
        # f.close()

        #@Ole also log this user in the LogUser table
        log = LogUser()
        log.user = self.user
        log.timestamp = now
        log.save()

        #Log the login
        logger('authentication').info(f'[{str(self.user)}] has logged in')
        # logger('debug').debug('This is a debug test')

        return data


class UserSignUpSerializer(serializers.ModelSerializer):
    # View to use for sign up

    class Meta:
        model = User
        # fields = '__all__'
        ## Or specify the fields manually
        fields = [
          'username',
          'password',
          'first_name',
          'last_name',
          'email'
        ]
        # make use that password is read-only
        extra_kwargs = {
                    'password': {'write_only': True}
        }
        # depth = 1     # Specify how deep the (left)joined data must be included (nested serialization)

    def save(self):
        # Define what needs to be saved
        # use validated_data as the input from the API

        # Create a User with the variable from validated data
        user = User(
            username    = self.validated_data['username'],
            first_name  = self.validated_data['first_name'],
            last_name   =  self.validated_data['last_name'],
            # It is possible to change the data. Then make sure to also update the validated_data
            # otherwise the old value will be shown in the API reponse
            # last_name   =  'XXX', 
            email       = self.validated_data['email']
        )

        # validate the password using the default password validators
        password = self.validated_data['password']
        # password = data.get('password')

        # When validating the password using the validate_password then 
        # the error must be catched, otherwise this whole serializer will result in an error

        errors = dict() 
        try:
            # validate the password and catch the exception
            validate_password(password=password)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)
        else:
            # Add the password to the user and save to the database
            user.set_password(password)
            user.save()

        # Log the registration of a new user
        now = timezone.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        # f = open("/apps/Klaverjassen/log/klaverjas_registration.txt", "a")
        # log_text = '*** ' + dt_string + ', Username: ' + self.validated_data['username'] \
        #             + ', Naam: ' + self.validated_data['first_name'] + ' ' + self.validated_data['last_name'] \
        #             + ', Email: ' + self.validated_data['email'] +  "\n"  
        # f.write(log_text)
        # f.close()

        # log the registration 
        logger_text = 'Username: ' + self.validated_data['username'] \
                    + ', Naam: ' + self.validated_data['first_name'] + ' ' + self.validated_data['last_name'] \
                    + ', Email: ' + self.validated_data['email']  
        logger('registration').info(f'{logger_text}')

        try:
            # send a mail
            subject='New user registered'
            message_text = '*** ' + dt_string + ', Username: ' + self.validated_data['username'] \
                        + ', Naam: ' + self.validated_data['first_name'] + ' ' + self.validated_data['last_name'] \
                        + ', Email: ' + self.validated_data['email'] 
            mailfrom='klaverjasfun@gmail.com'  
            mailto='ole.karlsen@gmail.com'
            send_mail(
                subject,
                message_text,
                mailfrom,
                [mailto],
                fail_silently=False,
            )
        except:
            logger('errors').exception('Mail could not be sent')

        
        # Example to change the value that must be stored and displayed in the response
        # self.validated_data['last_name'] = 'XXX'


    def validate_username(self, value):
        # Validation on username
        #  - validate that username does not already exist
        #  - ....

        # Validation on unique username is already done due to unique =True in the model
        # qs = User.objects.filter(username__exact=value)

        # if qs.exists():
        #     raise serializers.ValidationError("Username already exists!")
        # else:
        return value


