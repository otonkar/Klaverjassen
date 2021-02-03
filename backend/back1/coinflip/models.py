# coinflip/models.py

# from datetime import date
from django.db import models
from django.utils import timezone
# from computed_property import ComputedTextField

from my_auth.models import User


class CoinFlipResults(models.Model):
    '''
    Register the results of the coin flips.

    '''
    ID                  = models.AutoField(primary_key=True)
    user                = models.ForeignKey(User,on_delete=models.PROTECT, blank=False, null=False)
    nToss               = models.PositiveSmallIntegerField(null=True, blank=True)
    nHeads              = models.PositiveSmallIntegerField(null=True, blank=True)
    chance              = models.DecimalField(max_digits = 11, decimal_places = 8)
    in_play             = models.BooleanField(null=False, blank=False, default=False)
    date_updated        = models.DateTimeField(default=timezone.now, blank=False, null=False)
