<template>
  <div class="Appgame_details">

    <!-- Show Send mail  -->
    <b-jumbotron class="jumbotron" v-bind="{hidden: !show_send_mail}">
        <h3>Verstuur mail </h3>
        <p> 
            U kunt een anonieme mail sturen naar de andere spelers van dit potje om informatie te delen over:
            <ul>
                <li>datum en speeltijden</li>
                <li>de te gebruiken video meetings</li>
                <li>telefoonnummer of mail addressen om nader af te spreken</li>
            </ul>
        </p>

          <div>
            <b-form-textarea
            id="textarea"
            v-model="mailText"
            placeholder="Schrijf hier uw mail"
            rows="3"
            max-rows="6"
            ></b-form-textarea>

            <!-- <pre class="mt-3 mb-0">{{ text }}</pre> -->
        </div>


        <b-row>
            <b-col><b-button block @click="doStopMail()"  class="btn btn-danger"> Stoppen  </b-button></b-col>
            <b-col><b-button block v-on:click="doSendMail()" variant="primary" class="btn"> Verstuur mail  </b-button></b-col>
        </b-row>
    </b-jumbotron>


    <b-container v-if="isLoaded">

        <b-row v-if="allow_play_game">
            <!-- <b-col ><b-button block class="btn btn-warning"> Accepteer partner </b-button> </b-col>  -->
            <b-col>
                <b-form-checkbox
                    id="lock_game"
                    v-model="game.locked"
                    @change="lockGame(game.locked)"
                >
                Overschijven spelers verbieden 
                </b-form-checkbox>
            </b-col>
            <b-col ><b-button @click="playGame(game, players)"  class="btn btn-success"> speel dit potje  </b-button> </b-col> 
        </b-row>
        

        <br>
        <b-card  class="bg-secondary text-center">
        <b-row>
            <b-col ><b-button @click="doRegister(0)"  v-bind:disabled="!allow_register || game.locked" block class="btn btn-light"> A1: {{  sorted_players[0].player.username }} </b-button> </b-col> 
            <b-col ><b-button @click="doRegister(1)" v-bind:disabled="!allow_register || game.locked" block class="btn btn-dark"> B2: {{  sorted_players[1].player.username }} </b-button> </b-col> 
        </b-row>
        <br>
        <b-row>
            <b-col ><b-button @click="doRegister(3)" v-bind:disabled="!allow_register || game.locked" block class="btn btn-dark"> B4: {{  sorted_players[3].player.username }} </b-button> </b-col> 
            <b-col ><b-button @click="doRegister(2)" v-bind:disabled="!allow_register || game.locked" block class="btn btn-light"> A3: {{  sorted_players[2].player.username }} </b-button> </b-col> 
        </b-row>
        </b-card>

        <br>

        <b-row>
            <b-col><b-button @click="doUnRegister()" v-if="allow_unregister" v-bind:disabled="!allow_unregister" block class="btn btn-warning"> Afmelden bij potje  </b-button> </b-col> 
            <b-col><b-button @click="doShowMail()" v-if="allow_send_mail"  block variant="primary" > Stuur bericht naar spelers  </b-button> </b-col>
        </b-row>


    </b-container>

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Appgamedetails',
  props: {
    // Case instance to use in this component
    game: Object
  },
  data () {
    return {
        title: 'Game details page',
        polling: null,            // Needed to auto refresh this page
        isLoaded: false,
        lock_game: false,           // lock game for registering overwriting a position
        mailText: '',               // Input mail text
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
        sorted_players: [ 
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
        // allow_make_new_game: false,         // For button to make new game,  not needed on this page
        allow_register: false,              // For button to register a player to a game
        allow_unregister: false,            // For butoon to un-register a player from a game
        allow_play_game: false,             // For button to play the game
        allow_send_mail: false,             // For button to let the form start for sending mails
        player_is_registered: false,        // indicator that player is registered to the game
        show_send_mail: false,              // For showing the send mail form
        errors: {}, 
    }
  },
  created: function () {
      // receive the matchID from the match details page
        this.matchID = this.$route.params.matchID;
        // // console.log(this.game)

        if (this.game.length !== 0) {
        this.getPlayers()
        } 

  },
  deactivated () {
    // To stop refreshing the data when the page is left
    clearInterval(this.polling)
  },

  activated: function () {
      // Refresh this component every x seconds
    //   this.pollData()

      if (this.user.user_is_logged_in === false) {
            this.$router.push({ name: 'Home' })
      } else {
          // receive the matchID from the match details page
          this.matchID = this.$route.params.matchID;

          if (this.game.length !== 0) {
            this.doRefresh()
          } 
          
      }//END if
  },//END mounted
  methods: {
    pollData () {
      // To refresh the data every x seconds
      // https://renatello.com/vue-js-polling-using-setinterval/
      this.polling = setInterval(() => {
        this.doRefresh()
      }, 1000)
    },
    doRefresh: function () {
        this.getPlayers()
    }, //END doRefresh

    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    },  //END gotoLogin
    playGame: function (game, players) {
        this.$router.push({ name: 'Game_play', params: { 'game': game, 'players': players} })

        let message = 'Speel potje ' + this.matchID + '/' + game.gameID
        this.logButton(message)
        message = 'Play game: ' + this.matchID + '/' + game.gameID
        this.logAction(message)
    },
    doHideElement: function (id) {
        var x = document.getElementById(id);
        x.style.display = "none";
    },
    doShowElement: function (id) {
        var x = document.getElementById(id);
        x.style.display = "block";
    },
    filterOnUsername: function (item) {
        // Filter the players on usersname
      return item.player.username === this.user.username
    },
    doShowMail: function () {
        this.show_send_mail = true

    },
    doStopMail: function () {
        this.mailText = ''
        this.show_send_mail = false

    },
    lockGame: async function (value) {
        // lock_game value is changed by the checkbox using the v-model

        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        // Update the lock status to the game
        await api_request({
            method: 'put',
            url: this.appSettings.url_games_update + this.game.gameID + '/',
            data: {
                gameID: this.game.gameID,
                locked: value,
            }
        })
        .then(response => {
            if (response.status === 200) {
                // console.log(response.status)
                if (value === true) {
                    let message = 'Locked Game: ' + this.matchID + '/' + this.game.gameID
                    this.logButton(message)
                    this.logAction(message)
                } else {
                    let message = 'Unlocked Game: ' + this.matchID + '/' + this.game.gameID
                    this.logButton(message)
                    this.logAction(message)

                }
            }
        })
        .catch(error => {
            // console.log(error.response.data)
            alert(error.response.data[1])

        })

    },
    doSendMail: async function () {
        // Send a mail to the players
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        if (this.mailText.length !== 0) {

            await api_request({
                method: 'post',
                url: this.appSettings.url_games_mail,
                data: {
                    gameID: this.game.gameID,
                    mailText: this.mailText,
                }
            })
            .then(response => {
                if (response.status === 200) {
                    alert(response.data[1])
                    let message = 'Send mail to players, potje: ' + this.game.gameID 
                    this.logButton(message)
                    message = 'Send mail to players, potje: ' + this.game.gameID + "\n" + this.mailText
                    this.logAction(message)
                    this.show_send_mail = false
                    this.mailText = ''
                }
            })
            .catch(error => {
                // console.log(error.response.data)
                alert(error.response.data[1])

            })

        } else {
            alert('Vul eerst de tekst voor de mail in')
        }

    },  //END doSendMail


    getPlayers: async function () {
        // Get the players registered for this game
        // Check the condition to show the buttons to start the game
        // create a sorted_players list in which the players are sorted to position on screen [0,1,2,3]
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        await api_request({
            method: 'get',
            url: this.appSettings.url_game_players + 'matchID=' + this.game.matchID.matchID + '&gameID=' + this.game.gameID
            // data: this.input
        })
        .then(response => {
            if (response.status === 200) {
                this.players = response.data
            }
        })
        .catch(() => {
            // console.log(error.response)
        })

        
        // Sort the players based on position (note:  django should have returned an sorted list)
        // this.players.sort((a, b) => (a.position > b.position) ? 1 : -1)

        // Create an empty player
        var dummy = {}
        dummy.position = ''
        dummy.player = {'username': '--geen speler--'}

        // Put empty players in the sorted player list
        // // console.log(this.players[1])
        this.sorted_players = []
        var i
        for (i = 0; i < 4; i++) {
            this.sorted_players[i] = dummy
        }

        // Fill the sorted players with the players received from the Backend
        var count_players = 0
        for (var obj in this.players) {
            this.sorted_players[this.players[obj].position] = this.players[obj]
            count_players = count_players + 1
        }

        // ********************************************************************************************************
        // Validate allow_play_game  (is play the game)
        //   * match start date is passed (check this because after game was created the start date was changed)
        //   * 4 players registered at game, and this player is part of the game
        //   * Game is not ended , that is Not all legs have been completed
        //   * Match stop date not expired, and game not already started
        //
        // 

        // Buttons to validate on this page
        //  - Aanmelden bij potje
        //  - Afmelden bij potje
        //  - speel potje
        //  - Stuur mail naar spelers

        // Reset buttons
        // this.allow_make_new_game    = false      // Not needed on this page
        this.allow_register         = false
        this.allow_unregister       = false
        this.allow_play_game        = false
        this.allow_send_mail        = false
        this.player_is_registered   = false

        // initialize parameters
        var check_match_start_passed            = false
        var check_match_stop_passed             = false
        var check_match_registerstop_passed     = false

        var check_four_players_registered       = false         // There are 4 players registered at this game
        var check_player_is_registered          = false         // player is registerd at this game
     
        var check_game_has_not_ended            = false         // Game has not been completed (ended) (status ended, or all legs completed)
        var check_game_is_being_played          = false         //

        // Set dates
        const currentdate       = new Date() 
        const match_start       = new Date(this.game.matchID.date_match_start)
        const match_stop        = new Date(this.game.matchID.date_match_stop)
        const register_stop     = new Date(this.game.matchID.date_register_stop)

        // Check the dates
        if (currentdate >= match_start) {
            check_match_start_passed = true
        }
        // console.log('check_match_start_passed', check_match_start_passed)

        if (currentdate >= match_stop) {
            check_match_stop_passed = true
        }
        // console.log('check_match_stop_passed', check_match_stop_passed)

        if (currentdate >= register_stop) {
            check_match_registerstop_passed = true
        }
        // console.log('check_match_registerstop_passed', check_match_registerstop_passed)

        // Check that 4 players are registered at game
        if (count_players === 4) {
            check_four_players_registered = true
        } else {
            check_four_players_registered = false
        }
        // console.log('check_four_players_registered', check_four_players_registered)

        // Check that this user is registered with this game
        for (obj in this.sorted_players) {
            if (this.sorted_players[obj].player.username === this.user.username) {
                check_player_is_registered = true
                this.player_is_registered = true
            }
        }
        // console.log('check_player_is_registered', check_player_is_registered)
        

        // Check Game is not ended , that is Not all legs have been completed (that legs_completed < n_legs)
        // Note legs_completed = 0 implies that 0 legs have been played. 
        check_game_has_not_ended = this.game.legs_completed < this.game.matchID.n_legs
        // console.log('check_game_has_not_ended', check_game_has_not_ended)


        // Check that game has already started and not ended
        check_game_is_being_played = this.game.gameStatus === 'wordt gespeeld'
        // console.log('check_game_is_being_played', check_game_is_being_played)


        // Validate allow to play game (start)
        // This needs to cover starting a new game and resuming a started game
        // Rules for starting a new game:
        // * match_start date has passed
        // ** match_stop date not passed 
        // ------- Not valid ----------------------------------------------// * registerstop date not passed
        // ** 4 players registered at game
        // ** user is a player  of this game
        // ** game has not ended

        // Rules for starting a existing game:
        // ** match_stop date not passed 
        // ** 4 players registered at game
        // ** user is a player  of this game
        // * Game in status wordt gespeeld. (dus ook game has not ended)

        if (check_match_stop_passed ||
                !check_four_players_registered ||
                !check_player_is_registered ||
                !check_game_has_not_ended) {
            this.allow_play_game = false
            // console.log('A', this.game.gameID, check_match_stop_passed, !check_four_players_registered, !check_player_is_registered, !check_game_has_not_ended )
        } else {

            if (check_game_is_being_played) {
                 // Existing game
                this.allow_play_game = true
                // console.log('B', this.game.gameID)
            } else {
                if (!check_match_start_passed ) {
                    this.allow_play_game = false
                    // console.log('C', this.game.gameID, !check_match_start_passed, check_match_registerstop_passed)
                } else {
                    // new game
                    this.allow_play_game = true
                    // console.log('D')
                }
            }  
        }

        // Validate allow to register
        // * match_stop date not passed
        // * match registerstop date not passed
        // * player is not already registered
        // * game has not yet been completed
        if (check_match_stop_passed ||
                check_match_registerstop_passed ||
                check_player_is_registered ||
                !check_game_has_not_ended ) {

            this.allow_register = false
        } else {
            this.allow_register = true
        }
        // console.log('allow_register', this.allow_register)

        // Validate allow to un-register
        // * match_stop date not passed
        // * player is registered with game
        // * game has not yet been completed 
        // if (!check_match_start_passed && check_player_is_registered )  {
        if (check_match_stop_passed ||
                check_match_registerstop_passed ||
                !check_player_is_registered ||
                !check_game_has_not_ended ) {

            this.allow_unregister = false
        } else {
            this.allow_unregister = true
        }
        // console.log('allow_unregister', this.allow_unregister)


        // Validate allow to send mail
        //  * player is registered with game
        if (check_player_is_registered ) {
            this.allow_send_mail = true
        } else {
            this.allow_send_mail = false
        }

         this.isLoaded = true

    },  //END getPlayers

    doRegister: async function (position) {
        // Register a player to a game

        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        // First get the ID of the user, as registered in django
        await api_request({
            method: 'get',
            url: this.appSettings.url_user_details + this.user.username + '/'
            // data: this.input
        })
        .then(response => {
            if (response.status === 200) {
                this.user.id = response.data.id
            }
        })
        .catch(() => {
            // console.log(error.response)
        })

        // Check if there is already a player on this position.
        // if Yes, then delete this player from this position/game
        // // console.log(this.sorted_players[position].player.username)
        var must_delete = false
        if (this.sorted_players[position].player.username !== '--geen speler--') {
            must_delete = true
        } else {
            must_delete = false
        }

        if (must_delete) {
            await api_request({
                method: 'delete',
                url: this.appSettings.url_game_players_rud + this.sorted_players[position].id
                // data: {
                // }
            })
            .then(response => {
                // // console.log('Status RUD player: ',response.status)
                if (response.status === 201) {
                    // console.log(response)
                }
            })
            .catch(() => {
                // console.log('RUD player failed')
                // console.log(error.response)
            })

            // this.$forceUpdate()

        }

        // Next register a player using the user.id
        // at first allow always to register
        // also when game has started. for now no accesptance of partners

        // // console.log(this.game.gameID, this.user.id )

        var data = {
                "position": position,
                "gameID": this.game.gameID,
                "player": this.user.id
            }


        await api_request({
            method: 'post',
            url: this.appSettings.url_game_players_create,
            data: data
            // data: {
            //     position: position,
            //     gameID: this.game.gameID,
            //     player: this.user.id
            // }
        })
        .then(response => {
            // console.log('Status create player: ',response.status)
            if (response.status === 201) {
                // console.log(response)
                let message = 'Potje aanmelden: ' + this.game.matchID.matchID + '/' + this.game.gameID +  '/' + position
                this.logButton(message) 
                message = 'Register to Game: ' + this.game.matchID.matchID + '/' + this.game.gameID +  '/' + position
                this.logAction(message) 
            }
        })
        .catch(() => {
            // console.log('Create player failed')
            // console.log(error.response)
        })

        this.getPlayers()

    },//END doRegister

    doUnRegister: async function () {
        // UnRegister a player to a game

        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        // Determine on which position the user is registered and get the ID
        var id = ''
        for (var obj in this.sorted_players) {
            if (this.sorted_players[obj].player.username === this.user.username) {
                id = this.sorted_players[obj].id
            }
        }

        // Next remove this player from the game
        await api_request({
            method: 'delete',
            url: this.appSettings.url_game_players_rud + id + '/'
            // data: this.input
        })
        .then(response => {
            if (response.status === 204) {
                let message = 'Potje afmelden: ' + this.game.matchID.matchID + '/' + this.game.gameID +  '/'
                this.logButton(message)
                message = 'Unregister to Game: ' + this.game.matchID.matchID + '/' + this.game.gameID +  '/'
                this.logAction(message) 

                // Remove the lock on the game when it is present
                // And store the false value in the database
                if (this.game.locked === true) {
                    this.game.locked = false;
                    this.lockGame(false);
                }

            }
        })
        .catch(() => {
            // console.log(error.response)
        })

        this.getPlayers()

    },//END doUnRegister   

  },  //END methods
  computed: {
    user () {
      return this.$store.state.user
    },
    appSettings () {
      return this.$store.state.appSettings
    }
  }
}
</script>
