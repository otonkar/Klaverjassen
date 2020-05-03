#klaverjas/klaverjas_lib/klaverjas.py

#######################################################################################
##
## This is a module to support the klaverjas functions.
## It contains the following functions/classes
##
##  - createPlayingCards()              ; to create a card desk of 32 klaverjas playing cards 
##  - CreateMatchDecks(n_Legs)          ; to create n_Legs sets of playing cards divided over 4 players
##  - sortCards(cards, troef)           ; sorts a set of cards, taking into account the troef color
##  - countRound(cards, troef)          ; counts the points of the cards for a single playing round  (4 cards) 
##  - evaluateSlag(cards, troef, start) ; Determines which player has won the round (slag)
##  - validateCard(roundCards, handCards, troef) ; 
##
#######################################################################################

import random
from itertools import product

def createPlayingCards(): 
    '''
    This function creates a desk of ordered playing cards (32 cards).

        Use as:   cards = createPlayingCards()

        OUTPUT: a list of dictionaries

    A card is a dictionary like {'color': 'hearts, 'rank': queen}
    '''
    
    # define the 32 playing cards
    colors = ('hearts', 'spades', 'diamonds', 'clubs')
    ranks  = ('seven', 'eight',
              'nine', 'ten', 'jack', 'queen', 'king', 'ace')

    cards = list()

    # id = 0
    for color in colors:
        for rank in ranks:
            # card = dict()
            card = {
                # 'id': id,
                'color': color,
                'rank': rank
            }
            cards.append(card)
            # id = id + 1

    return cards


def CreateMatchDecks(n_Legs):
    ''' 
    Create a list of klaverjas playing cards, already shuffled and dealed for a complete match.
    This set of cards can be used within a game to play.
    Within a match multiple games will be played with different pairs of players.
    All games will use the same shuffled set of cards to play to be able the compair the results.

    Every game consists of n_Legs legs to be played.
    In a leg each player will receive 8 cards.
    These cards will then be played in 8 rounds, where every player plays 1 card.

    For a play the deck needs to be shuffled and devided over 4 persons (8 cards each)
    There are n_Legs number of legs to deal for (normally 16)

        Use as:     match = CreateMatchDecks(n_Legs)

        INPUT:      
            n_Legs, the number of legs to play in each game

        OUTPUT:     
            a list containing the shuffled playing cards divided over the 4 players
            matchcards[4][2] contains
                - for leg number 4 (fifth leg)
                - the cards for player 2 (third player)

            a card is a dictionary like: {'color': 'hearts, 'rank': queen}

    '''

    # store the shuffled decks complete match
    match = list()

    # loop over the spellen 
    for i in range(0, n_Legs,1):
        spel = list()
        # Create the deck in the loop otherwise only the last deck
        # will be added to all items in the list

        # Create a new deck
        deck = createPlayingCards()
        # Shuffle the deck
        random.shuffle(deck)
        # Divide the cards over 4 persons
        spel.append(deck[0:8])
        spel.append(deck[8:16])
        spel.append(deck[16:24])
        spel.append(deck[24:32])


        # Add the card dealt for a complete round to the match
        match.append(spel)

    return match


def sortCards(cards, troef):
    '''
    Sort the klaverjas playing 'cards' from highest to lowest value per color 
    in case one color is 'troef'.

    This function sorts cards as follows
     - per color (type)
     - for each color per value, taking into account the different
       values for troef and non-troef cards

    Cards is a list of dictionaries containing a color and a rank.
    ( {"color": 'hearts, "rank": 'ace}, {...}, {...} )

    colors are: hearts, spades, diamonds, clubs.
    ranks are: seven, eight, nine, 10, jack, queen, king, ace

        Use as: cards_sorted = sortCards(cards, troef)

        INPUT  
            troef        = the 'color' that is troef
            cards        = a set of cards to be sorted

        OUTPUT 
            cards_sorted = a set of sorted cards
    '''

    # Define the values of the cards voor klaverjassen
    value_notroef = { 'seven':1, 'eight':2,'nine':3, 'jack':4,
                    'queen':5, 'king':6, 'ten':7, 'ace':8,}

    value_troef = { 'seven':51, 'eight':52, 'queen':53, 'king':54, 
                    'ten':55, 'ace':56, 'nine':57, 'jack':58}

    colors = ('hearts', 'spades', 'diamonds', 'clubs')


    cards_sorted = list()

    # define dynamically created lists for the different colors
    # this created lists named hearts, clubs,...
    for color in colors: 
        globals()[color] = list()

    # Collect the different colors in the named lists
    for card in cards: 

        # Get the card value based on troef/notroef
        if card["color"] == troef:
            card_value = value_troef[card["rank"]]
        else:
            card_value = value_notroef[card["rank"]]

        # print('----', card_value)

        # Collect the colors in different lists
        for color in colors:
            if card["color"] == color:
                globals()[color].append(card_value)

    # print(globals()['hearts'])
    # print(hearts)

    # Sort the named lists (per color) based on values
    for color in colors:
        globals()[color].sort(reverse=True)

    # Convert the values back to the cards
    for color in colors:
        if color == troef:
            values = value_troef
        else:
            values = value_notroef

        for item in globals()[color]:

            for key, value in values.items(): 
                if value == item:
                    card = { "color": color, "rank": key }
                    cards_sorted.append(card)

    return cards_sorted


def countRound(cards, troef):
    '''
    Given a set of cards and a troef color, calculate the points for klaverjassen.
    A Round (slag) contains a set of 4 cards.

        Use as:     total_count = countRound(cards, troef)

        INPUT:      
            cards, a list of 4 dictionaries representing cards
            troef, the 'color' that is troef

        OUTPUT:     
            total_count, the amount of points for this klaverjas round (slag)
            Note: only the card points are counted, exclusing last round and bonus (roem)

    The cards must be a list of 4 dictionaries
    '''

     # Define the values for counting cards for klaverjassen
    value_notroef = { 'seven':0, 'eight':0,'nine':0, 'jack':2,
                    'queen':3, 'king':4, 'ten':10, 'ace':11,}

    value_troef = { 'seven':0, 'eight':0, 'queen':3, 'king':4, 
                    'ten':10, 'ace':11, 'nine':14, 'jack':20}   

    # Check that cards is a complete slag of 4 cards 
    N_cards = 4
    if N_cards != len(cards):
        print('Error, slag does not contain 4 cards')
        return -10000

    total_count = 0
    for card in cards:
        if card["color"] == troef:
            total_count = total_count + value_troef[card["rank"]]
        else:
            total_count = total_count + value_notroef[card["rank"]]

    return total_count


def evaluateSlag(cards, troef, start):
    '''
    Given a set of 4 cards in a round,  and a troef color, 
    this function determines which player has won the slag

        Use as:     player = evaluateSlag(cards, troef, start)

        INPUT
            cards: list of 4 cards (dictionaries with color,rank) played in a round
            troef: a single color (like hearts, spades, diamonds, clubs)
            start: number indicating which player started this slag (0,1,2 or 3)

        OUTPUT
            number: represents which person won the slag (0,1,2,3)

    General rules for counting:
     - troef is always higher than a non-troef
     - a color has no value when this color is non-troef and is not the same as the color that started the slag
    '''

    # Define the values of the cards voor klaverjassen
    value_notroef = { 'seven':1, 'eight':2,'nine':3, 'jack':4,
                    'queen':5, 'king':6, 'ten':7, 'ace':8,}

    value_troef = { 'seven':51, 'eight':52, 'queen':53, 'king':54, 
                    'ten':55, 'ace':56, 'nine':57, 'jack':58}

    colors = ('hearts', 'spades', 'diamonds', 'clubs')

    # Check that cards is a complete slag of 4 cards 
    N_cards = 4
    if N_cards != len(cards):
        print('Error, slag does not contain 4 cards')
        return -10000

    # Rotate the cards list so that the player that started the slag is in position 0
    # print(cards)
    cards = cards[start:] + cards[:start]
    # print(cards)

    score = 0
    winner = 0
    initial_color = cards[0]["color"]
    for card in cards:
        if card["color"] == troef:
            if value_troef[card["rank"]] > score:
                score = value_troef[card["rank"]]
                winner = cards.index(card)
        else:
            if card["color"] == initial_color:
                if value_notroef[card["rank"]] > score:
                    score = value_notroef[card["rank"]]
                    winner = cards.index(card)

    # the index of the winner must be set back to the orignal cards order. 
    # For this add the winner and the original shift and do modulo 4

    return (winner + start) % 4


def validateCard(roundCards, handCards, troef):
    '''
    This function validates which remaining cards from a player (handCards)
    are allowed to be played, given the fact that none or multiple cards are
    already played on the table (in de slag als roundCards

    The ruling is
        * On first card to be played in the slag are no restrictions
        * Also on last card to play are no restriction
        * player must use the same color as the initial card played

        - moet zelfde kleur meegooien
        - andere introeven en overtroeven als dat kan
        - anders mag iedere andere kleur worden gespeeld

        handCards is the current hand that includes the newCard to be played

        output list of cards that are valid to play
    '''


    # Define the values of the cards voor klaverjassen
    value_notroef = { 'seven':1, 'eight':2,'nine':3, 'jack':4,
                    'queen':5, 'king':6, 'ten':7, 'ace':8,}

    value_troef = { 'seven':51, 'eight':52, 'queen':53, 'king':54, 
                    'ten':55, 'ace':56, 'nine':57, 'jack':58}

    colors = ('hearts', 'spades', 'diamonds', 'clubs')

    # First Determine the color of the first card played
    initial_color = 'not played yet'
    if len(roundCards) != 0:
        initial_color = roundCards[0]["color"]

    # Next determine that the hand contains any color similar as initial_color
    initial_color_in_hand = False
    for card in handCards:
        if card["color"] == initial_color:
            initial_color_in_hand = True

    # Next determine if there are any troef cards played in the slag.
    # And determine the highest value of the troefcard in the slag
    troef_played = False
    troef_values = [0]      # fill with inital value, because max(.) will fail on empy list
    for card in roundCards:
        if card["color"] == troef:
           troef_values.append( value_troef[card["rank"]] )
           troef_played = True

    highest_value_troef_in_slag = max(troef_values)

    # Next dertermine that the hand has troef cards that are higher than the highest value of troef in slag
    troef_values = [0]  # fill with inital value, because max(.) will fail on empy list
    troef_present = False
    for card in handCards:
        if card["color"] == troef:
            troef_values.append( value_troef[card["rank"]] )
            troef_present = True

    # Overtroeven is mandatory (true) when the hand has a higher troef card than troef in current slag
    overtroeven = max(troef_values) > highest_value_troef_in_slag

    
    # Now determine which cards in the hand are allowed to play
    correctCards = list()
    if len(roundCards) == 0:
        # The person that has to throw the first card is allowed to choose any card from the hand
        correctCards = handCards
        # print('DUMMY1')
    else:
        if len(handCards) == 1:
            # In the last slag you must play the last card
            correctCards = handCards
            # print('DUMMY2')
        else: 
            # In case one or more cards are already in the slag
            # evaluate every card in the hand
            for card in handCards:

                if card["color"] == initial_color:
                    # All cards in hand with the same initial color are allowed
                    correctCards.append(card)
                    # print('DUMMY3')
                
                else: 
                    if initial_color_in_hand == False:
                        # when you do not have the same color in hand then
                        # check that there are troef cards in the hand.
                        # If there is troef in hand 
                        if card["color"] == troef:
                            if troef_played == False:
                                # When no troef is in slag then any troef from hand is allowed
                                correctCards.append(card)
                                # print('DUMMY4')
                            else: 
                                if overtroeven == True:
                                    # Als troef al gespeeld is dan moet je overtroeven
                                    if value_troef[card["rank"]] > highest_value_troef_in_slag:
                                        correctCards.append(card)
                                        # print('DUMMY5')
                                else:
                                    # overtroeven niet mogelijk
                                    correctCards.append(card)
                                    # print('DUMMY6')

                        else:
                            # Only allowed when there is no troef in the hand
                            if troef_present == False: 
                                correctCards.append(card)
                                # print('DUMMY7')

                    else: 
                        # no card allows if there is a some color as inital color.
                        pass

    return correctCards