# chat/consumers.py
import json
from datetime import datetime, date
from channels.generic.websocket import AsyncWebsocketConsumer

from django.db.models import Sum

from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async

# from klaverjas.serializers import MatchSerializer, GameSerializer, PlayerSerializer, PlayerListSerializer, LegSerializer
from klaverjas.klaverjas_lib.klaverjas import sortCards, evaluateSlag, countRound

from my_auth.models import User
from appwebsocket.models import WSConnectedStatus
from klaverjas import serializers
from klaverjas.models import Match, Game, GamePlayer, Slag, Troef, GameStatus, Leg


####################################################################################
##
## For ORM queries in a async function follow the instructions of
##      https://www.tutorialdocs.com/tutorial/django-channels/database-access.html


@database_sync_to_async
def set_connected_status(gameID, position, channel):
    '''
    Update the status of a player at a position at the table at a game.
    Use this function when a player connects to the game.
    '''
    # first check that an entry for that game/position exists
    # if not, create an entry
    qs = WSConnectedStatus.objects.filter(gameID=gameID, position=position)
    if len(qs) > 0:
        obj = WSConnectedStatus.objects.get(gameID=gameID, position=position)
        obj.connected = True
        obj.channel = channel
        obj.save()
    else: 
        entry = WSConnectedStatus()
        entry.gameID = gameID
        entry.position = position
        entry.connected = True
        entry.channel = channel
        entry.save()
        print('++ Entry created ', gameID, position, channel)


@database_sync_to_async
def set_disconnected_status(channel):
    '''
    Update the status of a player at a position at the table at a game.
    Use this function when a player connection gets disconnected.
    There should already be an db entry for this connection.
    If it doen not exist there is no need to create one, because no entry implies not connected
    '''
    # first check that an entry for that game/position exists
    # if not, create an entry
    gameID = 5
    qs = WSConnectedStatus.objects.filter(channel=channel)
    if len(qs) == 1:
        obj = WSConnectedStatus.objects.get(channel=channel)
        obj.connected = False
        obj.channel = ''
        gameID = obj.gameID
        obj.save()
       
    return gameID


@database_sync_to_async
def get_connected_status_of_players(gameID):
    '''
    For a game get the status of all players (positions) as registered in the database
    '''
    qs = WSConnectedStatus.objects.filter(gameID=gameID)

    # Create a new list with position and connection status.
    # A position can be empty, this implies connected =  False
    result = list()
    for item in qs:
        result.append((item.position, item.connected))

    return result


@database_sync_to_async
def get_players(gameID):
    '''
    For a game get the players
    '''
    qs = GamePlayer.objects.filter(gameID=gameID).order_by('position')

    serializer = serializers.PlayerListSerializer(qs, many=True)
    # print(serializer.data)

    return serializer.data


@database_sync_to_async
def get_player_cards(matchID, gameID, leg, position, troef):
    '''
    For a specific game, get the cards for a players (position) of the leg n.  [0...n_leg-1]
    Position here is the position in the registration,
    '''
    match = Match.objects.get(matchID=matchID)

    #!!! Can not use MatchSerializer, because this serializer does not return cards
    # serializer = MatchSerializer(match)
    # print(serializer.data)

    # print('DUMMY2', type(match.cards) )
    # Note: cards were stored in the db as json.dumps in a TextField.
    # Convert to python object using json.loads. Then get the correct set.
    cards = json.loads(match.cards)
    cards = cards[leg][position]
    # print('DUMMY3')

    # Sort the cards 
    # make sure the same order of colors is used as in Vue.
    colors = ('clubs','hearts', 'spades', 'diamonds')
    troefcolor = colors[troef]
    # print('DUMMY4', troefcolor)

    sorted_cards = sortCards(cards,troefcolor)
    # sorted_cards.reverse()        # When we want the cards shown in inverted order

    # print('Get player cards succeeded')

    return sorted_cards


@database_sync_to_async
def get_played_cards_of_leg(gameID, leg, position):
    '''
    For a specific leg in a game, get the cards that have already been played by player on a position
    Position here is the position in the registration,
    '''

    # Get the list of played cards
    qs = Slag.objects.filter(gameID=gameID, leg=leg)
    played_cards = []

    if len(qs) == 0:
        return played_cards           # empty set of cards
    else:
        # get the cards played for a position in a leg
        for slag in qs:
            cards = json.loads(slag.cards_slag)
            played_cards.append(cards[position])

        return played_cards

    # print('Get played cards of leg succeeded')

@database_sync_to_async
def get_match(matchID):
    '''
    Get  a match object with the details of that match
    '''
    match = Match.objects.get(matchID=matchID)

    # print('GET Match succeeded')

    return match

@database_sync_to_async
def get_game(gameID):
    '''
    Get  a game object with the details of a game with gameID
    '''
    game = Game.objects.get(gameID=gameID)

    # print('GET GAME succeeded')

    return game

@database_sync_to_async
def save_game(game):
    '''
    save  a game object 
    '''
    game.save()
    # print('save_game succeeded')

@database_sync_to_async
def update_game(input_data):
    '''
    update the data of game with gameID
    '''

    serializer = serializers.GameSerializer(data=input_data) 
    print('****', input_data)

    if serializer.is_valid():
        serializer.save()
    


@database_sync_to_async
def get_troef(troef):
    '''
    Get a troef instance
    '''
    
    troef = Troef.objects.get(troef=troef)
    # print('get_troef succeeded')

    return troef

@database_sync_to_async
def get_slag(gameID, leg, round):
    '''
    get  a slag object 
    '''
    slag = Slag.objects.get(gameID=gameID, leg=leg, n_slag=round)
    # print('get_slag succeeded')

    return slag

@database_sync_to_async
def delete_slag(gameID, leg, round):
    '''
    delete one or multiple rounds for a gameID/leg/round number
    '''
    qs = Slag.objects.filter(gameID=gameID, leg=leg, n_slag=round)

    if len(qs) != 0:
        # print('-----')
        for slag in qs:
            # print('Delete slag')
            slag.delete()


@database_sync_to_async
def save_slag(slag):
    '''
    save  a slag object 
    '''
    slag.save()
    # print('save_slag succeeded')

@database_sync_to_async
def get_roem(gameID, leg):
    '''
    Get the total roem for both parties in a current leg
    '''
    # Roem A
    qs = Slag.objects.filter(gameID=gameID, leg=leg, teamA_won=True)
    if len(qs) != 0:
        totalRoemA = qs.aggregate(Sum('roem'))
    else: 
        totalRoemA = {'roem__sum': 0}

    # Roem B
    qs = Slag.objects.filter(gameID=gameID, leg=leg, teamA_won=False)
    if len(qs) != 0:
        totalRoemB = qs.aggregate(Sum('roem'))
    else: 
        totalRoemB = {'roem__sum': 0}


    # ## Get the sum of roem when teamA has won
    # totalRoemA = Slag.objects.filter(gameID=gameID, leg=leg, teamA_won=True).aggregate(Sum('roem'))
    # totalRoemB = Slag.objects.filter(gameID=gameID, leg=leg, teamA_won=False).aggregate(Sum('roem'))

    return [totalRoemA, totalRoemB]

@database_sync_to_async
def get_current_scores(gameID):
    '''
    For a game get the scores and roem per leg
    To be shown during the play of the game.
    Get the a list with scores per leg.
    Also get the total score over all played legs
    '''
    
    qs = Leg.objects.filter(gameID=gameID).order_by('leg')

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
            data = serializers.LegSerializer(item).data
            leginfo.append(data)
            
            totalscoreA = totalscoreA + item.scoreA
            totalscoreB = totalscoreB + item.scoreB
            totalroemA = totalroemA + item.roemA
            totalroemB = totalroemB + item.roemB
    
    return [leginfo, [totalscoreA, totalroemA, totalscoreB, totalroemB] ]
            

@database_sync_to_async
def get_gameStatus(status):
    '''
    Get  a game status
    '''
    gameStatus = GameStatus.objects.get(gameStatus=status)

    # print('GET Match succeeded')

    return gameStatus

@database_sync_to_async
def save_leg(input_data):
    '''
    Save a Leg using a serializer
    '''
    serializer = serializers.LegSerializer(data=input_data)

    if serializer.is_valid():
        serializer.save()
        print('Serializer OK')

@database_sync_to_async
def delete_leg(gameID, leg):
    '''
    delete a registerd leg 
    '''
    qs = Leg.objects.filter(gameID=gameID, leg=leg)

    if len(qs) != 0:
        # print('-----')
        for leg in qs:
            # print('Delete slag')
            leg.delete()


@database_sync_to_async
def evaluate_leg(gameID, leg):
    '''
    Determine the winner and scores for a completed leg
    '''
    qs = Slag.objects.filter(gameID=gameID, leg=leg)
    

    if len(qs) != 8:
        print('WARNING: Leg not properly completed')
        return 'Leg not properly completed'
    else:
        # Determine who took om this leg. (heeft aangenomen)
        player_aangenomen = leg % 4  # In the game variant 'verplicht aannemen'
        
        total_score_A = 0
        total_score_B = 0
        total_roem_A = 0
        total_roem_B = 0
        # determine the total score and roem for both teams
        for slag in qs:
            if slag.teamA_won == True:
                total_score_A = total_score_A + slag.score
                total_roem_A = total_roem_A + slag.roem
            else:
                total_score_B = total_score_B + slag.score
                total_roem_B = total_roem_B + slag.roem

        # Check that the player of Team A succeeded in playing the leg (is 'door')
        if player_aangenomen == 0 or player_aangenomen == 2:
            team = 'team A'
            succeeded = (total_score_A + total_roem_A ) > (total_score_B + total_roem_B )
            if not succeeded:
                # als 'nat'
                total_score_A = 0
                total_roem_A = 0
                total_score_B = 162
                total_roem_B = (total_roem_A + total_roem_B)

            if succeeded and total_score_A == 162:
                total_roem_A = total_roem_A + 100
                pit = True 
            else:
                pit = False

        # Check that the player of Team B succeeded in playing the leg (is 'door')
        if player_aangenomen == 1 or player_aangenomen == 3:
            team = 'team B'
            succeeded = (total_score_B + total_roem_B ) > (total_score_A + total_roem_A )
            if not succeeded:
                # als 'nat'
                total_score_B = 0
                total_roem_B = 0
                total_score_A = 162
                total_roem_A = (total_roem_A + total_roem_B)

            if succeeded and total_score_B == 162:
                total_roem_B = total_roem_B + 100
                pit = True 
            else:
                pit = False

    return [player_aangenomen, succeeded, pit, team, total_score_A, total_roem_A, total_score_B, total_roem_B]

class ChatConsumer(AsyncWebsocketConsumer):

    ## CONNECT
    async def connect(self):
        #@ Currently there is no validation on user, so everybody can connect to a channel
        #@ Needs to add an authentication
        self.gameID = self.scope['url_route']['kwargs']['gameID']
        self.group_name = 'game_%s' % self.gameID

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # can add here a validation before the accept
        await self.accept()

        # On connect send a confirmation with channelname to the client
        # the client can then send a back message with channel, gameid and position 
        # to be stored in the database
        message = { 
            'type': 'confirm_connected',
            'channel': self.channel_name
        }

        # Only send the the client (not to the group)
        await self.send(text_data=json.dumps(message))
        print('Connection created : ', self.channel_name)



    ## DISCONNECT
    async def disconnect(self, close_code):
        

        # On disconnect update the status in the database and
        # send the new stattusses of the game on the group
        # Update the status in the table
        gameID = await set_disconnected_status(self.channel_name)

        # Get all connected players of that game
        connected_positions = await get_connected_status_of_players(gameID)

        # send this info to all players in the group.
        message = {
            'type'      : 'statusUpdate',
            'status'    : connected_positions
        }

        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name, 
            {
                'type': 'send_to_group',        ## Based on this name a function to handle is created
                'message': message
            }
        )

        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

        print('@@@ DISCONNECTED')


    # CLIENT RECEIVE messages from websocket client
    async def receive(self, text_data):
        message = json.loads(text_data)     # converts the data to Python


        ###### Functions to handle the different request types

        #####################################################################################################
        #### TYPE: connected_update
        ## register this player as connected and send all connection statusses of that game to all players
        if message['type'] == 'connected_update':
            print('@@@ CONNECTED_UPDATE')
            await self.connected_update(message)

        #####################################################################################################
        #### TYPE: handle_verzaken
        ## Show to all players that a player has noted verzaakt
        if message['type'] == 'notify_verzaken':
            print('@@@ HANDLE_VERZAKEN')
            await self.notify_verzaken(message)

        #####################################################################################################
        #### TYPE: process_verzaken
        ## Show to all players that a player has noted verzaakt
        # if message['type'] == 'process_verzaken':
        #     print('@@@ PROCESS_VERZAKEN')
        #     await self.process_verzaken(message)

        
        #####################################################################################################
        #### TYPE: get_players   !NOT USED ANYMORE !!!
        elif message['type'] == 'get_players':
            # Get the players for a gameID
            print('@@@ GET_PLAYERS')
           
            message = json.loads(text_data)     # converts the data to Python
            # print('**', message)

            players = await get_players(message['gameID'])

            # send this info to all players in the group.
            message = {
                'type'      : 'send_players',
                'players'   : players
            }

            # Send message to room group
            await self.channel_layer.group_send(
                self.group_name, 
                {
                    'type': 'send_to_group',        ## Based on this name a function to handle is created
                    'message': message
                }
            )

            # print('GET_PLAYERS')


        #####################################################################################################
        #### TYPE: request_new_round
        ### Send to info to the player to play a new round
        ### Sends back 8 cards, but the cards that have been played in the previous rounds
        ### will be set to no card. This ensures that the cards will be shown on the same position as 
        ### in the previous round.
        ### Also a signal will be send to all other player to load the round.
        ### The troef is klaver for every first round. For the next rounds the troef will be the samen
        ### as the first round
        ###
        elif message['type'] == 'request_new_round':
            print('@@@ REQUEST_NEW_ROUND')

            message = json.loads(text_data)     # converts the data to Python
            # print('**', message)

            # Set the variables to be used.
            matchID         = message['matchID']
            gameID          = message['gameID']
            position        = message['position']
            troef           = message['troef']              # Needs to be included when troef is changed in first round
            button_pressed  = message['button_pressed']

            # print('DUMMY20', matchID, gameID, position, troef )

            ### FIRST: get the information of the game
            game = await get_game(message['gameID'])
            current_leg     = game.legs_completed       # when 0 are completed get leg 0 for the new leg
            current_round   = game.rounds_completed

            ##@@@@@ Only do this when current_leg < n_leg (get from match)
            if current_leg < message['n_legs']:

                ### NEXT Determine the troef that needs to be send
                ### In the first round the default troef is clubs. This can be changed.
                ### In the next rounds in the leg the same troef will be used as in round 0
                troef_choices = ['clubs', 'hearts', 'spades', 'diamonds']
                if current_round != 0:
                    # get the troef from round = 0
                    slag = await get_slag(gameID, current_leg, 0 )
                    for i in range(len(troef_choices)):
                        if troef_choices[i] == slag.troef_id:
                            troef = i
                


                ### NEXT: get all cards of the leg and sort this for the troef
                cards_all = await get_player_cards(matchID, gameID, current_leg, position, troef)

                ### NEXT: get all played cards in the previous rounds of this leg for a position (player)
                played_cards = await get_played_cards_of_leg(gameID, current_leg, position)
                # print('played cards :', played_cards)

                ### NEXT: Remove the playeds cards from the hand, by setting the card to blank
                ### that is, set color and rank to 'no-card'

                cards = cards_all
                for i in range(len(cards)):
                    # check all cards in the hand to match a played card.
                    # When they match then the card will be set to no-card

                    # If played cards is empty the for loop will be skipped
                    # In that case assign all cards to the cards list
                    if len(played_cards) != 0:
                        for played in played_cards:
                            if cards[i] == played:
                                cards[i] = {'color': 'no-card', 'rank': 'no-card' }


                # print('position ', position, cards)

                ### NEXT: Determine which player has to start this round.
                if current_round == 0:
                    next_to_play = current_leg % 4
                else: 
                    # When cards in the round have been played,
                    # then the next person to start depends on the winner of the previous round
                    slag = await get_slag(gameID, current_leg, current_round - 1)
                    next_to_play = slag.player_won

                ## Determine the total roem thusfar in the leg for both parties 
                ## roem is a list of two values for team A and teamB
                ## Note: roem for teamA is : roem[0]['roem__sum']
                roem = await get_roem(gameID, current_leg)     # do not need current_round

                ### Send the information to only the player that requested this new round.
                # Only send to the client (not to the group)
                message = {
                    'type'          : 'send_new_round',
                    'cards'         : cards,
                    'next_to_play'  : next_to_play,
                    'current_leg'   : current_leg,
                    'current_round' : current_round,
                    'troef'         : troef,
                    'roem'          : roem          # is a list with the values of roemA and roemB
                    
                }

                # if not button pressed it only needs to be send to a single player
                if button_pressed == False:
                    await self.send(text_data=json.dumps(message))

                ### Send a message to the other players to if buttonpressed = true

                if button_pressed == True:
                    message = {
                    'type'          : 'signal_to_load_new_round'
                    }

                    # Send message to room group
                    await self.channel_layer.group_send(
                        self.group_name, 
                        {
                            'type': 'send_to_group',        ## Based on this name a function to handle is created
                            'message': message
                        }
                    )

            ### end if
                


        #####################################################################################################
        #### TYPE: request_player_cards
        ### This sends the cards to only the player that reqeusted the cards
        elif message['type'] == 'request_player_cards':
            print('@@@ REQUEST_PLAYER_CARDS')

            message = json.loads(text_data)     # converts the data to Python
            # print('**', message)

            cards = await get_player_cards(message['matchID'], message['gameID'], message['leg'], message['position'], message['troef'])

            # Only send the the client (not to the group)
            message = {
                'type'      : 'send_player_cards',
                'cards'     : cards
            }
            await self.send(text_data=json.dumps(message))
            # print('Cards send : ', self.channel_name)


        #####################################################################################################
        #### When a player plays a card, this card needs to be communicated to the other players
        #### Django will also update who is next to play and the count on how many cards have been played in this round
        elif message['type'] == 'play_card':
            message = json.loads(text_data)     # converts the data to Python
            # print('@@@ PLAY_CARD')
            # print('Card played by :', message['position'], message['color'], message['rank'])

            # set the next player to throw a card
            message['next_to_play'] = ( message['next_to_play'] + 1 ) % 4 
            message['count_cards_played'] = ( message['count_cards_played'] + 1 )

            # Send message to room group
            await self.channel_layer.group_send(
                self.group_name, 
                {
                    'type': 'send_to_group',        ## Based on this name a function to handle is created
                    'message': message
                }
            )
        #####################################################################################################
        #### TYPE: check_round
        #### the played round is send from player with my_position = 0 to the websocket.
        #### The following needs to be done
        ####  - check who won the round and send this to the group
        #### receive : 'gameID', 'leg', 'round', 'cards', 'troef'
        elif message['type'] == 'check_round':
            message = json.loads(text_data)     # converts the data to Python
            print('@@@ CHECK_ROUND')
            # print(message)

            # FIRST: get the game information
            # We need the info from some fields 
            game = await get_game(message['gameID'])

            # NEXT:  determine the troef played
            troef_choices = ['clubs', 'hearts', 'spades', 'diamonds']
            troef = troef_choices[message['troef']]

            # NEXT: Determine which position started this round.
            # if the round = 0 then determine based on current leg
            # if round > 0 then look at the winner of the previous round
            if message['round'] == 0:
                position_start = (game.legs_completed ) % 4
                # print('Position that started this round: ', position_start)
            else:
                # Get the winner of the previous round (slag)
                slag = await get_slag(message['gameID'], message['leg'], message['round']-1  )
                position_start = slag.player_won
                

            # Determine which player and team won the round
            print('AAAAA',troef, position_start,message['cards'])
            winner = evaluateSlag(message['cards'], troef, position_start)

            message = {
                'type'          : 'winner_round',
                'winner'        : winner
            }

            # Send message to room group
            await self.channel_layer.group_send(
                self.group_name, 
                {
                    'type': 'send_to_group',        ## Based on this name a function to handle is created
                    'message': message
                }
            )


        #####################################################################################################
        #### TYPE: log_round
        #### the played round is send from player with my_position = 0 to the websocket.
        #### Or verzaakt is reported by a player.
        ####
        #### The following needs to be done
        ####  - store the result of this round in the database
        ####  - Update this game with the correct leg and round numbers
        ####
        #### A variable is used to incidate that the game has ended
        ####
        #### when a slag already exists, then first remove it and then log the new slag
        ###
        ### This procedure needs to determine whether or not a new round needs to be played
        ### There are tree possibilies
        ###  - Play new round
        ###  - Signal end of leg
        ###  - Signal the end of game
        #### 
        #### receive : 'gameID', 'leg', 'round', 'cards', 'troef', 'roem'
        elif message['type'] == 'log_round':
            message = json.loads(text_data)     # converts the data to Python
            print('@@@ LOG_ROUND')
            print('***', message)
            await self.process_log_round(message)
           
                
        #####################################################################################################
        #### TYPE: request_scores
        #### For a game get all the leg scores and total score for the game
        elif message['type'] == 'request_scores':
            message = json.loads(text_data)     # converts the data to Python
            print('@@@ REQUEST SCORES')
            # print(message)

            scores_per_leg , totalscores = await get_current_scores(message['gameID'])

            ### Create the message based on state
            message = {
                'type'                  : 'send_scores',
                'scores_per_leg'        : scores_per_leg,
                'totalscores'           : totalscores
            }

            # Only send the the client that did this request(not to the group)
            await self.send(text_data=json.dumps(message))

            # # Send message to room group
            # await self.channel_layer.group_send(
            #     self.group_name, 
            #     {
            #         'type': 'send_to_group',        ## Based on this name a function to handle is created
            #         'message': message
            #     }
            # )

        #####################################################################################################
        else:
            # Types that do not need to be processed can directly be forwarded to the group
            # like status updates
            # Send message to room group
            print('@@@@ Other messages')
            await self.channel_layer.group_send(
                self.group_name, 
                {
                    'type': 'send_to_group',        ## Based on this name a function to handle is created
                    'message': message
                }
            )




    # GROUP RECEIVE message from room group to forward your client
    async def send_to_group(self, event):
        # event is the object that contains the complete message that was send
        # This includes the type that refers to this function
        # send only this 
        message = event['message']
        # print('@@@ SEND_TO_GROUP')

        # print('channel_name*: ', self.channel_name, self.group_name)

        # Send message to WebSocket to client
        await self.send(text_data=json.dumps(message))


    async def connected_update(self, message):
        '''
        register a player as connected and send all connection statusses of that game to all players
        '''
                    
        # Update the status in the table
        await set_connected_status(message['gameID'], message['position'], message['channel'])

        # Get all connected players of that game
        connected_positions = await get_connected_status_of_players(message['gameID'])

        # send this info to all players in the group.
        message = {
            'type'      : 'statusUpdate',
            'status'    : connected_positions
        }
        # message = json.dumps(message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name, 
            {
                'type': 'send_to_group',        ## Based on this name a function to handle is created
                'message': message
            }
        )

        # print('CONNECTION_UPDATE')


    async def notify_verzaken(self, message):
        '''
        Notify to all players that a player has started the verzaken procedure
        '''

        # send this info to all players in the group.
        message = {
            'type'          : 'activate_verzaken',
            'player_name'   :  message['player_name']
        }

        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name, 
            {
                'type': 'send_to_group',        ## Based on this name a function to handle is created
                'message': message
            }
        )


    # async def process_verzaken(self, message):
    #     '''
    #     Once the team is selected that should receice all points 
    #     this must be processed into the database 
    #     Further the current Round must be closed.
    #     '''

    #     print('Team that gets all points: ', message['team'])


    async def process_log_round(self, message):
        print('*****', message)
        # Cover also the case 'verzaakt'

        #First delete any slag for the same game/leg/round, if it exists
        await delete_slag(message['gameID'], message['leg'], message['round'])

        # NEXT: get the game information
        # We need the info from some fields and at the end some game fields needs to be updated
        game = await get_game(message['gameID'])

        ### If this is the first round of the first leg then
        ### - set the startdate of this game
        ### - register the troef of this leg. this will  be registered in the slag of the first round / leg
        ###   This is automatically done on saving the first leg

        if (message['leg'] == 0) and (message['round']) == 0:
            # Set the date_game_start and save the game
            game.date_game_start = datetime.now()
            game.gameStatus_id = await get_gameStatus('wordt gespeeld')
            await save_game(game)

        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        if message['verzaakt'] == False:
            ### Handle the regular processing of a leg

            # NEXT:  determine the troef played
            troef_choices = ['clubs', 'hearts', 'spades', 'diamonds']
            troef = troef_choices[message['troef']]

            # NEXT: Determine which position started this round.
            # if the round = 0 then determine based on current leg
            # if round > 0 then look at the winner of the previous round
            if message['round'] == 0:
                position_start = (game.legs_completed ) % 4
                # print('Position that started this round: ', position_start)
            else:
                # Get the winner of the previous round (slag)
                slag = await get_slag(message['gameID'], message['leg'], message['round']-1  )
                position_start = slag.player_won
                

            # Determine which player and team won the round
            # team A =  players 0/2    B= players 1/3
            print('BBBB', message['cards'], troef, position_start)
            winner = evaluateSlag(message['cards'], troef, position_start)
            print('winner: ', winner)
            if (winner == 0) or (winner == 2):
                teamA_won = True
            else:
                teamA_won = False

            # print('troef, winner : ', troef, winner)

            print('Team A won: ', teamA_won)

            # Determine the score.
            cards = message['cards']
            # print('cards : ', cards)
            score = countRound(cards, troef)

            # For last round add 10 mounts to score
            if message['round'] == 7:
                score = score + 10

            # print('Score: ', score)

            # get the roem
            roem = message['roem']

            # Later add validation on 'verzaakt.
            # !! NO, verzaakt will be related to a leg and not a single slag
            verzaakt = None

            troef_obj = await get_troef(troef)

            # Store the slag in the database
            slag = Slag()  
            slag.gameID             = game
            slag.leg                = message['leg']
            slag.n_slag             = message['round']
            slag.cards_slag         = json.dumps(cards)     # store as json item in a textfield
            slag.troef              = troef_obj
            slag.position_start     = position_start
            slag.player_won         = winner
            slag.teamA_won          = teamA_won
            slag.score              = score
            slag.roem               = roem
            verzaakt                = verzaakt

            # store in the database
            await save_slag(slag)

        else: 
            ## handle the verzaakt situation
            pass
            ## Set round to 7 so that leg will be closed
            ## and can be registered.
            message['round'] = 7
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    

        ### NEXT increase the rounds played in the game, or when the leg is completed 
        ### then increase the leg and set rounds to 0
        ### when the maximum number of legs have been realized then send signal potje completed

        # First get the match info to get the maximum number of legs
        match = await get_match(game.matchID_id)


        ## After registering the played round signal three possibilies
        ## 1) play next round
        ## 2) signal end of leg: communicate the result of the leg to be shown in the screen.
        ## 3) signal the end of game: show both the result of the latest leg and result of total game
        ##
        ## Use  'state'=  'next_round', 'end_of_leg', 'end_of_game'
        ##
        ## and update the round in the game parameters
        state = ''
        if message['round'] < 7:
            game.rounds_completed = game.rounds_completed + 1
            state = 'next_round'

        else:
            game.rounds_completed = 0
            # Update the legs_completed
            if message['leg'] < match.n_legs - 1:
                game.legs_completed = game.legs_completed + 1
                state = 'end_of_leg'
                print('LEG is COMPLETED')
            else: 
                # Game is finished
                state = 'end_of_game'
                game.legs_completed = game.legs_completed + 1
                game.date_game_end = datetime.now()
                game.gameStatus_id = await get_gameStatus('uitgespeeld')
                
                print('GAME is COMPLETED')

        await save_game(game)

    
        #### STATE : next_round
        if state == 'next_round':
            
            message_out = {
            'type'          : 'state_of_game',
            'state'         : state,
        # 'data_completed'        : datetime.now(),
            # 'player_aangenomen'     : player_aangenomen, 
            'scoreA'                : 0, 
            'roemA'                 : 0,
            'scoreB'                : 0,
            'roemB'                 : 0,
            # 'succeeded'             : succeeded, 
            # 'pit'                   : pit,
            # 'team'                  : team          # team A or team B
        }

        #### STATE : end_of_leg
        if state == 'end_of_leg' or state == 'end_of_game':
            ## Store the result of the leg: score, roem, who won, door/nat.
            ## and show it to the players

            leg = game.legs_completed - 1   # Note this was already increaed by 1

            if message['verzaakt'] == False:
                # Get the scores of the leg
                [player_aangenomen, succeeded, pit, team,  score_A, roem_A, score_B, roem_B] = await evaluate_leg(message['gameID'], leg)
                
                # register the leg using a serializer
                input_data={
                    'gameID'                : message['gameID'], 
                    'leg'                   : leg, 
                    'data_completed'        : datetime.now(),
                    'player_aangenomen'     : player_aangenomen, 
                    'scoreA'                : score_A, 
                    'roemA'                 : roem_A,
                    'scoreB'                : score_B,
                    'roemB'                 : roem_B,
                    'succeeded'             : succeeded, 
                    'pit'                   : pit
                    }

            else:
                # In case of verzaakt assign all 262 + all roem to the other party
                roem = await get_roem(message['gameID'], leg)
                print('---- ',roem)
                totRoem = roem[0]['roem__sum'] + roem[1]['roem__sum']
                print('---- ',totRoem)
                succeeded = False
                pit = False

                player_aangenomen = leg % 4  # In the game variant 'verplicht aannemen'

                if message['team_get_points'] == 'A':
                    #Get all reported roem of this leg
                    score_A     = 162
                    roem_A      = totRoem + 100
                    score_B     = 0
                    roem_B      = 0
                    team = 'team A'

                else: 
                    score_B     = 162
                    roem_B      = totRoem + 100
                    score_A     = 0
                    roem_A      = 0
                    team = 'team B'

                # register the leg using a serializer
                input_data={
                    'gameID'                : message['gameID'], 
                    'leg'                   : leg, 
                    'data_completed'        : datetime.now(),
                    'player_aangenomen'     : player_aangenomen, 
                    'scoreA'                : score_A, 
                    'roemA'                 : roem_A,
                    'scoreB'                : score_B,
                    'roemB'                 : roem_B,
                    'succeeded'             : succeeded, 
                    'pit'                   : pit
                    }


            #First delete any leg for the same game , if it exists.
            await delete_leg(message['gameID'], message['leg'])

            # save the Leg to the database
            await save_leg(input_data)

            ### Create the message based on state
            message_out = {
                'type'                  : 'state_of_game',
                'state'                 : state,
                # 'data_completed'        : datetime.now(),
                'player_aangenomen'     : player_aangenomen, 
                'scoreA'                : score_A, 
                'roemA'                 : roem_A,
                'scoreB'                : score_B,
                'roemB'                 : roem_B,
                'succeeded'             : succeeded, 
                'pit'                   : pit,
                'team'                  : team          # team A or team B
            }



        #### STATE : end_of_game
        #### change the game status to 'uitgespeeld' set the date of game end
        if state == 'end_of_game':

            print('State: end of game')

            message_out = {
                'type'                  : 'state_of_game',
                'state'                 : state,
                # 'data_completed'        : datetime.now(),
                'player_aangenomen'     : player_aangenomen, 
                'scoreA'                : score_A, 
                'roemA'                 : roem_A,
                'scoreB'                : score_B,
                'roemB'                 : roem_B,
                'succeeded'             : succeeded, 
                'pit'                   : pit,
                'team'                  : team          # team A or team B
            }


            # Update the score to the game
            scores_per_leg , totalscores = await get_current_scores(message['gameID'])

            game.scoreA                = totalscores[0] 
            game.roemA                 = totalscores[1]                 
            game.scoreB                = totalscores[2] 
            game.roemB                 = totalscores[3]

            await save_game(game)

            # new_date = datetime.now()

            # print('****', message['gameID'])
            

            # scores_per_leg , totalscores = await get_current_scores(message['gameID'])
            # print('****', totalscores)
            
            # #define the game data to be updated
            # game_data = {
            #     'gameID'                : message['gameID'],
            #     'date_game_end'         : datetime.now(),
            #     'gameStatus'            : 'uitgespeeld',
            #     'scoreA'                : totalscores[0], 
            #     'roemA'                 : totalscores[1],                 
            #     'scoreB'                : totalscores[2], 
            #     'roemB'                 : totalscores[3], 
            # }

            # await update_game(game_data)


        # Send message to room group
        await self.channel_layer.group_send(
            self.group_name, 
            {
                'type': 'send_to_group',        ## Based on this name a function to handle is created
                'message': message_out
            }
        )

  

    









##### Synchronous version
# # chat/consumers.py
# import json
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer

# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.group_name = 'chat_%s' % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.group_name,
#             self.channel_name
#         )

#         print('DUMMY1')

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))