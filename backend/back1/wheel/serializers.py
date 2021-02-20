# wheel/serializers.py


from django.core import exceptions
from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

from wheel.models import WheelSettings

from base.logging.my_logging import logger
from base.lib.my_lib import get_client_ip

from klaverjas.serializers import UserSerializer
from my_auth.models import User


# class WheelSettingsSerializer(serializers.Serializer):
class WheelSettingsSerializer(serializers.ModelSerializer):
    '''
    For WheelSettings
    '''

    class Meta:
        model = WheelSettings
        fields = '__all__' 
        # fields = [
        #     'ID',
        #     'name',
        #     #'user',           #Determine user based on request
        #     'userSettings',
        #     'userInput',
        # ]
        # depth = 1


    # ID              = serializers.IntegerField(label='ID', read_only=True)
    # name            = serializers.CharField(max_length=50)
    # userSettings    = serializers.CharField(label='UserSettings', max_length=1000, style={'base_template': 'textarea.html'})
    # userInput       = serializers.CharField(label='UserInput', max_length=80000, style={'base_template': 'textarea.html'})
    # user            = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())



    def create(self, validated_data):
        '''
        Store the wheel settings.
        Get the user from the request and add it to the wheelSettings.
        '''

        # Get the user from the request
        # user_obj  = self.context['request'].user

        # Add the user to the wheelSettings
        wheelSettings = WheelSettings.objects.create(**validated_data)

        return wheelSettings
        

    def update(self, instance, validated_data):
        '''
        Update the instance only for settings and input.
        Set the new value when present in the data, else use the existing value
        '''
        print('YY1', instance)
        instance.userSettings   = validated_data.get('userSettings', instance.userSettings)
        print('YY2')
        instance.userInput      = validated_data.get('userInput', instance.userInput)
        instance.name   = validated_data.get('name', instance.name)
        instance.user   = validated_data.get('user', instance.user)

        instance.save()

        return instance

        



        


