# klaverjas/views.py

from rest_framework import generics         # to use the generic views
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.views import APIView

import json

from klaverjas import serializers
from klaverjas.klaverjas_lib import klaverjas
from klaverjas.models import Match, Game, GamePlayer, Leg, Slag
from my_auth.models import User

from base.logging.my_logging import create_logger

class MatchCreate(generics.CreateAPIView):
    '''
    Create a new match
    '''
    queryset = Match.objects.all()
    serializer_class = serializers.MatchCreateSerializer

    # Automatically add the request user as owner of the match
    def perform_create(self, serializer):

        # Add the owner
        serializer.save(owner=self.request.user)

        # Create the cards
        # use: serializer.validated_data['matchID'] or
        #      serializer.data['matchID']

        cards = klaverjas.CreateMatchDecks(serializer.validated_data['n_legs'])
        # store the cards as a json format
        cards = json.dumps(cards)
        serializer.save(cards=cards)


class UserRetrieve(generics.RetrieveAPIView):
    '''
    Get the id and username of a user
    '''
    
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset 

    # Change the default pk as lookup to the matchID
    def get_object(self):
        # get the matchID from the url
        username = self.kwargs.get("username")
        return User.objects.get(username=username)


class GameCreate(generics.CreateAPIView):
    '''
    Create a new Game
    '''
    queryset = Game.objects.all()
    serializer_class = serializers.GameCreateSerializer


class PlayerCreate(generics.CreateAPIView):
    '''
    Create a new Player
    '''
    queryset = GamePlayer.objects.all()
    serializer_class = serializers.PlayerSerializer


class PlayerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get, update (PUT)  or delete a player
    '''
    queryset = GamePlayer.objects.all()
    serializer_class = serializers.PlayerSerializer



class MatchList(generics.ListAPIView):  
    ''' 
    List the current matches. Do not show the cards
    Send the complete list to the front-end.
    The front-end can do additional filtering
    '''

    serializer_class = serializers.MatchListSerializer

    def get_queryset(self):
        """
        Possibily to add search arguments
        """
        queryset = Match.objects.all().order_by('-date_created')

        return queryset


class MatchRetrieveUpdate(generics.RetrieveUpdateAPIView):
    '''
    View the match details or update a match
    '''
    
    serializer_class = serializers.MatchRetreiveUpdateSerializer

    def get_queryset(self):
        queryset = Match.objects.all()
        return queryset 

    # Change the default pk as lookup to the matchID
    def get_object(self):
        # get the matchID from the url
        matchID = self.kwargs.get("matchID")
        return Match.objects.get(matchID=matchID)

    def perform_update(self, serializer):

        # Create the cards with the new n_legs coming from the PUT (update)
        # print('***self ', self.__dict__)
        # print('***validated_data ',serializer.validated_data)

        instance = serializer.save()

        matchID = self.kwargs.get('matchID')

        # First get the current value of n_legs
        qs = Match.objects.get(matchID=matchID)

        # Only update the cards when n_legs has been changed.
        if qs.n_legs != serializer.validated_data['n_legs']:
            cards = klaverjas.CreateMatchDecks(serializer.validated_data['n_legs'])
            # store the cards as a json format
            cards = json.dumps(cards)
            serializer.save(cards=cards)
            print('*********** CARDS UPDATED')


class PlayerList(generics.ListAPIView):  
    ''' 
    List the current matches, with games and players
    '''

    # queryset = GamePlayer.objects.all()
    serializer_class = serializers.PlayerListSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['position']

    def get_queryset(self):
        """
        Possibily to add search based on arguments
        Add in urls.py:   
            url(r'^players/search/$', views.PlayerList.as_view(), name='players_list'),
        filtering on options
           http://klaverjasfun.nl:5000/klaverjas/players/search/?matchID=Match1&gameID=1&playerName=Test1

        The search parameters will be received as a dictionary like,
            <QueryDict: {'matchID': ['Match1'], 'gameID': ['1'], 'playerName': ['Test1']}>

        """
        queryset = GamePlayer.objects.all()

        # Get the filtersettings 
        # print(self.request.query_params)
        value_matchID = self.request.query_params.get('matchID', None)
        value_gameID = self.request.query_params.get('gameID', None)
        value_playerName = self.request.query_params.get('playerName', None)
        #print(value_matchID, value_gameID, value_playerName)

        # sequential filtering on queryset results in AND filtering

        # Exact search on matchID
        if value_matchID is not None:
            queryset = queryset.filter(gameID__matchID=value_matchID)

        # Exact search on gameID
        if value_gameID is not None:
            queryset = queryset.filter(gameID=value_gameID)

        # Exact search on playername
        if value_playerName is not None:
            queryset = queryset.filter(player__username=value_playerName)

        # for item in queryset:
        #     print(item.id)


        return queryset.order_by('gameID', 'position')


class Game2MatchList(generics.ListAPIView):  
    ''' 
    Show which games belong to a match.
    Can filter on matchID to get all games for that match

        url(r'^games/search/$', views.Game2MatchList.as_view(), name='game_list'),

        use as:  http://145.53.40.4:8000/klaverjas/games/search/?matchID=Match1 


    '''

    # queryset = Game.objects.all()
    serializer_class = serializers.Game2MatchSerializer

    def get_queryset(self):

        queryset = Game.objects.all()

        # Get the filtersettings 
        value_matchID = self.request.query_params.get('matchID', None)

        # Exact search on matchID
        if value_matchID is not None:
            queryset = queryset.filter(matchID=value_matchID)

        return queryset.order_by('-matchID', '-gameID')


class GameScore(APIView):
    """
    Get the score of game
    ..../klaverjas/game/score/?gameID=28

    Get request 

    returns a list containining two lists
    * List 1 is a list of legs with scores
    * List 2 is a list with the totalscore for that gameID
      (totalscoreA, totalroemA, totalscoreB, totalroemB)

    """

    def get(self, request, format=None):
        """
        Get the score of a game
        """

        serializer = serializers.LegSerializer

        queryset = Leg.objects.all()

        value_gameID = self.request.query_params.get('gameID', None)
        # Exact search on gameID
        if value_gameID is not None:
            qs = queryset.filter(gameID=value_gameID).order_by('leg')

        print('DUMMY1')

        # define the lists
        leginfo = []
        scoreA = []
        scoreB = []
        roemA = []
        roemB = []
        totalscoreA = 0
        totalscoreB = 0
        totalroemA = 0
        totalroemB = 0

        if len(qs) != 0:
            for item in qs:
                # store the leg info as regular data object
                data = serializer(item).data
                leginfo.append(data)
                
                totalscoreA = totalscoreA + item.scoreA
                totalscoreB = totalscoreB + item.scoreB
                totalroemA = totalroemA + item.roemA
                totalroemB = totalroemB + item.roemB
        
        return Response( [leginfo, [totalscoreA, totalroemA, totalscoreB, totalroemB] ] )


class SlagList(generics.ListAPIView):  
    ''' 
    Get the slagen.
    Can filter on gameID, leg and n_slag to get all slagen for a leg

        url(r'^games/slagen/search/$', views.SlagList.as_view(), name='slag_list'),

        use as:  https://klaverjasfun.nl:5000/klaverjas/games/slagen/search/?gameID=26&leg=2&n_slag=2


    '''

    # queryset = Game.objects.all()
    serializer_class = serializers.SlagSerializer

    def get_queryset(self):

        queryset = Slag.objects.all()

        # Get the filtersettings 
        value_gameID    = self.request.query_params.get('gameID', None)
        value_leg       = self.request.query_params.get('leg', None)
        value_n_slag    = self.request.query_params.get('n_slag', None)

        # Exact search on gameID
        if value_gameID is not None:
            queryset = queryset.filter(gameID=value_gameID)

        # Exact search on leg
        if value_leg is not None:
            queryset = queryset.filter(leg=value_leg)
        
        # Exact search on n_slag
        if value_n_slag is not None:
            queryset = queryset.filter(n_slag=value_n_slag)

        return queryset.order_by('id')

