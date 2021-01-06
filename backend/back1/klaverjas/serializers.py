# klaverjas/serializers.py


from django.core import exceptions
from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password

from my_auth.models import User

from klaverjas.klaverjas_lib import klaverjas

from klaverjas.models import Match, Game, GamePlayer, Leg, Slag, Remark


class UserSerializer(serializers.ModelSerializer):
    '''
    Define this serializer to reduce the number of User fields to be 
    shown in other serializers with depth > 0
    '''

    class Meta:
        model = User
        fields = [
            'id', 
            'username'
        ]
        ## Or use exclude. like
        # exclude = (
        #     'password', 'last_login', 'is_superuser', 'email',
        #     'first_name', 'last_name',
        #     'is_active', 'date_joined',
        #     'is_staff', 'groups', 'user_permissions', 
        # )

class MatchSerializer(serializers.ModelSerializer):
    '''
    Define this serializer to show a game.
    This serializer can be used in joined queries, to only show the user id and name
    '''

    owner = UserSerializer()

    class Meta:
        model = Match
        exclude = (
            'cards', 
        )

class GameSerializer(serializers.ModelSerializer):
    '''
    Define this serializer to show a game
    This serializer can be used in joined queries, to define what to show of a game.
    This is needed when as part of the game the match-owner only needs to show id and name
    '''

    matchID = MatchSerializer()

    class Meta:
        model = Game
        fields = '__all__' 


class GameCreateSerializer(serializers.ModelSerializer):
    '''
    To create games
    '''
    class Meta:
        model = Game
        fields = '__all__' 


class LegSerializer(serializers.ModelSerializer):
    '''
    To serialize a leg
    '''
    class Meta:
        model = Leg
        fields = '__all__' 

class SlagSerializer(serializers.ModelSerializer):
    '''
    To serialize a slag
    '''
    class Meta:
        model = Slag
        fields = '__all__' 


class MatchCreateSerializer(serializers.ModelSerializer):
    '''
    Serializer to be used when creating new matches.
    parameters are validated
    Note: owner and cards are created in the view using perform_create 
    '''
    
    class Meta:
        model = Match
        fields = [
            'matchID',
            #'owner',           #Determine user based on request
            'description',
            'n_legs',
            #'date_created',    # this will be autofilled by the model
            #'cards',             #this will be calculated
            'date_match_start',
            'date_match_stop',
            'date_register_stop'
        ]

    # Validate matchID
    # the model will validate that matchID is unique, so no additional validation needs to be added
    # Also defining this here will not function, because first the validation by the model
    # itself is done, so that the validation here will be get invoked.

    def validate_description(self, value):
        """
        Validate that description length is less or equals than 500
        """
        length = len(value)
        
        if length > 500:
            raise serializers.ValidationError('De omschrijving moet minder dan 500 karakters bevatten')

        return value


    def validate_n_legs(self, value):
        """
        Validate that n_legs is greater than 0 and less than 100
        """
        
        if value < 1 or value > 100:
            raise serializers.ValidationError('het aantal rondes per potje moet liggen tussen [1,2,...100]')

        return value


    def validate_date_match_stop(self, value):
        '''
        Validate that Match stop date is after Match start date
        '''

        match_start = self.initial_data['date_match_start']
        match_stop  =  self.initial_data['date_match_stop']
        # print(match_stop <= match_start)
        if match_stop <= match_start:
            raise serializers.ValidationError('De wedstrijd stop datum moet later zijn dan de start datum')

        return value


    def validate_date_register_stop(self, value):
        '''
        Validate that registration stop date is before the Match stop date
        '''

        register_stop  = self.initial_data['date_register_stop']
        match_stop  =  self.initial_data['date_match_stop']

        if match_stop <= register_stop: 
            raise serializers.ValidationError('De stop datum voor registratie moet eerder zijn dan de stop datum wedstrijd')

        return value


class MatchListSerializer(serializers.ModelSerializer):
    '''
    List the matches
    Do not show the cards
    '''

    owner = UserSerializer()        # only show a reduced set of fields

    class Meta:
        model = Match
        fields = [
            'matchID',
            'owner',            # Determine user based on request
            'description',
            'n_legs',
            'date_created',     # this will be autofilled by the model
            # 'cards'           #this will be calculated
            'date_match_start',
            'date_match_stop',
            'date_register_stop',
            'status_color',         # note : @property fields are not auto included in fields = '__all__'
        ]

        depth = 1    # Specify how deep the (left)joined data must be included (nested serialization)

        
class MatchRetreiveUpdateSerializer(serializers.ModelSerializer):
    '''
    Only to Retreive (show) the details of the matches
    '''

    class Meta:
        model = Match
        # fields = '__all__'      # do not need status_color
        # fields = [
        #     'id', 
        #     'username'
        # ]
        
        ## Exclude the cards to be shown or updated
        exclude = (
            'cards', 
        )

        read_only_fields = [
            'matchID',
            'owner',            # Determine user based on request
            #'description',
            #'n_legs',
            'date_created',     # this will be autofilled by the model
            'cards'           #this will be calculated
            #'date_match_start',
            #'date_match_stop',
            #'date_register_stop',
        ]

        depth = 1   

    ## !! Use the same validation as used for create.

    def validate_description(self, value):
        """
        Validate that description length is less or equals than 500
        """
        length = len(value)
        print('****', value)
        
        if length > 500:
            raise serializers.ValidationError('De omschrijving moet minder dan 500 karakters bevatten')

        return value


    def validate_n_legs(self, value):
        """
        Validate that n_legs is greater than 0 and less than 100
        And validate that within the match no round (slag) has been registered
        """ 

        # data = self.initial_data
        matchID = self.instance.matchID
        # print('****', value, self.instance.matchID)
        
        if value < 1 or value > 100:
            raise serializers.ValidationError('het aantal rondes per potje moet liggen tussen [1,2,...100]')

        # Check that value of n_legs is changed
        qs = Match.objects.get(matchID=matchID)
        if value == qs.n_legs:
            changed = False
        else:
            changed = True

        # Determine that there are no rounds played in this match
        # Changing n_legs is not allowed
        qs = Slag.objects.filter(gameID__matchID__matchID=matchID)
        # print(len(qs))


        if len(qs) != 0 and changed:
            raise serializers.ValidationError('Kan niet aangepast worden als een potje al is gestart')

        return value


    def validate_date_match_stop(self, value):
        '''
        Validate that Match stop date is after Match start date
        '''

        match_start = self.initial_data['date_match_start']
        match_stop  =  self.initial_data['date_match_stop']
        # print(match_stop <= match_start)
        if match_stop <= match_start:
            raise serializers.ValidationError('De wedstrijd stop datum moet later zijn dan de start datum')

        return value


    def validate_date_register_stop(self, value):
        '''
        Validate that registration stop date is before the Match stop date
        '''

        register_stop  = self.initial_data['date_register_stop']
        match_stop  =  self.initial_data['date_match_stop']

        if match_stop <= register_stop: 
            raise serializers.ValidationError('De stop datum voor registratie moet eerder zijn dan de stop datum wedstrijd')

        return value


class PlayerListSerializer(serializers.ModelSerializer):
    '''
    Of all matches, show the games and players
    '''

    player = UserSerializer()        # only show a reduced set of fields
    gameID = GameSerializer()
    # owner = UserSerializer()        # only show a reduced set of fields

    class Meta:
        model = GamePlayer
        fields = '__all__'  

        # Do not need depth, because the join is defined by the serialiser.
        # depth = 1    # Specify how deep the (left)joined data must be included (nested serialization)


class Game2MatchSerializer(serializers.ModelSerializer):
    '''
    For a game show all related matches
    '''

    matchID = MatchSerializer()
    # date_game_start = serializers.DateTimeField(format="%Y-%m-%d, %H:%M:%S")
    # date_game_end   = serializers.DateTimeField(format="%Y-%m-%d, %H:%M:%S")
    date_game_start = serializers.DateTimeField(format="%d-%m-%Y om %H:%M:%S")
    date_game_end   = serializers.DateTimeField(format="%d-%m-%Y om %H:%M:%S")


    class Meta:
        model = Game
        fields = '__all__'  

class PlayerSerializer(serializers.ModelSerializer):
    '''
    Create a player linked to a game
    ?? validate that request.user is the player
    '''
    
    class Meta:
        model = GamePlayer
        fields = '__all__'  

        # depth = 1    # Specify how deep the (left)joined data must be included (nested serialization)


class RemarkSerializer(serializers.ModelSerializer):
    '''
    Define this serializer to show remarks.
    '''

    class Meta:
        model = Remark
        fields = '__all__'  


class RemarkListSerializer(serializers.ModelSerializer):
    '''
    Define this serializer to show remarks.
    '''

    user = UserSerializer()
    date_created = serializers.DateTimeField(format="%Y-%m-%d, %H:%M:%S")

    class Meta:
        model = Remark
        fields = '__all__'  
        depth = 1








    #####################################################################################################
    ## Other methods
    # Do not use these because the contain themselves same functions that you do not want to overwrite.
    # def create(self, validated_data):
    # def update(self, instance, validated_data):
    # def save(self):


    # def save(self):
    #     # save does some general checks. When the item is new then call create else calls update
    #     # https://stackoverflow.com/questions/45100515/what-is-the-different-between-save-create-and-update-in-django-rest-fram
    #     # Define what needs to be saved
    #     # use  validated_data as the input from the API
    #     print(self.validated_data)


    #     #Create the card for all legs in a match/game
    #     cards = klaverjas.CreateMatchDecks(self.validated_data['n_legs'])

    #     # print(self.context['request'].data['date_match_start'])
    #     # print('****',self.validated_data['date_match_start'])

    #     # Determine the user that created this match
    #     user = self.context['request'].user

    #     # Create a Match with the variables from validated data
    #     match = Match(
    #         matchID             = self.validated_data['matchID'],
    #         owner               = user, #self.validated_data['owner'],
    #         description         = self.validated_data['description'],
    #         n_legs               = self.validated_data['n_legs'],
    #         cards               = cards,
    #         date_match_start    = self.validated_data['date_match_start'],
    #         date_match_stop     = self.validated_data['date_match_stop'],
    #         date_register_stop  = self.validated_data['date_register_stop'],
    #         # status_color        = self.validated_data['status_color'],
    #     )

    #     # Start Validations
    #     errors = dict()     # collect the remarkt when validation is not okay

    #     print(self.validated_data)

    #     # *** Validate that n_legs is greater than 0 and less than 100
    #     N = self.validated_data['n_legs']
    #     if N < 1 or N > 100:
    #         errors['n_legs'] = ['the number of legs must be greater than 0 and less then 101']
            
    #     # *** Validate that Match start start date is before Match stop date
    #     match_start = self.validated_data['date_match_start']
    #     match_stop  = self.validated_data['date_match_stop']
    #     if match_stop <= match_start:
    #         errors['date_match_stop'] = ['The stop date should be after the start date of the match']

    #     # *** validate that stop register date is before stop of the match
    #     register_stop  = self.validated_data['date_register_stop']
    #     if match_stop <= register_stop: 
    #         errors['date_register_stop'] = ['The registration should stop before the end of the match']

        
    #     # When there a re any errors then create a Validation error.
    #     # Only when there a no error then create the Match
    #     if errors:
    #         raise serializers.ValidationError(errors)
    #     else:
    #         match.save()