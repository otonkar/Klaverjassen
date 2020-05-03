#appwebsocket/models.py

from django.db import models



class WSConnectedStatus(models.Model):
    '''
    Register for a player position 0,1,2,3 the status of being connected to 
    the Websocket. True = connected, False =  disconnected
    '''
    position            = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    gameID              = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    connected           = models.BooleanField(null=False, blank=False, default=False)    
    channel             = models.CharField(max_length=50, blank=False, null=False, default='not known')
