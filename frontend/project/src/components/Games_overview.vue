<template>
  <div class="Appgames_overview">

    <b-container v-if="isLoaded">

        <br>
        <h2> Overzicht potjes </h2>

        <hr>
        <b-button v-on:click="gotoMatchesList()"  class="btn btn-secondary"> Terug naar wedstrijdoverzicht  </b-button></b-col>
        <hr>

        <b>Wedstrijdnaam:</b> <span style="color:purple;font-weight:bold;font-size:1.4em"> {{ matchID }} </span>
        <p>
          <b>Status: </b> {{ status_text}}
        </p>
        
        <hr>
        <b-row>
            <b-col><b-button block v-on:click="doCreateGame()" v-if="allow_game_create" class="btn btn-success"> Nieuw potje maken  </b-button></b-col>
            <b-col><b-button block v-on:click="gotoMatchDetails(matchID)" class="btn btn-success"> Bekijk wedstrijddetails  </b-button></b-col>
        </b-row>
        <hr>

        <p> 
          Een nieuw potje kan worden aangemaakt als de registratieperiode nog niet verlopen is.
          Bij een bestaand potje, kan op een spelerpositie worden geklikt om je aan te melden. 
          Druk op de gele knop bij het potje om je weer af te melden.
          Pas als 4 spelers bij een potje zijn aangemeld kan het potje gestart worden. Klik op de balk van 
          een potje om de score en gespeelde slagen te zien.
        </p>

        <hr>

        <div v-for="game in games" v-bind:key="game.gameID" >
            <b-button v-if="game.gameStatus === 'uitgespeeld'"  @click="gotoGameScore(game.gameID)" block class="btn btn-danger"> Potje met ID = {{ game.gameID }}  </b-button>
            <b-button v-else @click="gotoGameScore(game.gameID)" block class="btn btn-info"> Potje met ID = {{ game.gameID }}  </b-button>

            <b-row>
                <b-col><strong>Rondes: </strong> {{ game.legs_completed }} / {{ game.matchID.n_legs }}</b-col>
                <b-col> <span style="color:blue;font-weight:bold;font-size:1.0em"> {{  game.gameStatus }} </span></b-col> 
            </b-row>
            <b-row>
                <b-col><strong>Potje gestart: </strong> {{  game.date_game_start }} </b-col> 
            </b-row>
            <b-row>
                <b-col><strong>Potje gestopt: </strong> {{ game.date_game_end }} </b-col>
            </b-row>
            <div v-if="game.gameStatus === 'uitgespeeld'">
              <b-row>
                  <b-col><strong>Score team A:</strong> {{ game.scoreA }} + {{ game.roemA }} = {{ game.scoreA  + game.roemA}} </b-col>
              </b-row>
              <b-row>
                  <b-col><strong>Score team B:</strong> {{ game.scoreB }} + {{ game.roemB }} = {{ game.scoreB  + game.roemB}} </b-col>
              </b-row>
            </div>

            <keep-alive>
              <app-gamedetails
                  v-if="isLoaded"
                  v-bind:game="game"
              ></app-gamedetails>
            </keep-alive>

             <hr>
        </div>

  
        <b-button v-on:click="gotoMatchesList()"  class="btn btn-secondary"> Terug naar wedstrijdoverzicht  </b-button></b-col>
        <hr>

    </b-container>

  </div>
</template>

<script>
import Appgamedetails from '../components/Game_details.vue'


export default {
  name: 'Appgamesoverview',
  components: {
    'app-gamedetails': Appgamedetails
  },
  data () {
    return {
        title: 'Game details page',
        polling: null,            // Needed to auto refresh this page
        isLoaded: false,          // to rerender the page when data is loaded
        matchID: '',              // Contains the matchID as received from the match list
        status_color: '',         // Contains the  color indicator of the match
        status_text: '',          // Describes the status of the match
        match_details: '',        // Contains the details of the match
        games: '',
        allow_game_create: false,
        test: '',
        errors: {},
        game_score: [
          [],
          [0,0,0,0]
        ],           // Store the score data fo the game
        show_game_score: false,   // variable to show the game score
        gameID_to_show: 0,        // 
    }
  },
  deactivated () {
    // To stop refreshing the data when the page is left
    clearInterval(this.polling)
  },

  // Do not use mounted, otherwise no new game will be loaded
  activated: async function () {
      // To refresh the page every x seconds
      this.pollData()

      document.title = 'Klaverjasfun'
      // console.log(this.$route.name)
      // Do not show full screen on login page
      // document.exitFullscreen();
      if (this.user.user_is_logged_in === false) {

            this.$router.push({ name: 'Home' })

      } else {

          //Check that screen is mobile. If so, set full screen
          var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
          if (isMobile) {
            // document.body.requestFullscreen()
            document.documentElement.requestFullscreen()
          }

          // When coming to this screen via potjes, then no parameter is send.
          if (this.$route.params.matchID) {
            this.matchID = this.$route.params.matchID;
          }
          if (this.$route.params.status_color) {
            this.status_color = this.$route.params.status_color;
            if (this.status_color === 'success') {
              this.status_text = 'Groen - wedstrijd is gestart en nog niet gestopt. Registratie mag nog plaatsvinden. \
                                Spelers mogen potjes aanmaken, potjes starten en zich aan/af melden bij een potje.'
            }
            if (this.status_color === 'danger') {
              this.status_text = 'Rood - wedstrijd is gestopt. \
                                Spelers mogen geen potjes meer aanmaken of zich aan/af melden bij een potje. \
                                Potjes mogen niet meer gestart worden. \
                                Spelers van buiten dit potje mogen de gespeelde slagen inzien.'
            }
            if (this.status_color === 'secondary') {
              this.status_text = 'Grijs - wedstrijd is nog niet gestart, registratie mag niet meer plaatsvinden. \
                                Spelers mogen geen potjes aanmaken, zich aan- of afmelden bij een potje of een potje starten om te spelen. \
                                Wel mag een reeds gestart potje worden uitgespeeld.'
            }
            if (this.status_color === 'primary') {
              this.status_text = 'Blauw - wedstrijd is nog niet gestart, registratie bij een potje mag nog plaatsvinden. \
                                Spelers mogen potjes aanmaken, zich aan- en afmelden bij een potje. \
                                Nieuwe potjes mogen (nog) niet gestart worden om te spelen. \
                                Wel mag een reeds gestart potje worden uitgespeeld.'
            }
            if (this.status_color === 'warning') {
              this.status_text = 'Geel -  wedstrijd is gestart en nog niet gestopt. Registratie mag niet meer plaatsvinden. \
                                Spelers mogen geen potjes aanmaken of zich aan/af melden bij een potje. \
                                Wel mag een potje gestart worden om te spelen.'
            }
          }

          // Get the match details
          await this.getMatchDetails(this.matchID)
      
          this.user.show_header = true
          this.$store.dispatch('updateUser', this.user)

          //******************************************************************************
          // Validate allow to make new game
          //  * match-stop not passed
          //  * register-stop not passed
        
          // initialize parameters
          let check_match_stop_passed             = false
          let check_match_registerstop_passed     = false

          const currentdate       = new Date() 
          const match_stop        = new Date(this.match_details.date_match_stop)
          const register_stop     = new Date(this.match_details.date_register_stop)

          if (currentdate >= match_stop) {
            check_match_stop_passed = true
          }

          if (currentdate >= register_stop) {
            check_match_registerstop_passed = true
          }

          if (check_match_stop_passed || check_match_registerstop_passed) {
            this.allow_game_create = false
          } else {
            this.allow_game_create = true
          }

          // @Extra validation: do not allow to create a new game when there is already an empty game.
          // Do not do this, because a game can get fully un-registered but already mails have been send.

          //************************************************************************************ 

          this.game_score = [
            [],
            [0,0,0,0]
          ],
          this.show_game_score = false
          this.gameID_to_show = 0

          this.getGames()
          // this.testgetPlayers()

      }//END if
  },//END mounted
  methods: {
    pollData () {
      // To refresh the data every x seconds
      // https://renatello.com/vue-js-polling-using-setinterval/
      this.polling = setInterval(() => {
        this.getGames()
      }, 5000)
    },
    doLoad: function () {
      this.getGames()
    },

    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    },  //END gotoLogin
    gotoMatchesList: function () {
      this.$router.push({ name: 'Match_list' })
    },  //END gotoMatches
    gotoMatchDetails: function (id) {
      this.$router.push({ name: 'Match_details', params: {id} })
    },
    gotoGameScore: function (gameID) {
      this.$router.push({ name: 'Game_score', params: {gameID: gameID} })
    },
    doHideElement: function (id) {
        var x = document.getElementById(id);
        x.style.display = "none";
    },
    doShowElement: function (id) {
        var x = document.getElementById(id);
        x.style.display = "block";
    },

    getMatchDetails: async function (matchID) {
        // Based on the matchID get the details of the match
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        // console.log('DUMMY1')

        await api_request({
            method: 'get',
            url: this.appSettings.url_match_details + matchID + '/',
            // data: this.input
        })
        .then(response => {
            // // console.log('Status get match details: ',response.status)
            if (response.status === 200) {
                this.match_details = response.data
            }
        })
        .catch(() => {
            // console.log('Get match details failed')
            // console.log(error.response)
        })

    },  //END getMatchDetails

    getGames: async function () {
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        await api_request({
            method: 'get',
            url: this.appSettings.url_games_list + 'matchID=' + this.match_details.matchID
            // data: this.input
        })
        .then(response => {
            // // console.log('Status get game overview: ',response.status)
            if (response.status === 200) {
                this.games = response.data
                // // console.log(this.games.hasAttribute("player"))
                this.isLoaded = true

                // // console.log('DUMMY1')
                // // console.log(this.games)

                // Check that games contains info
                // if (this.games.length !== 0) {
                //   // console.log('games not empty')
                // } else {
                //   // console.log('games are empty')
                // }
            }
        })
        .catch(() => {
            // console.log('Get match details failed')
            // console.log(error.response)
        })

        this.$forceUpdate()

    },  //END getGames

    doGetScores: async function (gameID) {
        // Show the current score of the game

       // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        this.gameID_to_show = gameID

        // console.log('gameID = ', this.gameID_to_show, gameID)


        // Get all the players of a match
        await api_request({
            method: 'get',
            url: this.appSettings.url_game_score + 'gameID=' + gameID 
            // data: this.input
        })
        .then(response => {
            if (response.status === 200) {
                this.game_score = response.data
                // // console.log(this.test)
            }
        })
        .catch(() => {
            // console.log('Get game score failed')
            // console.log(error.response)
        })

        this.show_game_score = true
        // console.log('doGetScores', this.game_score)

    }, //END doGetScores

    filterTest: function (item) {
      return item.gameID.gameID === 3
    },

    testgetPlayers: async function () {
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')


        // Get all the players of a match
        await api_request({
            method: 'get',
            url: this.appSettings.url_game_players + 'matchID=' + this.match_details.matchID 
            // data: this.input
        })
        .then(response => {
            // // console.log('Status get game overview: ',response.status)
            if (response.status === 200) {
                this.test = response.data
                // // console.log(this.test)
            }
        })
        .catch(() => {
            // console.log('Get match details failed')
            // console.log(error.response)
        })

        // // console.log(this.test.filter(this.filterTest).length)

        // test a filter on the result


    },  //END getPlayers
    doCreateGame: async function () {
        // Create a new game
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        await api_request({
            method: 'post',
            url: this.appSettings.url_games_create,
            data: {
              matchID: this.match_details.matchID 
            }
        })
        .then(response => {
            // // console.log('Game created: ',response.status)
            if (response.status === 201) {
              // alert('new game is created')
              this.getGames()
            }
        })
        .catch(() => {
            // console.log('Get match details failed')
            // console.log(error.response)
        })



    }//END doCreateGame
       
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


