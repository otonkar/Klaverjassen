# coinflip/serializers.py


from django.core import exceptions
from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

from coinflip.models import CoinFlipResults

from base.logging.my_logging import logger
from base.lib.my_lib import get_client_ip

from klaverjas.serializers import UserSerializer


class CoinFlipResultsSerializer(serializers.ModelSerializer):
    '''
    For CoinFlipResults
    '''
    user = UserSerializer()

    class Meta:
        model = CoinFlipResults
        fields = '__all__' 
        depth = 1


class CoinFlipResultsSerializerUpdate(serializers.ModelSerializer):
    '''
    For CoinFlipResults
    '''

    class Meta:
        model = CoinFlipResults
        fields = '__all__' 
