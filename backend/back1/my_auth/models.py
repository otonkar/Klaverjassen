# my_auth/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    # add additional fields in here
    username            = models.CharField(max_length=150, unique=True)
    is_logged_in        = models.BooleanField(default=False)
    is_playing_game     = models.BooleanField(default=False)
    is_klaverjas_admin  = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class BlackListedToken(models.Model):
    '''
    Model to store tokens/user combinations when a user has been logged out.
    When an item in this blacklist exists it means that the token is may
    not be used anymore.
    '''

    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("token", "user")

    def __str__(self):
        return str(self.user) + ' - ' + str(self.token)
