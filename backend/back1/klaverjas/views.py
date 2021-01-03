# klaverjas/views.py

from django.core.mail import send_mail, EmailMessage   
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework import filters, generics, status        # to use the generic views
from rest_framework.response import Response
from rest_framework.views import APIView

import json

from klaverjas import serializers
from klaverjas.klaverjas_lib import klaverjas
from klaverjas.models import Match, Game, GamePlayer, Leg, Slag
from my_auth.models import User

from base.logging.my_logging import logger

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

    To see the score is allowed for everybody.

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


class SlagList(APIView):  
    ''' 
    Get the slagen.
    Can filter on gameID, leg and n_slag to get all slagen for a leg

        url(r'^games/slagen/search/$', views.SlagList.as_view(), name='slag_list'),

        use as:  https://klaverjasfun.nl:5000/klaverjas/games/slagen/search/?gameID=26&leg=2&n_slag=2

    Validation: on who is allowed to see the 'slagen'
    
    '''

    # queryset = Game.objects.all()
    # serializer_class = serializers.SlagSerializer

    def get_queryset(self):
        '''
        Get all the 'slagen' for a leg
        '''

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

    def validate_user_is_allowed(self, gameID, user):
        '''
        Validate that the user is allowed to see the scores.
        The slag is only allowed to be shown 
            * To all players registered to the game
            * When match is stopped everybody can see the legs
            * When match is not stopped, then only players that have finished a game of this match are allowed
        '''

        ### Variable that indicates that user is allowed to see the slag
        is_allowed = False

        ### First check that user is a player of this game
        qs = GamePlayer.objects.filter(gameID = gameID).filter(player__username = user)
        if qs:
            ## Player is part of the game
            is_allowed = True
            # print('ZZ1-user part of game')
        else:
            ## Check that the match has ended (status red/danger)
            try:
                match_obj = Game.objects.get(gameID = gameID).matchID
                match_status = match_obj.status_color
                # print('ZZ1-matchdetails', match_obj.matchID, match_status)
                if match_status == 'danger':
                    ## When match has been stopped everybody may see the legs
                    is_allowed = True
                    # print('ZZ2-match has stopped')
                else:
                    try:
                        ## Check that user has played a game in the same match
                        ## and that the game has been finished (end date of game is not NULL)

                        # Check that user has been registered with a game of that match
                        qs1 = GamePlayer.objects.filter(player__username = user).filter(gameID__matchID__matchID = match_obj.matchID)
                        if qs1:
                            ## Check that the game was finished.
                            ## Note: A user can play multiple games in the same match.
                            ## if at least 1 game is completed then the user is allowed to see the leg
                            for item in qs1:
                                if item.gameID.date_game_end:
                                    is_allowed = True
                                    # print('ZZ3-User plaed the game')
                                else:
                                    # print('ZZ4-User did niet finish the game')
                                    pass
                    except:
                        is_allowed = False
                        # print('ZZ5-except')
            except:
                is_allowed = False
                # print('ZZ6-except')

        return is_allowed


    def get(self, request):
        ### Define the get for the APIView.
        user = request.user
        gameID = request.query_params.get('gameID', None)
        # print('XX', user, gameID)

        is_allowed = self.validate_user_is_allowed(gameID, user)
        # print('ZZ6-is-allowed', is_allowed, gameID)

        model = self.get_queryset()
        serializer = serializers.SlagSerializer(model, many=True)

        if is_allowed:
            return Response([serializer.data, is_allowed])
        else:
            ### send and empty array so that the info can not be seen even in the API.
            return Response([ [], is_allowed])


class MailToPlayers(APIView):
    """
    This view is to receive a flat mail text that must be send to the players
    that belong to the same game

        INPUT: {"gameID": 17, "mailText": "This is a text ....."}


        OUTPUT: Mail to players
    """

    def post(self, request):
        """
        Receive gameID and mailText.
        Validate that user is part of the game.
        Send mails to participants.
        """

        try:
            user        = request.user
            gameID      = request.data['gameID']
            mailText    = request.data['mailText']

            # print('XX', user, gameID, mailText)

            ## Get the players with mail address 
            players = GamePlayer.objects.filter(gameID = gameID)

        
            ###  Get the mail addresses
            ### and check that user is a player of this game
            mail_addresses = list()
            user_is_valid = False
            for player in players:
                if str(player.player.username) == str(user):
                    user_is_valid = True
                    user_mail_address = player.player.email

                # print(player.player.username, user)
                # print(player.player.email)
                mail_addresses.append(player.player.email)

            # ## remove the user mail address from the mail list
            # mail_addresses.remove(user_mail_address)

            if not user_is_valid:
                content = [False, 'Mail is niet verstuurd. U bent geen speler van dit potje.']
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)

        
            ## there must be at least 1 mail adress and the user mail address
            if len(mail_addresses) < 2 :
                content = [False, 'Mail is niet verstuurd. Er zijn nog geen andere speler aangemeld om een mail naar te sturen.']
                return Response(content, status=status.HTTP_400_BAD_REQUEST)


            ### Send the mail
            # send a mail with the variables for the mail template.
            mailVars = {
                "gameID"    : gameID, 
                "user"      : user,
                "mailText"  : mailText,
            }

            mail_addresses.append('klaverjasfun@gmail.com')
            subject = f'Klaverjasfun.nl, bericht voor potje {gameID}.'
            from_email = 'klaverjasfun@gmail.com'
            to = []
            bcc = mail_addresses
            cc = []
            
            html_message = render_to_string('mail_template_mail_to_players.html', mailVars )
            plain_message = strip_tags(html_message)
            
            # send_mail(subject, plain_message, from_email, to, html_message=html_message)

            html_message
            email = EmailMessage(
                subject,
                html_message,
                from_email,
                to,
                bcc,
                reply_to=['klaverjasfun@gmail.com']
            )

            email.content_subtype = "html"
            email.send(fail_silently=True)

            #Log sending the reset code
            logger('default').info(f'Send mails for user [{user}] for game {gameID}. ')

        except:
            content = [False, 'Mail is niet verstuurd. Er is een fout opgetreden bij het versturen van de mails']
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


        content = [True, 'De mail is verstuurd naar de andere speler(s).']
        return Response(content, status=status.HTTP_200_OK)
