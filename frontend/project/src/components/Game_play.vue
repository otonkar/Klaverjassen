<template>
    <div class="Appgameplay o_fullscreen">

        <div class="gameID">
          Game: {{ game.gameID}}
        </div>

        <div class="leg">
          Ronde: {{ current_leg + 1 }}
        </div>

        <b-button class="goback" @click="doGoBack()" size="sm">Ga terug</b-button>
        <!-- <b-button class="btn-primary reset_slag" variant="primary" @click="doStartRound(true)" size="sm">reset slag</b-button>
        <b-button class="btn-primary show_scores" variant="primary" @click="doGetScores()" size="sm">Stand</b-button>
        <b-button class="btn-primary show_slagen" variant="primary" @click="doShowSlagen()" size="sm">Slagen</b-button> -->

        <div class="action_menu">
          <b-dropdown variant="primary" text="acties" class="m-md-2">
            <b-dropdown-item @click="doStartRound(true)" >Reset Slag</b-dropdown-item>
            <b-dropdown-item @click="doGetScores()">Bekijk Score</b-dropdown-item>
            <b-dropdown-item @click="doShowSlagen()">Vorige slag</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item @click="show_melden_verzaken = !show_melden_verzaken" >Melden verzaken</b-dropdown-item>
          </b-dropdown>
        </div>

        <!-- Empty placeholders to put the card played -->
        <div v-bind:class="{'card-holder  play_p0': rotated_next_to_play !== 0, 'card-holder  play_p0 place_turn': rotated_next_to_play === 0 }"></div>
        <div v-bind:class="{'card-holder  play_p1': rotated_next_to_play !== 1, 'card-holder  play_p1 place_turn': rotated_next_to_play === 1 }"></div>
        <div v-bind:class="{'card-holder  play_p2': rotated_next_to_play !== 2, 'card-holder  play_p2 place_turn': rotated_next_to_play === 2 }"></div>
        <div v-bind:class="{'card-holder  play_p3': rotated_next_to_play !== 3, 'card-holder  play_p3 place_turn': rotated_next_to_play === 3 }"></div>

        <!-- Base place to start throwing cards for players 1,2,3 -->
        <div  class="card-holder  hand_p1  red_back "></div>
        <div class="card-holder  hand_p2  red_back "></div>
        <div class="card-holder  hand_p3  red_back "></div>

        <!-- Create empty places for the handcards -->
        <div class="card-holder hand_p0-0 "></div>
        <div class="card-holder hand_p0-1 "></div>
        <div class="card-holder hand_p0-2 "></div>
        <div class="card-holder hand_p0-3 "></div>
        <div class="card-holder hand_p0-4 "></div>
        <div class="card-holder hand_p0-5 "></div>
        <div class="card-holder hand_p0-6 "></div>
        <div class="card-holder hand_p0-7 "></div>

        <!-- Set the name tags include color who is next to play -->
        <div v-bind:class="[
            {nametag:true}, {tag_p0 :true}, 
            {text_active: false },
            {text_inactive: true }]"  
            > {{ rotated_players[0].player.username }} (Team {{ my_team }} / {{ (0 + my_position) % 4 + 1}})
        </div>

        <div v-bind:class="[
            {nametag:true}, {tag_p1 :true}, 
            {text_active: false },
            {text_inactive: true }]"  
            > {{ rotated_players[1].player.username }} 
        </div>

        <div v-bind:class="[
            {nametag:true}, {tag_p2 :true}, 
            {text_active: false },
            {text_inactive: true }]"  
            > {{ rotated_players[2].player.username }} 
        </div>

        <div v-bind:class="[
            {nametag:true}, {tag_p3 :true}, 
            {text_active: false },
            {text_inactive: true }]"  
            > {{ rotated_players[3].player.username }} 
        </div>


        <!-- show the connection status -->
        <div v-bind:class="{'dot_1 not-connected': !rotated_players[1].connected, 'dot_1 connected': rotated_players[1].connected }">  </div>
        <div v-bind:class="{'dot_2 not-connected': !rotated_players[2].connected, 'dot_2 connected': rotated_players[2].connected }"> </div>
        <div v-bind:class="{'dot_3 not-connected': !rotated_players[3].connected, 'dot_3 connected': rotated_players[3].connected }"> </div>

        <img v-if="troef_selected === 0" @click="doSelectTroef()" class="troef_place" src="../assets/Cards/clubs.png">
        <img v-if="troef_selected === 1" @click="doSelectTroef()" class="troef_place" src="../assets/Cards/hearts.png">
        <img v-if="troef_selected === 2" @click="doSelectTroef()" class="troef_place" src="../assets/Cards/spades.png">
        <img v-if="troef_selected === 3" @click="doSelectTroef()" class="troef_place" src="../assets/Cards/diamonds.png">

        <!-- Show the played card. 
        Do not choose 'index' as key, because we already are using a number as key in showing the hand cards. 
        This is avoid the message 'Duplicate keys detected' -->
        <div  v-for="(card, index) in play_class" 
              v-bind:key="card.position" 
              v-bind:class='play_class[index]'
        > </div>


        <!-- Show the hand cards and be able to click when 4 players are connected -->
        <div v-if="(count_connected === 4 && cards_loaded === true && next_to_play === my_position)">
          <div  v-for="(card, index) in cards" 
                v-bind:key="index" 
                v-bind:class='card_class[index]'
                @click="doPlayCard(index)"
          > </div> 
        </div>
        <div v-else>
          <div  v-for="(card, index) in cards" 
                v-bind:key="index" 
                v-bind:class='card_class[index]'
          > </div> 
        </div>
        
        <!-- Create a dropUp for roem -->
        <div v-bind="{hidden: !show_register_roem}" class="roem_select">
          <b-dropdown id="roem" size="sm" dropup v-bind:text="'selecteer roem (' + roem_value + ')'" variant="primary" class="m-2">
            <b-dropdown-item @click="roem_value = -200">-200</b-dropdown-item>
            <b-dropdown-item @click="roem_value = -100">-100</b-dropdown-item>
            <b-dropdown-item @click="roem_value = -70">-70</b-dropdown-item>
            <b-dropdown-item @click="roem_value = -50">-50</b-dropdown-item>
            <b-dropdown-item @click="roem_value = -40">-40</b-dropdown-item>
            <b-dropdown-item @click="roem_value = -20">-20</b-dropdown-item>
            <b-dropdown-item >--------</b-dropdown-item>
            <b-dropdown-item @click="roem_value = 200">200</b-dropdown-item>
            <b-dropdown-item @click="roem_value = 100">100</b-dropdown-item>
            <b-dropdown-item @click="roem_value = 70">70</b-dropdown-item>
            <b-dropdown-item @click="roem_value = 50">50</b-dropdown-item>
            <b-dropdown-item @click="roem_value = 40">40</b-dropdown-item>
            <b-dropdown-item @click="roem_value = 20">20</b-dropdown-item>
            <b-dropdown-item @click="roem_value = 0">0</b-dropdown-item>
          </b-dropdown>
        </div>

        <!-- button to take the slag  -->
        <b-button v-bind="{hidden: !show_take_round}" @click="doTakeRound()" class="take_round" variant="warning">Neem slag</b-button>

      <!-- Show the current roem in the leg -->
      <div class="roem">Roem </div>
      <div class="roem_teamA">team A: {{ total_roem[0]['roem__sum'] }}</div>
      <div class="roem_teamB">team B: {{ total_roem[1]['roem__sum'] }}</div>

      <!-- Show the result of a leg  -->
      <b-jumbotron class="jumbotron" v-bind="{hidden: !show_leg_result}">
        <h5>Resultaat ronde {{ current_leg + 1 }} </h5>
        <p>Aangenomen door: {{ state_data.team}},  {{ name_player_leg }} </p>
       <h5>Team A</h5>
        <p>score: {{ state_data.scoreA }}, roem: {{ state_data.roemA }}</p>
        <h5>Team B</h5>
        <p>score: {{ state_data.scoreB }}, roem: {{ state_data.roemB }}</p>
        <!-- <b-button variant="warning" @click="showCorrectRoem()">Corrigeer roem</b-button> -->
        <b-button variant="primary" @click="continueLegResult()">Ga verder</b-button>
        <!-- <p>Laat 1 speler de roem corrigeren als dat nodig is.</p> -->
      </b-jumbotron>

      <!-- Corrigeer roem -->
      <b-jumbotron class="jumbotron" v-bind="{hidden: !show_correct_roem}">
        <h5>Corrigeer roem ronde {{ current_leg + 1 }} </h5>
        <p>Team A huidige roem: {{ state_data.roemA }} <br>
          nieuwe roem: <input type="text" v-model="corrected_roemA">
        </p>
        <p>Team B huidige roem: {{ state_data.roemB }} <br>
          nieuwe roem: <input type="text" v-model="corrected_roemB">
        </p>
        <b-button variant="danger" @click="stopCorrectRoem()">Annuleer</b-button>
        <b-button variant="success" @click="doCorrectRoem()">Pas aan</b-button>
      </b-jumbotron>

      <!-- Show the result current score  -->
      <b-jumbotron class="jumbotron" v-bind="{hidden: !show_score_of_game}">
        <h5>Score game {{ game.gameID}} </h5>

        <div>
          <b-table-simple small responsive>
            
            <colgroup><col></colgroup>
            <colgroup><col><col></colgroup>
            <colgroup><col><col></colgroup>
            <b-thead>
              <b-tr>
                <b-th colspan="1" ></b-th>
                <b-th colspan="2" variant="">Team A</b-th>
                <b-th colspan="2">Team B</b-th>
              </b-tr>
              <b-tr>
                <b-th>Ronde</b-th>
                <b-th variant="">Score</b-th>
                <b-th variant="">Roem</b-th>
                <b-th>Score</b-th>
                <b-th>Roem</b-th>
              </b-tr>
            </b-thead>
            <b-tbody>
                <b-tr v-for="leg in leg_scores" v-bind:key="leg.leg">
                  <b-th> {{ leg.leg + 1  }} </b-th>
                  <b-th> {{ leg.scoreA }} </b-th>
                  <b-th> {{ leg.roemA }} </b-th>
                  <b-td> {{ leg.scoreB }} </b-td>
                  <b-td> {{ leg.roemB }} </b-td>
                </b-tr>
            </b-tbody>
            <b-tfoot>
              <b-tr>
                <b-th>Totaal</b-th>
                <b-th variant="success"> {{ total_scores[0] }} </b-th>
                <b-th variant="success"> {{ total_scores[1] }} </b-th>
                <b-td variant="success"> {{ total_scores[2] }} </b-td>
                <b-td variant="success"> {{ total_scores[3] }} </b-td>
                <!-- <b-td variant="success"> <img src="./clubs.png" width="17px"> A  </b-td> -->
              </b-tr>
            </b-tfoot>
          </b-table-simple>
        </div>

        <b-button variant="primary" @click="show_score_of_game = !show_score_of_game" >Sluiten</b-button>
      </b-jumbotron>


      <!-- Show Slagen  -->
      <b-jumbotron class="jumbotron slagen" v-bind="{hidden: !variables.show_slagen}">

        <keep-alive>
          <app-gamepreviousslag
              v-bind:gameID="game.gameID"
              v-bind:leg="current_leg"
              v-bind:round="current_round-1"
          ></app-gamepreviousslag>
        </keep-alive>

      </b-jumbotron>

      <!-- Show alert when pressed on troef when not allowed -->
      <div>
        <b-modal hide-footer v-model="modalShow">
          Troef mag alleen aangepast worden door de speler die aan de beurt is. 
          Ook als de ronde begonnen is mag de troef niet aangepast worden. <br>
          <b-button class="mt-3" block @click="doCloseTroefAlert()" variant="primary">Sluiten</b-button>
        </b-modal>
        
      </div>

      <!-- Show Melden Verzaken  -->
      <b-jumbotron class="jumbotron" v-bind="{hidden: !show_melden_verzaken}">
        <h5>Melden verzaken </h5>
        <p> Weet je zeker dat je verzaken wilt melden?</p>
        <p> 
          Als je doorgaat MOET worden gekozen naar welke partij alle punten, gemaakte roem + 100 roem extra gaat <br>
          Dit wordt definitief toegekend en kan niet meer gewijzigd worden.
        </p>
        <b-row>
            <b-col><b-button block @click="show_melden_verzaken = !show_melden_verzaken"  class="btn btn-danger"> Stoppen  </b-button></b-col>
            <b-col><b-button block v-on:click="doHandleVerzaken()"  class="btn btn-success"> Melden  </b-button></b-col>
        </b-row>
      </b-jumbotron>

      <!-- Show Afhandelen verzaken  -->
      <b-jumbotron class="jumbotron" v-bind="{hidden: !show_handle_verzaken}">
        <h5>Afhandelen verzaken </h5>
        <p> 
          Bepaal welk team ALLE punten krijgt.
        </p>
        <b-row>
            <b-col><b-button block @click="doShowSlagen()"  class="btn btn-info"> Bekijk slagen  </b-button></b-col>
        </b-row>
        <br>
        <p>
          Kies welk team krijgt: <br>
          162 punten + gespeelde roem + 100 roem
        </p>
        <br>

        <div>
          <b-form-group >
            <b-form-radio-group
              id="radio-slots"
              v-model="radio_selected_team"
            >
              <b-form-radio value="A" size="lg">Team A</b-form-radio>
              <b-form-radio value="B" size="lg">Team B</b-form-radio>
            </b-form-radio-group>
          </b-form-group>

        </div>
        <br>
        <hr> 
        <br>
        <b-row>
            <b-col><b-button block @click="doProcessVerzaken()"  class="btn btn-warning"> Kies definief Team {{ radio_selected_team }} </b-button></b-col>
        </b-row>

      </b-jumbotron>

      <!-- Show Activate Verzaken: reduced screen   -->
      <b-jumbotron class="jumbotron" v-bind="{hidden: !show_verzaken_activated}">
        <h5>Melding Verzaakt !!! </h5>
        <p> 
          Gemeld door: <strong>{{ player_notified_verzaken }}</strong>
        </p>
        <p>
          Bepaal met elkaar welk team (A of B) alle punten, gemaakte roem en 100 extra roem krijgt toegewezen.
        </p>
        <p>De melder ({{ player_notified_verzaken }}) moet de definieve keuze verwerken.</p>
        <b-row>
            <b-col><b-button block @click="doShowSlagen()"  class="btn btn-info"> Bekijk slagen  </b-button></b-col>
        </b-row>
        <br>
        <br>
        <b-row>
            <b-col><b-button block @click="show_verzaken_activated = !show_verzaken_activated"  class="btn btn-primary"> Sluiten </b-button></b-col>
        </b-row>

      </b-jumbotron>

    </div>
</template>


<script>
import ReconnectingWebSocket from 'reconnecting-websocket'
// import Appgameslagen from '../components/Games_slagen.vue'
import Appgamepreviousslag from '../components/Games_previous_slag.vue'

export default {
    name: 'Appgameplay',
    components: {
    'app-gamepreviousslag': Appgamepreviousslag
    },
    data () {
        return {
            modalShow: false,         // Show the modal to notifiy that player is not allowed to click on troef
            title: 'Game play page',
            show_new_leg: false,      // !! OUD To show the button for play new round
            show_new_round: false,    // To show a button to load a new round. (is also reset/replay current round)
            show_register_roem: false, // Show the button the register roem
            show_take_round: false,   // When the round is complete show the button to 'take' the slag
            show_leg_result: false,   // Show the leg result jumbotron when the leg is completed
            show_score_of_game: false, // Show the total score of all legs played in the game. Toggle using button
            show_close_game: false,   // When the game is played show a text to close the game
            show_correct_roem: false,  // Show the possibility to correct the roem at the end of the game
            show_melden_verzaken: false, // Show the option to report 'verzaken'
            show_handle_verzaken: false, // jumbotron to handle vezaken
            show_verzaken_activated: false,  // show to players a reduced verzaken screen
            player_notified_verzaken: '',  // Show the name of the player that notified verzaken
            verzaakt: false,          // To indicate that the leg was verzaakt
            radio_selected_team: 'A',        // Value used for the radio button to select which team should get all the pointe in case of verzaakt
            my_team: '',              // Contains A or B for the team of the rotated players at position 0 
            corrected_roemA: 0,       // New value for the total roem team A
            corrected_roemB: 0,
            name_player_leg: '',      // To show the name in the leg result of the player that played the leg
            roem_value: 0,            // The value of the roem that needs to be registered
            total_roem: [0,0],        // Store the total roem for the leg  as list [roem team A, roem team B]
            leg_scores: [],           // list that contains the info of all legs played in this game
            total_scores: [],         // Contains the current total score in this game [totalscoreA, totalroemA, totalscoreB, totalroemB]
            current_leg: 0,           // Store the current leg to be played. leg[0] is the first leg!!
            current_round: 0,         // Store the number of the current Slag, value = 0  is the first round
            next_to_play: 0,          // Original position of the player that needs to play the cards
            rotated_next_to_play: 0,  // The position on the screen that needs to play
            player_has_played: false, // Indicates that the player has played a card, so is not allowed to play again in this round
            data_received: '',
            state_data: '',           // Data object with info of the state of the game, like leg result details
            game: {},                 // receive from game details page. This contains game and match info.
            onPlay: '',               // Variable to incicate who is next to play a card.
            count_connected: 0,       // Counts the number of connected players. if == 4 then allowed to play
            cards_loaded: false,      // Set to true when playing cards have been downloaded
            my_position: '',          // the original player position of the player that is playing this screen.
            count_cards_played: 0,    // Count the number of cards that have been played in a round (slag)
            list_connected: [],       // A list of true/false indicating that a player in original position has been connected
            card_class: [],           // Store the classes of the cards in the hands of the player.
            play_class: [],           // store the classes of the cards in the played positions, except for player 0 position
            cards: [
                {'color': 'red', 'rank': 'back'},   // When player cards are not loaded, then show the back of the cards
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'}
            ],
            // cards_played: [],         // ?? REMOVE contains the integer numbers of the card played from the hand. Needed to revoke?
            cards_slag: ['--', '--', '--', '--'],     // Register the cards of the slag (with color and rank)
            // troef: [                                  // Not needed anymore
            //     'clubs.png',
            //     'hearts.png',
            //     'spades.png',
            //     'diamonds.png',
            // ],
            troef_selected: 0,       // Integer that represents the troef [0=clubs, 1=hearts, 2=spades, 3=diamonds]
            players: [ 
                {
                    position: '',
                    id: '',
                    player: { 
                        username: ''
                    },
                },
                {
                    position: '',
                    id: '',
                    player: { 
                        username: ''
                    },
                },
                {
                    position: '',
                    id: '',
                    player: { 
                        username: ''
                    },
                },
                {
                    position: '',
                    id: '',
                    player: { 
                        username: ''
                    },
                },
            ],
            rotated_players: [                // Contains the list of players that has been rotated to that
                {                             // the person that is playing this screen is shifted to position 0 (bottom of screen)
                    position: '',       
                    id: '',
                    player: { 
                        username: ''
                    },
                },
                {
                    position: '',
                    id: '',
                    player: { 
                        username: ''
                    },
                },
                {
                    position: '',
                    id: '',
                    player: { 
                        username: ''
                    },
                },
                {
                    position: '',
                    id: '',
                    player: { 
                        username: ''
                    },
                },
            ]
        }
    },
    created: async function () {
    //     // Make sure the data is processed before the page is rendered!!
    //     // Otherwise Vue can not see the data

        // // console.log('CREATED')

        // receive the gameID from the game details page
        this.game = this.$route.params.game
        this.players = this.$route.params.players
        // console.log('Players from params ', this.$route.params.players)
        // console.log('Players on CREATE ', this.players)
        
        // await this.doGetPlayers()
        // // console.log('gameID and players :', this.game.gameID, this.players[0].player.username)

        // Determine what your player position is
        for (var obj in this.players) {
            
            if (this.players[obj].player.username === this.user.username) {
                this.my_position = this.players[obj].position
            }
        }//END for

        // this.rotated_players = this.players
        // this.rotated_players = this.rotate(this.players, -this.my_position)
        this.rotated_players = this.rotateArray(this.players, -this.my_position)
        // console.log('Players on CREATE1 ', this.players)
        
        // // console.log('rotated players :', this.rotated_players[0].player.username)

        // Connnect to the socket !!!! Do not use, because a second channel will be created
        // We need the connect at activated.
        // this.connect()
        
    },
    activated: async function () {
        document.title = 'Klaverjasfun - Spelen'
        // // console.log('ACTIVATED')

        // console.log(this.$route.name)

        if (this.user.user_is_logged_in === false) {
                this.$router.push({ name: 'Home' })

        } else {
            //Check that screen is mobile. If so, set full screen
            var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
            if (isMobile) {
              // document.body.requestFullscreen()
              document.documentElement.requestFullscreen()
            }
            
            // Do not display the header
            this.user.show_header = false
            this.$store.dispatch('updateUser', this.user)

            // receive the gameID from the game details page
            this.game = this.$route.params.game
            this.current_leg = this.game.legs_completed   // 0 implies that leg[0] needs to be played
          
            // reset variables
            // When the page has already been created and is activated again,
            // the old variable values are still loaded. 
            // make sure that when activated that main settings are reset.
            this.next_to_play = 0
            this.rotated_next_to_play = 0
            this.cards= [
                {'color': 'red', 'rank': 'back'},       // Initially the player cards will show the back of the cards
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'},
                {'color': 'red', 'rank': 'back'}
            ]
            this.modalShow = false
            this.card_class = []
            this.play_class = []
            this.count_connected = 0
            this.cards_loaded = false    // inididator that playing cards have been loaded
            this.player_has_played = false
            this.current_leg = 0
            this.current_round = 0
            this.troef_selected = 0

            this.n_slag = 0
            this.show_new_leg = false   // remove
            this.show_new_round = false
            this.show_register_roem = false // Show the button the register roem
            this.show_take_round = false, 
            this.cards_slag = ['--', '--', '--', '--']
            this.count_cards_played = 0
            this.cards_loaded = false
            this.roem_value =  0
            this.total_roem = [0,0]
            this.state_data = ''
            this.show_leg_result = false
            this.name_player_leg = ''
            this.show_score_of_game = false
            this.total_scores = []         
            this.current_leg = 0
            this.show_close_game = false
            this.show_correct_roem = false
            this.show_melden_verzaken = false
            this.show_handle_verzaken = false
            this.radio_selected_team = 'A'
            this.my_team = ''
            this.show_verzaken_activated = false
            this.player_notified_verzaken = ''
            this.verzaakt = false


            const api_request = require('axios')

            // Get all the players of the game, using sync request.
            // this to make sure the players are loaded before the rest is done
            await api_request({
                method: 'get',
                url: this.appSettings.url_game_players + 'gameID=' + this.game.gameID 
                // data: this.input
            })
            .then(response => {
                // // console.log('Status get game overview: ',response.status)
                if (response.status === 200) {
                    // console.log('Response ', response.data)
                    this.players = response.data
                    // console.log('game on ACTIVATED ', this.game)
                    // console.log('Players fetched on ACTIVATED ', this.players)
                }
            })
            .catch(() => {
                // console.log('Get match details failed')
                // console.log(error.response)
            })

            // Determine what your player position is
            for (var obj in this.players) {
                
                if (this.players[obj].player.username === this.user.username) {
                    this.my_position = this.players[obj].position
                }
            }//END for
            this.rotated_next_to_play = this.calcRotatedPosition(this.next_to_play, this.my_position)

            // // console.log('my_position : ', this.my_position)

            // console.log('Before rotate ', this.players)
            this.rotated_players = this.rotateArray(this.players, -this.my_position)
            // console.log('***', this.rotated_players)
            // console.log('After rotate ', this.players)
            // this.rotated_players = this.players
            // // console.log('rotated players :', this.rotated_players[0].player.username)

            // Connnect to the socket 
            
            // Determine the team to which the player of this screen belongs
            if (this.my_position % 2 === 0) {
              this.my_team = 'A'
            } else {
              this.my_team = 'B'
            }
            
            this.connect()

            // console.log('troef in activated : ', this.troef_selected)

            // this.$forceUpdate()

            
        }//END if logged in 
          
    },//activated

    deactivated: function () { 
      // Destroy the websocket connection when leaving this page.
      var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
            if (isMobile) {
               document.exitFullscreen()
            }
      this.disconnectWS()      

    },

    methods: {

        // doShowAlert: function () {
        //     var count = this.cards_played.length
        //     if (count > 8) {
        //         alert('test')
        //     }
            
        // },

        connect() {
            // this.gameSocket = new WebSocket(
            this.gameSocket = new ReconnectingWebSocket(
                this.appSettings.url_Websocket  + this.game.gameID +   '/')

            
            this.gameSocket.onopen = () => {
                // console.log('Websocket connected opened at :', this.gameSocket.url)
            }

            this.gameSocket.onmessage = ({data}) => {
                this.data_received = JSON.parse(data)
                // // console.log('Websocket received data', this.data_received)

                switch(this.data_received.type) {
                  case 'confirm_connected':
                    // console.log('@@@@@@@@@ CONFIRM CONNECTED')
                    this.doConfirmConnected(this.data_received.channel)
                    break;

                  case 'statusUpdate':
                    // console.log('@@@@@@@@@ STATUS UPDATE')
                    this.doStatusUpdate(this.data_received.status)
                    break; 

                  case 'update_troef':
                     // console.log('@@@@@@@@@ UPDATE TROEF')
                    this.doUpdateTroef(this.data_received.troef) 
                    break; 

                  case 'send_new_round':
                    // console.log('@@@@@@@@@ SEND NEW ROUND')
                    this.doLoadNewRound(this.data_received) 
                    break;

                  case 'play_card':
                    // console.log('@@@@@@@@@ PLAY CARD')
                    this.doUpdatePlayedCard(this.data_received) 
                    break; 

                  // case 'send_players':            // NOT USED anymore
                  //   // console.log('@@@@@@@@@ SEND PLAYERS')
                  //   this.doUpdatePlayers(this.data_received) 
                  //   break;
                    
                  case 'signal_to_load_new_round':
                    // console.log('@@@@@@@@@ SIGNAL TO LOAD NEW ROUND')
                    this.doSignalNewRound(this.data_received) 
                    break; 

                  case 'winner_round':
                    // console.log('@@@@@@@@@ WINNER ROUND')
                    this.doShowTakeRound(this.data_received) 
                    break; 

                  case 'state_of_game':
                    // console.log('@@@@@@@@@ WINNER ROUND')
                    this.doHandleState(this.data_received) 
                    break; 

                  case 'send_scores':
                    // console.log('@@@@@@@@@ SEND SCORES')
                    this.doShowScores(this.data_received) 
                    break; 

                  case 'activate_verzaken':
                    // console.log('@@@@@@@@@ SEND SCORES')
                    this.doActivateVerzaken(this.data_received) 
                    break; 

                } //END Switch

                // if (this.data_received.type === 'confirm_connected') {
                //     // this will communicate the channel name that was opened
                //     // // console.log('Confirm connected', this.data_received.channel)
                //     // console.log('@@@@@@@@@ CONFIRM CONNECTED')
                //     this.doConfirmConnected(this.data_received.channel)
                // }

            }

            this.gameSocket.onerror = () => {
            // console.log('Websocket error')
            }

            this.gameSocket.onclose = () => {

                // console.log('Websocket is closed')
            }

        },

        sendToGroup(input) {
            // Note input must be a object with keys and values
            this.gameSocket.send(JSON.stringify(input));
        },

        disconnectWS() {
            // When you need to go back to another page, then the websocket connection
            // needs to be closed.
            // The channels consumer will set this player to disconnected.
            var message = {
                'type'      : 'connection_disconnected',
                'position'  : this.my_position,
                'gameID'    : this.game.gameID,
            }
            this.sendToGroup(message)
            this.gameSocket.close();
            // console.log('connection is disconnected')
        },

        checkWsStatus: function () {
            // console.log('status websocket :', this.gameSocket.readyState)
        },

        doCloseTroefAlert: function () {
          this.modalShow = false
          //Check that screen is mobile. If so, set full screen
          var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
          if (isMobile) {
            // document.body.requestFullscreen()
            document.documentElement.requestFullscreen()
          }

        }, //END doCloseTroefAlert

        doConfirmConnected: function (channel) {
            // When a connection is created channels will send a confirm_connected message.
            // After receiving this confirm_connected this page send back a message
            //  with gameID, position and channel to be logged in db.
            // Logging in DB is needed to be able to store the connection statusses of the players.

            var message = {
                'type'      : 'connected_update',
                'position'  : this.my_position,
                'gameID'    : this.game.gameID,
                'channel'   : channel
            }
            // Send over the Websocket to the group
           this.sendToGroup(message)

        },

        doHandleVerzaken: function () {
          // Display the screen to handle verzaken
          this.show_melden_verzaken = false
          this.show_handle_verzaken = true
          this.verzaakt = true

          // Also make sure this screen is shown to all other players
          // Other player should be able to view the played slagen, but not be able to select the team that verzaakt 
          var message = {
                'type'        : 'notify_verzaken',
                'player_name' : this.players[this.my_position].player.username
            }
            // Send over the Websocket to the group
           this.sendToGroup(message)
        },

        doActivateVerzaken: function (data) {
          // When a player has started the verzaken procdure all player will receive
          // a activate_verzaken message that will display the verzaken jumbotron
          // A reduced jumbotron will be shown that offers the possibility to view the slagen.
          // But it is not possible to select the team that receives all points


          // The player that initiated verzaken will not see the reduced screen
          if (data.player_name !== this.rotated_players[0].player.username) {
            this.show_verzaken_activated = true
            this.player_notified_verzaken = data.player_name
          }

        },

        doProcessVerzaken: function () {
          // Once the player has defined to which team the points should be assiged, this needs to 
          // be proccessed in the Django backend

          // var message = {
          //       'type'        : 'process_verzaken',
          //       'team'        : this.radio_selected_team    // value is A or B
          //   }
          //   // Send over the Websocket to the group
          //  this.sendToGroup(message)

            // The jumbotron must be closed
           this.show_handle_verzaken = false

            // Start a new Round and force this also to all other users
           this.doTakeRound()

           // @@ show the score of the round
           this.show_leg_result = true
          
        },

        doStatusUpdate: function (status) {
            // When a player gets connected or disconnected, the other players need to be informed.
            // Channels will send a statusUpdate message.
            // This message contains a list with (position of player, connected status)
            // When a position is not in the list, this implies that connected is false

            // Set all players to not connected
            this.list_connected = [false, false, false, false]

            // Check the status and if connected = true then update the list_connected
            // And count the number of connected players
            var count = 0
            for ( var item in status) {
                //  // console.log('item : ', status[item])

                if (status[item][1] === true) {
                    this.list_connected[status[item][0]] = true
                    count = count + 1
                }
            }

            // Based on updated status, make the playing cards active or non-active
            // only show start new round botton when 4 players are connected
            this.count_connected = count
            this.show_new_leg = false
            this.show_new_round = false
            if (this.count_connected === 4) {
              // this.show_new_leg = true
              this.show_new_round = true
            }

            // next load the cards. 
            // this.doLoadPlayerCards(this.cards)
            // console.log('BBBB', this.troef_selected)
            // this.doLoadNewRound(this.cards)
            this.doStartRound(false)


            // Add this status to the rotated_players
            for (var player in this.rotated_players) {
                this.rotated_players[player].connected = this.list_connected[this.rotated_players[player].position]
                // // console.log(player)
            }

            // // console.log('Status: ', this.rotated_players)

            // When a status update is received this must be rendered to the screen
            // this.$forceUpdate()
        },
        doSleep: function (ms) {
          // To wait some time. Use in a async function
          return new Promise(resolve => setTimeout(resolve, ms));
        },

        doGoBack: function () {
            // Disconnect from websocket and Go back to the games overview
            this.disconnectWS()
            var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
            if (isMobile) {
              document.exitFullscreen()
            }
            
            this.$router.push({ name: 'Games_overview' })
        },

        // doGetPlayers: function () {
        //   // Send request over Websocket to get the list of players
        //   // Not needed anymore
         
        //     var message = {
        //         'type'      : 'get_players',
        //         'gameID'    : this.game.gameID
        //     }
        //     // Send over the Websocket to the group
        //     this.sendToGroup(message)

        //     // console.log('DOGETPLAYERS')
        // },

        // doUpdatePlayers: function (data) {
        //   this.players = data.players
        //   // // console.log('new Players: ',data.players )
        //   // // console.log('new player', data.players)
        //   // for (var p in data.players) {
        //   //   // console.log(data.players[p])
        //   // }

        // },

        doSelectTroef: function () {
            // Troef may be changed on the following conditions
            // - only in the first round of a leg
            // - no cards have been played in the round
            // - the player that is next to play can change the troef
            if ( this.current_round === 0 
                  && this.count_cards_played === 0 
                  && this.next_to_play === this.my_position) {

              this.troef_selected = (this.troef_selected + 1) % 4     //Modulus 4

              // Send the selected troef to the WebSocket group
              var message = {
                  'type'      : 'update_troef',
                  'troef'     : this.troef_selected   // Is an integer [0..3]
              }
              // Send over the Websocket to the group
              this.sendToGroup(message)

              // // console.log(this.troef_selected)

            } else {
                // if (alert('Troef mag alleen aangepast worden door speler die aan de beurt is. Ook als het spel begonnen is mag de troef niet aangepast worden.')) { 
                //   // console.log('ja')
                // } else {
                //   var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
                //   if (isMobile) {
                //     document.body.requestFullscreen()
                //   }
                // }

                this.modalShow = true
                // alert('Troef mag alleen aangepast worden door speler die aan de beurt is. Ook als het spel begonnen is mag de troef niet aangepast worden.')
                // //Check that screen is mobile. If so, set full screen
                // var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
                // if (isMobile) {
                //   document.body.requestFullscreen()
                // }
            }//END if/else
        },

        doUpdateTroef: function (troef) {
            // Update the troef on screen as received from the Websocket group
            this.troef_selected = troef

            // Also update the sorting of the cards
            // Do this by load the cards again
            this.doStartRound(false)
            // this.startNewLeg()
        },

        doStartRound: function (button_pressed) {
          // Every players separately has to press this button to load his own cards
          // button_pressed = true: needs to send a signal to all players to also do this update

          // This function can be initiated by the player by pressing the start new Round button.
          // When this is done, a message needs to be send to all other players to load the new Round.
          // The other player will also call this doStartRound function from the websocket message.
          // In that case buttonpressed should be set to false, so no additional message is send to the group.

          this.show_register_roem = false
          this.show_take_round = false

          // console.log('Troef selected ', this.troef_selected)
          var message = {
                'type'          : 'request_new_round',
                'matchID'       : this.game.matchID.matchID,
                'gameID'        : this.game.gameID,
                'position'      : this.my_position,
                'troef'         : this.troef_selected,
                'button_pressed': button_pressed,            // true/false
                'n_legs'        : this.game.matchID.n_legs
                
          }
          // Send over the Websocket to the group
          // Note that the group channel will return the cards only to this player.
          // Also a signal will be given to the other player to load the rounds automatically
          this.sendToGroup(message)


        },//END doStartRound

        doSignalNewRound: function () {
          // A signal is received from the Websocket that a player has loaded a new game.
          // Now also the player has to load the new Round.
          // Make sure not to signal to the other players by setting the 'false' option.
          // Otherwise there will be a loop 

          this.doStartRound(false)
        },

        doLoadNewRound: function (data) {
          // After receiving information from the websocket for a new round
          // show the player cards on the screen in the hand of the player

          // reset values on loading a new Round
          this.player_has_played = false
          this.cards_slag = ['--', '--', '--', '--']  // Cards played in the round
          this.cards_loaded       = true              // Indicator that cards have been loaded
          this.count_cards_played = 0                 // Counts how many cards have been played in a round
          this.card_class = []
          this.play_class = []

          // Get the data coming from the websocket
          this.next_to_play       = data.next_to_play // Original player position of player to play next card.
          this.current_leg        = data.current_leg
          this.current_round      = data.current_round
          this.troef_selected     = data.troef
          this.total_roem         = data.roem

          this.rotated_next_to_play = this.calcRotatedPosition(this.next_to_play, this.my_position)

          //Determine the rotated_next_to_play, that is the position on the screen that needs to play

          // console.log('Game, Leg, Round, next to play :',this.game.gameID, this.current_leg, this.current_round, this.next_to_play)


          // If new cards received from websocket, use these new cards
          if (data.cards) {
            this.cards = data.cards         // the cards in the hand of the player
          } // Else just use this.cards

          // test no card
          // this.cards[2]['color'] = 'no-card'

          this.card_class = []        // reset the card classes
          // this.cards_played = []      // reset the cards played

          for (var card in this.cards) {
            var key = ''
            var hand = ''
            var classes = {}

            hand = 'hand_p0-' + card

            if (this.cards[card].color === 'no-card') {
              key = '-'    // Set no class for the card so that no card is shown
            } else { 
              key = this.cards[card].color + '_' + this.cards[card].rank
            }

            // Card must be shown as active (light up on hover) when
            // - all players are connected
            // - card is no back of the card
            // - card is not empty
            var card_active = false
            // if (this.count_connected === 4 && (key !== 'no-card' || this.cards[card].rank === 'back') ) {
            if (this.count_connected === 4 && (key !== '-' && this.cards[card].rank !== 'back')) {
              card_active = true 
            } 

            classes = {
                'card-holder'   : true,
                'card-active'   : card_active,
                'play_p0'       : false,
            }
            classes[hand]   = true
            classes[key]    = true

            this.card_class.push(classes)

            // // console.log(card, key, hand)
            // // console.log(this.card_class[card])
            // this.$forceUpdate()
          }

        },//END doLoadNewRound

        doPlayCard: async function (card) {
            // When a player selects an activated card, this card will be played.
            // The card will go to played position indicated by class .play_p0
            // Card the the number (integer) of the card played from the hand

            // Only move the card when 
            // - the card is active 
            // - this player has to play 
            // - this player did not already play a card in this round
            if (this.card_class[card]['card-active'] === true 
                  && this.next_to_play === this.my_position
                  && this.player_has_played === false) {

              // Set the indicator that this player has played a card
              this.player_has_played = true
              
              // Determine class of the card that will be played
              // Make this card inactive and move is to the played position (class .play_p0)
              var hand = 'hand_p0-' + card
              this.card_class[card][hand] = false
              this.card_class[card]['card-active'] = false
              this.card_class[card]['play_p0'] = true

              // Send the played card to the group
              // Also send the onPlay variable, which indicated which player has to play.
              // Let Django do the increment of this variable, so that is can be send to all players.
              var message = {
                  'type'                : 'play_card',
                  'position'            : this.my_position,       // Original position of the player playing this card
                  'color'               : this.cards[card].color,
                  'rank'                : this.cards[card].rank,
                  'next_to_play'        : this.next_to_play,      // Who has played the card (wie aan de beurt was)
                  'count_cards_played'  : this.count_cards_played
                  }

              // Send the message over the Websocket to the group
              this.sendToGroup(message)

              // Register the card played by the player in this Round (slag)
              // Store is to the original player position
              this.cards_slag[this.my_position] = {
                  'color'     : this.cards[card].color,
                  'rank'      : this.cards[card].rank
                  }

              // console.log('BB ', this.cards_slag)

            }//END if

        },//END doPlayCard

        doUpdatePlayedCard: async function (data) {
            // This function is executed when a 'play_card' message is received over the websocket.
            // Who is next to play is update, along with the count of cards that have been played in this round

            // Store these updated values in the global variables.
            this.count_cards_played = data.count_cards_played
            this.next_to_play = data.next_to_play
            this.rotated_next_to_play = this.calcRotatedPosition(this.next_to_play, this.my_position)

            var p = this.calcRotatedPosition(data.position, this.my_position)
            

            // // console.log('play position: ', p)

            // The updates only come from the group Websocket, so do not
            // add the card of the player looking at the screen.
            // console.log('Before p ', this.cards_slag)
            // console.log('p = ', p)
            if (p !== 0) {

              // Next create the card at the p position in the screen
              // The card is and placement is created by setting the classes
              var classes = {}

              // Set the z-index, so that the latest card will be on top
              // var z = this.cards_played.length
              // var z_index = 'z' + z
              // classes[z_index] = true

              // Card needs to move from the hand position (player 1/2/3) to the played card position.
              var hand = 'hand_p' + p
              var play = 'play_p' + p
              var key = data.color + '_' + data.rank
              // // console.log('played card :', key)

              // The playing of the card will be done animated/
              // First put the played card on the player hand position.
              // Next the card will move to the played position

              // Show card a 'hand' position
              classes = {
                  'card-holder'   : true,
                  'card-active'   : false
              }
              classes[hand]   = true
              classes[play]   = false
              classes[key]    = true

              // Add the class to the cards on the hand position
              this.play_class.push(classes)

              // Show the card for 0.5 sec on this position
              await this.doSleep(500);

              // Next put the card at the play position.
              // This wil create a transform  (flow of the card)
              this.play_class.pop()     // remove the class

              classes[hand]   = false
              classes[play]   = true
              classes[key]    = true

              // Add the class to the played cards
              this.play_class.push(classes)

            }//END if p !==0

            // Register the card played by the player in the round (slag)
            // A slag card contains position, color and rank
            // console.log('DDD', data.position, data.color, data.rank  )
            this.cards_slag[data.position] = {
              'color'     : data.color,
              'rank'      : data.rank
            }

            // console.log('BBB ', this.cards_slag)

            // // console.log('Current SLAG : ', this.cards_slag )

            // Check when 4 cards have been played in this round.
            // When this count_cards_played === 4 the round (slag) is complete and 
            // needs to be stored and a new round needs to be loaded
            if (this.count_cards_played === 4) { 
              // Only the player with the original position 0 (my_position = 0) will initiate the registration.
              // this to avoid collisions when multiple players do the same action at the same time

              // First the cards of the round will be send to the group.
              // This will send back to all players the person that won this round.
              // The player that won will see a button to take the slag.
              // Before that the person can first register any roem before taking the round
              // The roem button will only show for the player that won the round.


              // First send the round info to the backend, so that the backend
              // can send back who has won the round
              if (this.my_position === 0) {
                // Send the played card to the group
                // console.log('CCC ', this.cards_slag)

                var message = {
                    'type'      : 'check_round',
                    'gameID'    : this.game.gameID,
                    'leg'       : this.current_leg,           // starts with 0
                    'round'     : this.current_round,         // starts with 0
                    'cards'     : this.cards_slag,
                    'troef'     : this.troef_selected,        // this is a number 0..3 representing clubs, hearts, spades, diamonds
                    

                }
                // Send over the Websocket to the group
                this.sendToGroup(message)

              }

              // After playing a round keep on loading new rounds 
              // Until the game has been completed
              // NOTE: 
              // console.log(this.current_round != 7 && this.current_leg != this.game.matchID.n_legs -1)
              // console.log(this.current_round, this.game.matchID.n_legs -1)
              if (this.current_round == 7 && this.current_leg == this.game.matchID.n_legs -1) {
                // @@ 
                // console.log('leg must be closed')
                // this.troef_selected = 0 // reset the selected troef

              } else {
                // await this.doSleep(1500)
              }


              // @@ initate new round

            }//END if

        },

        doShowTakeRound: function (data) {
          // On receiving 'winner_round' show the take round button 
          // only for the player that has won the slag
          // Also show the button to register roem.

          this.show_take_round = false
          this.show_register_roem = false

          if (data.winner === this.my_position) {
            this.show_take_round = true
            this.show_register_roem = true
          }

          // console.log('AAA', this.cards_slag)

        }, //END doShowTakeRound

        doTakeRound: function () {
          // Take the round, and send the info to be processed to the backend (log_round)
          // Only the winner, or person that reports 'verzaken'can send this info to the backend
          // django will send info back that will be processed by doHandleState
          // console.log('AAAA', this.cards.slag)

          // Send the played card to the group
          var message = {
              'type'            : 'log_round',
              'gameID'          : this.game.gameID,
              'leg'             : this.current_leg,           // starts with 0
              'round'           : this.current_round,         // starts with 0
              'cards'           : this.cards_slag,
              'troef'           : this.troef_selected,        // this is a number 0..3 representing clubs, hearts, spades, diamonds
              'roem'            : this.roem_value,
              'verzaakt'        : this.verzaakt,              // If true then it will handle the verzaakt process
              'team_get_points' : this.radio_selected_team     // value is A or B
          }

          // Send over the Websocket to the group
          this.sendToGroup(message)

        },

        doHandleState: function (data) {
          // Receive 'state_of_game' from the Websocket. This was iniitated in backend by log_round
          // This is a indicator that next round needs to be played, leg is completed or game is completed

          this.state_data = data
          // console.log('STATE received : ', this.state_data)

          if (this.state_data.state === 'next_round') {
            // Start new round
            // console.log('Next round')
            this.doStartRound(true)
            this.show_take_round = false
            this.show_register_roem = false
            this.roem_value = 0               // reset to 0, otherwise the old value is default in the next round
          }

          // Show the completed leg information
          // On the leg result a button to shown to go to continueLegResult()
          if (this.state_data.state === 'end_of_leg' || this.state_data.state === 'end_of_game') {
            // console.log('Leg completed or end of game')
            this.show_leg_result = true

            //  Show the name of the player that 'heeft aangenomen' in the leg result.
            // doing the statement directly in {{ .. }} does not work
            // console.log('Players before aangenomen ',this.state_data.player_aangenomen, this.players)
            this.name_player_leg =  this.players[this.state_data.player_aangenomen].player.username

            // reset verzaakt
            this.verzaakt = false

          }
          
        }, //END doHandleState

        continueLegResult: function () {
          // Continue button on leg result field.

          // Remove the leg result jumbotron
          this.show_leg_result = false

          // When end_of_leg that start a new leg and round
          if (this.state_data.state === 'end_of_leg') {

            // console.log('@@ New leg')
            this.doStartRound(true)
            this.show_take_round = false
            this.show_register_roem = false
            this.roem_value = 0 

          } else {
            // console.log('@@ End game')
            alert('Einde van dit potje')
            this.doGetScores()
            this.show_take_round = false
            this.show_register_roem = false
            this.show_close_game = true
          }

        }, //END continueLegResult

        showCorrectRoem: function () {
          this.show_correct_roem = true

        }, //END correctRoem

        stopCorrectRoem: function () {
          this.show_correct_roem = false

        }, //END stopCorrectRoem

        doCorrectRoem: function () {
          this.state_data.roemA = this.corrected_roemA
          this.state_data.roemB = this.corrected_roemB
          this.show_correct_roem = false


        }, //END doCorrectRoem

        doGetScores: function () { 
          // Send a request to Django to get the current leg scores of the game
          // When the websocket send the response this is processed by doShowScores

          // Send the played card to the group
          var message = {
              'type'      : 'request_scores',
              'gameID'    : this.game.gameID,
          }

          // Send over the Websocket to the group
          this.sendToGroup(message)

        }, //END doGetScores

        doShowScores: function (data) {
          // When the websockets send the leg scores of the current game this needs to be shown.

          this.leg_scores = data.scores_per_leg   
          this.total_scores = data.totalscores

          // open the jumbotron
          this.show_score_of_game = true


        }, //END doShowScores

        doShowSlagen: function () {

          // console.log('Before emit', this.current_leg)
          this.$root.$emit('changeLeg', this.current_leg);

          this.variables.show_slagen = true
          this.$store.dispatch('updateVariables', this.variables)
          

        }, //END doShowSlagen

        doResetLeg: function () {
          // Send a request to the backend to reset the current leg.
          // This implies removing all the played rounds op this leg
          // and setting the rounds_completed  = 0 in the game.
          alert('Needs to be developed')

          // var message = {
          //     'type'                : 'request_reset_leg',
          //     'gameID'              : this.gameID,
          //     'leg'                 : this.current_leg
          //     }   

          // // Send the message over the Websocket to the group
          // this.sendToGroup(message)

        },

        // rotate: function (array1, k) {
        //     // Rotate an array by k elements
        //     var array = array1
        //     if (array.length > k) {
        //         array.unshift( ...array.splice(-k))
        //     } else {
        //         let i = 0
        //         while (i<k) {
        //             array.unshift(array.splice(-1))
        //             i++
        //         }//END while
        //     }//END if
        //     return array
        // },//END Rotate

        rotateArray: function (array, k) {
            // Rotate an array by k elements
            // k must be between -array.length and + array.length
            // array [0,1,2,3]  with k=-1 will result in [1,2,3,0]

            // If k < 0  then add the array.length to make a positive number
            // so k = -1 behaves the same a k = 3 for an 4 element array
            var len = array.length
            if (k < 0) {
              var kk = len + k
            } else {
              kk = k
            }

            // Create an empty array
            var rot_array = []
            var i = 0
            for (var item in array) {
              rot_array.push(item)
            }

            // Shift the elements of the array
            var n = 0
            for (i = 0; i < len; i++) {
              n = (i + kk) % len
              // console.log(len, k, kk, i, n)
              rot_array[n] = array[i]
            }

            // console.log('Ori array ', array)
            // console.log('Rot array ', rot_array)

            return rot_array
        },//END Rotate

        calcRotatedPosition: function (pos, my_pos ) {
          // Given a original position pos, calculate the rotated position 
          // from perspective of a player that is on position my_pos
          // my_pos is an interger 0....3

          var p = ( pos - my_pos ) % 4      // take modulo 4
            // Modulo -1 does not result in (3), so correct this.
            // Only correct this in the range -3 till 7
            if (p < 0) {
              p = p + 4
            }
            if (p>3) {
              p = p - 4
            }

            // console.log('@@@@@@', pos, p)

            return p 

        }//END calcRotatedPosition

    },  //END methods
  computed: {
    user () {
      return this.$store.state.user
    },
    appSettings () {
      return this.$store.state.appSettings
    },
    variables () {
      return this.$store.state.variables
    },
    window_size () {
      return this.$store.state.window_size
    }
  }
}
</script>

<style scoped lang='scss'>
// function with input px and output vw
// @function get-vw($font)
//   @if $vw-enable
//     $vw-context: $vw-viewport * 0.01 * 1px

//     @return $font / $vw-context * 1vw

//   @return $font


// Define variables
$height_header: 0px;
$width_card: 63px;
$height_card: $width_card * 1.4;
$v_offset: 10px;                   // Vertical offset 

.o_fullscreen {
  height: calc(100vh - #{$height_header});
  width:100vw;
  background-color: green;
  // margin: 0 auto;    // To center
  text-align: center;
  padding: 5px 5px 5px calc(0*#{$width_card}); //take into consideration the overlap of cards
}

.gameID {
  display: block;
  position: fixed;
  left: calc( 100vw/2 );
  top: 2px + $v_offset;
  transform:translate(-105%,0%);
  font-size: 1.3em;
  color: orange;
  font-family: sans-serif;
  font-weight: bold;
}

.leg {
  display: block;
  position: fixed;
  left: calc( 100vw/2 );
  top: 2px + $v_offset;
  transform:translate(+05%,0%);
  font-size: 1.3em;
  color: orange;
  font-family: sans-serif;
  font-weight: bold;
}

.goback {
  display: block;
  position: fixed;
  left: 5px;
  top: 45px + $v_offset;
  // transform:translate(-50%,0%);
  font-size: 1.0em;
  color:white;
  font-family: sans-serif;
  font-weight: bold;
  width: 30vw;
}

.action_menu {
  display: block;
  position: fixed;
  right: 5px;
  top: 45px + $v_offset;
  z-index: 10;
  // transform:translate(-50%,0%);
  // font-size: 1.0em;
  // color:white;
  // font-family: sans-serif;
  // font-weight: bold;
  // width: 30vw;
  
}

.reset_slag {
  display: block;
  position: fixed;
  right: 5px;
  top: 45px + $v_offset;
  // transform:translate(-50%,0%);
  font-size: 1.0em;
  color:white;
  font-family: sans-serif;
  font-weight: bold;
  width: 30vw;
  
}


.show_scores {
  display: block;
  position: fixed;
  right: 5px;
  top: 85px + $v_offset;
  // transform:translate(-50%,0%);
  font-size: 1.0em;
  color:white;
  font-family: sans-serif;
  font-weight: bold;
  width: 30vw;
}

.show_slagen {
  display: block;
  position: fixed;
  right: 5px;
  top: 125px + $v_offset;
  // transform:translate(-50%,0%);
  font-size: 1.0em;
  color:white;
  font-family: sans-serif;
  font-weight: bold;
  width: 30vw;
  z-index:20;
}

// general colors for nametag
.nametag {
    font-size: 1.1em;
    color: rgb(196, 196, 30);
    font-family: sans-serif;
    font-weight: bold;
    // background-color: grey;
}

.text_active {
  // color: white;
  // color: rgb(128, 245, 105);
  color: rgb(250, 250, 0);
  font-size: 1.7em;
}

.text_inactive {
  color: rgb(200, 200, 200);
}

// tag per player
.tag_p0 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 3.0*#{$height_card} + 5px );
  transform:translate(-50%,0%);
}

.tag_p1 {
  display: block;
  position: fixed;
  left: calc( 0.25*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 0.5*#{$height_card} + 5px );
}

.tag_p2 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  - 3.0*#{$height_card} - 15px );
  transform:translate(-50%,0%);
}


.tag_p3 {
  display: block;
  position: fixed;
  right: calc( 0.25*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 0.5*#{$height_card} + 5px );
}

// Show status circle in color per player
.dot_1 {
  display: block;
  position: fixed;
  left: calc( 0.60*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} - 24px );
  height: 20px;
  width: 20px;
  border-radius: 50%;
  display: inline-block;
}

.dot_2 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  - 2.0*#{$height_card} - 5px );
  transform:translate(-50%,0%);
  height: 20px;
  width: 20px;
  border-radius: 50%;
  display: inline-block;
}

.dot_3 {
  display: block;
  position: fixed;
  right: calc( 0.55*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} - 24px );
  height: 20px;
  width: 20px;
  border-radius: 50%;
  display: inline-block;
}

// define the color of the status
.connected {
   background-color: rgb(128, 245, 105); 
}

.not-connected {
    background-color: red; 
}

.roem_select {
  display: block;
  position: fixed;
  left: 2px;
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
  transform:translate(0%,-95%);
}

.roem {
  display: block;
  position: fixed;
  left: 20px;
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 2.0*#{$height_card} - 15px );
  color: yellow;

}

.roem_teamA {
  display: block;
  position: fixed;
  left: 20px;
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 2.0*#{$height_card} );
  color: white;
}

.roem_teamB {
  display: block;
  position: fixed;
  left: 20px;
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 2.0*#{$height_card} + 15px);
  color: white;
}

.take_round {
  display: block;
  position: fixed;
  // right: calc( 100vw/4 );
  right: 2px;
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
  transform:translate(0%,-100%);
}

.jumbotron {
  display: block;
  position: fixed;
  left: calc( 100vw/2 );
  top: calc( #{$v_offset} + 100vh/2 );
  z-index: 20;
  transform:translate(-50%,-70%);
  width: 90vw;
}

.slagen {
  z-index:30
}

// Player card bottom
.play_p0 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc(#{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 0.5*#{$height_card} );
  transition-property: display, position, left, top;
  transition-duration: 0.7s;
}

// player card left
.play_p1 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 1.5*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
  transition-property: display, position, left, top, right, transform;
  transition-duration: 0.7s;
}

// player card top
.play_p2 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 1.5*#{$height_card} );
  transition-property: display, position, left, top, right, transform;
  transition-duration: 0.7s;
}

// player card right
.play_p3 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 + 0.5*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
  transition-property: display, position, left, top, right, transform;
  transition-duration: 0.7s;
}

// Hand of other players to start from playing a card to the middle
.hand_p1 {
  display: block;
  position: fixed;
  left: calc( 0.25*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
  transform: rotateZ(180deg);
}

.hand_p2 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  - 3.0*#{$height_card} );
  transform: rotateZ(270deg);
}

.hand_p3 {
  display: block;
  position: fixed;
  left: calc(100vw - 1.25*#{$width_card} );
  // right: calc( 0.25*#{$width_card} );  // Do not use right, because transition will not function using left/right
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
  transform: rotateZ(180deg);
}

// Calulate the total space per card. 
// 8 cards should fit on the screen. 
// maximalize the spacing beteeen the cards 

$side_margin: 5px;   // minimal margin on left and right side of screen. 
$max_margin: 10px;
$margin: 10px;
// $N: 8;               // Number of cards to fit on screen
// $margin: 2px; 
// $dummy1: $N - 1;
// $dummy2: calc(100vw - 2 * #{$side_margin} - 8 * #{$width_card});
// $margin: calc(#{$dummy2} / #{$dummy1});
// $margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / 7);
// $margin: calc(#{$dummy2} / #{$dummy1});
// $margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / ($N - 1));
// calc( (100vw - 2*#{$side_margin} - 8*#{$width_card} ) / (#{$N}-7) );  // spzce between cards
// (100vw - 2*$side_margin - 8*$width_card ) / ($N-7) ;
$margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / 7);
// CANNOT limit margin to < 10 px.

// make the margin flexible when the screen is snaller than xxxpx
// @media screen and (min-width: 480px) {
//       $margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / 7);
// } 


// $margin: $margin + 10%;
// $test: calc(#{$margin} - 10px);
// @if calc(#{$test} ) < 0 {
//     $margin: 10px;
// }

@media screen and (min-width: 400px) {
  $margin: calc(10px);
}


.hand_p0-0 {
  $pos: -4;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-1 {
  $pos: -3;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-2 {
  $pos: -2;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-3 {
  $pos: -1;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-4 {
  $pos: -0;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-5 {
  $pos: 1;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-6 {
  $pos: 2;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-7 {
  $pos: 3;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.troef_place {
    width:0.9 * $width_card;
    display: block;
    position: fixed;
    left: calc( 100vw/2 + 2px);
    top: calc(  #{$v_offset} + (100vh - #{$height_header}) / 2  + #{$height_header} - 0*#{$height_card} );
    transform:translate(-50%, -50%);
    background-image: '../assets/Cards/hearts.png';
    
}

.card-holder{
  width:$width_card;
  height:$height_card;
  box-shadow:2px 2px 2px rgba(0,0,0,.8);
  border-radius: 5px;
  background-color: rgb(11, 97, 11);
  // position:relative;
  // display:inline-block;
  margin-top:2px;
  margin-left: 2px;
  // margin-left: calc(-0.50*#{$width_card});   // Overlap the cards

  transform-style: preserve-3d;
  backface-visibility: hidden;

  background-repeat:no-repeat;
  background-position: 0% 0%;
  background-size: 100% 100%;
}

.place_turn {
  background-color: rgb(107, 192, 107);
  background-repeat:no-repeat;
  background-position: 0% 0%;
  background-size: 100% 100%;
}

.card-active:hover {
  box-shadow:0px 5px 10px rgba(0,0,0,.7);
  transform:translate(0px,-5px);
}
.card-active:active{
  transform:scale(.9);
}

.z0 {
    z-index: 0;
}

.z1 {
    z-index: 1;
}

.z2 {
    z-index: 2;
}

.z3 {
    z-index: 3;
}

.z4 {
    z-index: 4;
}

.z5 {
    z-index: 5;
}

.z6 {
    z-index: 6;
}

.z7 {
    z-index: 7;
}

.z8 {
    z-index: 8;
}

.z-1 {
    z-index: -1;
}


//******** Define the cards **************************************** */

.hearts_ace {
  background-image: url('../assets/Cards/AH.png');
}

.hearts_two {
  background-image: url('../assets/Cards/2H.png');
}

.hearts_three {
  background-image: url('../assets/Cards/3H.png');
}

.hearts_four {
  background-image: url('../assets/Cards/4H.png');
}

.hearts_five {
  background-image: url('../assets/Cards/5H.png');
}

.hearts_six {
  background-image: url('../assets/Cards/6H.png');
}

.hearts_seven {
  background-image: url('../assets/Cards/7H.png');
}

.hearts_eight {
  background-image: url('../assets/Cards/8H.png');
}

.hearts_nine {
  background-image: url('../assets/Cards/9H.png');
}

.hearts_ten {
  background-image: url('../assets/Cards/10H.png');
}

.hearts_jack {
  background-image: url('../assets/Cards/JH.png');
}

.hearts_queen {
  background-image: url('../assets/Cards/QH.png');
}

.hearts_king {
  background-image: url('../assets/Cards/KH.png');
}


//************************************************ */

.spades_ace {
  background-image: url('../assets/Cards/AS.png');
}

.spades_two {
  background-image: url('../assets/Cards/2S.png');
}

.spades_three {
  background-image: url('../assets/Cards/3S.png');
}

.spades_four {
  background-image: url('../assets/Cards/4S.png');
}

.spades_five {
  background-image: url('../assets/Cards/5S.png');
}

.spades_six {
  background-image: url('../assets/Cards/6S.png');
}

.spades_seven {
  background-image: url('../assets/Cards/7S.png');
}

.spades_eight {
  background-image: url('../assets/Cards/8S.png');
}

.spades_nine {
  background-image: url('../assets/Cards/9S.png');
}

.spades_ten {
  background-image: url('../assets/Cards/10S.png');
}

.spades_jack {
  background-image: url('../assets/Cards/JS.png');
}

.spades_queen {
  background-image: url('../assets/Cards/QS.png');
}

.spades_king {
  background-image: url('../assets/Cards/KS.png');
}

//************************************************ */

.diamonds_ace {
  background-image: url('../assets/Cards/Ace_diamonds.png');
}

.diamonds_two {
  background-image: url('../assets/Cards/2D.png');
}

.diamonds_three {
  background-image: url('../assets/Cards/3D.png');
}

.diamonds_four {
  background-image: url('../assets/Cards/4D.png');
}

.diamonds_five {
  background-image: url('../assets/Cards/5D.png');
}

.diamonds_six {
  background-image: url('../assets/Cards/6D.png');
}

.diamonds_seven {
  background-image: url('../assets/Cards/7D.png');
}

.diamonds_eight {
  background-image: url('../assets/Cards/8D.png');
}

.diamonds_nine {
  background-image: url('../assets/Cards/9D.png');
}

.diamonds_ten {
  background-image: url('../assets/Cards/10D.png');
}

.diamonds_jack {
  background-image: url('../assets/Cards/JD.png');
}

.diamonds_queen {
  background-image: url('../assets/Cards/QD.png');
}

.diamonds_king {
  background-image: url('../assets/Cards/KD.png');
}

//************************************************ */

.clubs_ace {
  background-image: url('../assets/Cards/AC.png');
}

.clubs_two {
  background-image: url('../assets/Cards/2C.png');
}

.clubs_three {
  background-image: url('../assets/Cards/3C.png');
}

.clubs_four {
  background-image: url('../assets/Cards/4C.png');
}

.clubs_five {
  background-image: url('../assets/Cards/5C.png');
}

.clubs_six {
  background-image: url('../assets/Cards/6C.png');
}

.clubs_seven {
  background-image: url('../assets/Cards/7C.png');
}

.clubs_eight {
  background-image: url('../assets/Cards/8C.png');
}

.clubs_nine {
  background-image: url('../assets/Cards/9C.png');
}

.clubs_ten {
  background-image: url('../assets/Cards/10C.png');
}

.clubs_jack {
  background-image: url('../assets/Cards/JC.png');
}

.clubs_queen {
  background-image: url('../assets/Cards/QC.png');
}

.clubs_king {
  background-image: url('../assets/Cards/KC.png');
}

//************************************************ */

.red_back {
  background-image: url('../assets/Cards/red_back.png');
}






</style>
  



