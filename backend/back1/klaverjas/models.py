# klaverjas/models.py

from django.db import models
# from datetime import datetime, date
from django.utils import timezone
from computed_property import ComputedTextField
# import os

from my_auth.models import User


class Match(models.Model):
    '''
    Register the matches
    '''
    matchID            = models.CharField(primary_key=True, max_length=30, blank=False, null=False, unique=True)
    owner              = models.ForeignKey(User,on_delete=models.PROTECT, blank=False, null=False)
    description        = models.CharField(max_length=500, blank=True, null=True)
    n_legs             = models.PositiveSmallIntegerField(null=False, blank=False)
    date_created       = models.DateTimeField(default=timezone.now(), blank=False, null=False)
    # cards              = models.CharField(max_length=80000, blank=False, null=False)
    cards              = models.TextField(max_length=80000, blank=False, null=False)
    date_match_start   = models.DateField(blank=True, null=True)     # date when games may start
    date_match_stop    = models.DateField(blank=True, null=True)     # date that no games may be started
    date_register_stop = models.DateField(blank=True, null=True)     # date when no persons may register to the match
    status_color       = ComputedTextField(compute_from='get_status_color', blank = True)

    @property
    def status_color(self):
        # returns a color for bootstrap based on the dates
        #
        # Add the following color codes
        #
        # secondary (grey)  : match play not started and can not register
        # primary(blue)     : match play not started but can register
        # warning(yellow)   : match play started, can not register
        # success (green)   : match play started and can register
        # danger(rood)      : match has stopped

        today = date.today()

        # print(self.matchID)
        before_start = ( today < self.date_match_start )  #True/False
        # print(before_start)
        started = (today >= self.date_match_start and today < self.date_match_stop)
        # print(started)
        register = ( today < self.date_register_stop) 
        # print(register)

        if today >= self.date_match_stop:
            # print('danger')
            return 'danger'  # red   match has stopped
        elif (before_start and  not register):
            # print('secondary')
            return 'secondary'  # grey, match play not started, and can not register
        elif (before_start and register):
            # print('primary')  
            return 'primary'  # blue, match play not started and can register
        elif (started and not register):
            # print('warning')
            return 'warning'  # yellow, match play started, and can not register
        elif (started and register):
            # print('success')
            return 'success'  # green, match play started and can register
        else:
            # print('error')
            return None


class GameStatus(models.Model):
    # Table that contains the status values of the games
    gameStatus          = models.CharField(primary_key=True, max_length=30,blank=False, null=False, unique=True)


# GameStatus = [
#     ('1', 'niet gestart'),
#     ('2', 'wordt gespeeld'),
#     ('3', 'uitgespeeld'),'
#     ('4', 'afgebroken'),
# ]


class Game(models.Model):
    '''
    Register the Games, which are the tables (potjes) of the match to be played.
    A game consists of 4 players: pair A = 0,2  pair B = 1,3
    '''
    gameID              = models.AutoField(primary_key=True)
    matchID             = models.ForeignKey(Match,on_delete=models.PROTECT, blank=True, null=True)
    #gameName            = models.CharField(max_length=20, blank=True, null=True)
    gameStatus          = models.ForeignKey(GameStatus,on_delete=models.PROTECT, default='niet gestart', null=False)
    # gameStatus          = models.CharField(max_length=30, choices=GameStatus, default='niet gestart')
    legs_completed      = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    rounds_completed    = models.PositiveSmallIntegerField(null=True, blank=True, default=0)  # 0  when no round has been played
    date_game_start     = models.DateField(blank=True, null=True)
    date_game_end       = models.DateField(blank=True, null=True)
    scoreA              = models.PositiveSmallIntegerField(null=True, blank=True)
    roemA               = models.PositiveSmallIntegerField(null=True, blank=True)
    scoreB              = models.PositiveSmallIntegerField(null=True, blank=True)
    roemB               = models.PositiveSmallIntegerField(null=True, blank=True)


class Leg(models.Model):
    '''
    Register the completed legs, including winning team and score
    Team A = player 0,2   team B = player 1,3
    '''
    legID               = models.AutoField(primary_key=True)
    gameID              = models.ForeignKey(Game,on_delete=models.PROTECT, blank=True, null=False)
    leg                 = models.PositiveSmallIntegerField(null=True, blank=True)       # The leg that was played [0,..n_leg-1]
    date_completed      = models.DateTimeField(default=timezone.now(), blank=False, null=False)
    player_aangenomen   = models.PositiveSmallIntegerField(null=True, blank=True)       # origonal position of player that heeft aangenomen.
    scoreA              = models.PositiveSmallIntegerField(null=True, blank=True)
    roemA               = models.PositiveSmallIntegerField(null=True, blank=True)
    scoreB              = models.PositiveSmallIntegerField(null=True, blank=True)
    roemB               = models.PositiveSmallIntegerField(null=True, blank=True)
    succeeded           = models.BooleanField(null=False, blank=False, default=False)
    pit                 = models.BooleanField(null=False, blank=False, default=False)
    verzaakt            = models.PositiveSmallIntegerField(null=True, blank=True)    # original player position. If empty than not verzaakt


class GamePlayer(models.Model):
    '''
    Register a player to a game.
    '''
    gameID              = models.ForeignKey(Game,on_delete=models.PROTECT, blank=True, null=False)
    player              = models.ForeignKey(User,on_delete=models.PROTECT, blank=False, null=False)
    position            = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    accepted            = models.BooleanField(null=False, blank=False, default=False)               # Only partner can accept 
    gameCompleted       = models.BooleanField(null=False, blank=False, default=False)               # When collecting score it is easy to filter on this field 
    endScore            = models.PositiveSmallIntegerField(null=True, blank=True)
    endRoem             = models.PositiveSmallIntegerField(null=True, blank=True)


class Troef(models.Model):
    # Table that contains the status values of the games
    troef               = models.CharField(primary_key=True, max_length=30,blank=False, null=False, unique=True)

    # 0 - 'clubs'
    # 1 - 'hearts'
    # 2 - 'spades'
    # 3 - 'diamonds'


class Slag(models.Model):
    '''
    Register a round of cards played, that belongs to a leg in a game
    '''
    gameID              = models.ForeignKey(Game,on_delete=models.PROTECT, blank=True, null=False)
    leg                 = models.PositiveSmallIntegerField(null=False, blank=False, default=0)  # [1,...n_leg ]
    n_slag              = models.PositiveSmallIntegerField(null=False, blank=False, default=0)  # [0,...7 ]
    cards_slag          = models.TextField(max_length=500, blank=False, null=False)
    troef               = models.ForeignKey(Troef,on_delete=models.PROTECT, default='clubs', null=False)
    position_start      = models.PositiveSmallIntegerField(null=False, blank=False, default=0)  # [0,...7 ]
    player_won          = models.PositiveSmallIntegerField(null=False, blank=False, default=0)  # [0,...3 ] original position
    teamA_won           = models.BooleanField(null=False, blank=False, default=False)   #team A is players (0,2)
    score               = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    roem                = models.IntegerField(null=False, blank=False, default=0)
    



