# wheel/models.py

# from datetime import date
from django.db import models
from django.utils import timezone
# from computed_property import ComputedTextField

from my_auth.models import User


class WheelSettings(models.Model):
    '''
    Store the settings for the Wheel for a user

    '''
    ID                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=50, blank=False, null=False)
    user                = models.ForeignKey(User,on_delete=models.PROTECT, blank=False, null=False)
    userSettings        = models.TextField(max_length=1000, blank=False, null=False)
    userInput           = models.TextField(max_length=80000, blank=False, null=False)

