<template>
  <div class="Appgames_overview">

    <b-container v-if="isLoaded">

        <br>
        <h2> Overzicht potjes </h2>
        Voor de wedstrijd: <span style="color:purple;font-weight:bold;font-size:1.4em"> {{ matchID }} </span>
        <hr>

        <b-row>
            <b-col><b-button block v-on:click="gotoMatchesList()"  class="btn btn-secondary"> Terug  </b-button></b-col>
            <b-col></b-col>
            <!-- <b-col><b-button block v-on:click="doLoad()"  class="btn btn-warning"> Refresh  </b-button></b-col> -->
            <!-- <b-col><b-button block v-on:click="gotoMatchesList()" class="btn btn-success"> Naar potjes  </b-button></b-col> -->
        </b-row>
        <br>

        <b-row>
            <b-col><b-button block v-on:click="doCreateGame()" v-if="allow_game_create" class="btn btn-success"> Nieuw potje maken  </b-button></b-col>
            <b-col><b-button block v-on:click="gotoMatchDetails(matchID)" class="btn btn-success"> Wedstrijd details  </b-button></b-col>
        </b-row>
        <br>


        <!-- <div class="col text-center">
            <b-button  v-on:click="doCreateGame()" v-if="allow_game_create" class="btn btn-success"> Nieuw potje maken  </b-button>
        </div> -->

        <br>
        <p> 
          Er kan een nieuw potje worden aangemaakt. <br> 
          Bij een bestaand potje, kan op een spelerpositie worden geklikt. Je meldt je daarmee aan op die positie. 
          Druk op de rode knop bij het potje om je weer af te melden.
          Pas als 4 spelers bij een potje zijn aangemeld kan het potje gestart worden.
        </p>

        <hr>
        <!-- <button  v-on:click="gotoMatchesList()" class="btn btn-secondary"> Terug  </button> -->

        <div v-for="game in games" v-bind:key="game.gameID" >
            <b-button v-if="game.gameStatus === 'uitgespeeld'"  @click="gotoGameScore(game.gameID)" block class="btn btn-danger"> Potje met ID = {{ game.gameID }}  </b-button>
            <b-button v-else @click="gotoGameScore(game.gameID)" block class="btn btn-info"> Potje met ID = {{ game.gameID }}  </b-button>

            <b-row>
                <b-col><strong>Rondes: </strong> {{ game.legs_completed }} / {{ game.matchID.n_legs }}</b-col>
                <b-col> <span style="color:blue;font-weight:bold;font-size:1.0em"> {{  game.gameStatus }} </span></b-col> 
            </b-row>
            <!-- <b-row>
                <b-col> <strong>Afgeronde rondes: </strong> {{ game.legs_completed }} / {{ game.matchID.n_legs }}</b-col> 
                <b-col> , slag: {{ game.rounds_completed }} /8  </b-col>
            </b-row> -->
            <b-row>
                <b-col><strong>Datum potje gestart: </strong> {{  game.date_game_start }} </b-col> 
            </b-row>
            <b-row>
                <b-col><strong>Datum potje gestopt: </strong> {{ game.date_game_stop }} </b-col>
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

          // When coming to this screen via potjes, then no parameter is send.
          if (this.$route.params.matchID) {
            this.matchID = this.$route.params.matchID;
          }

          // Get the match details
          await this.getMatchDetails(this.matchID)
      
          this.user.show_header = true
          this.$store.dispatch('updateUser', this.user)

          // Check that Registration is still open. 
          // only show create game button when this is allow_game_create = true
          // Do Check that there are no games empty when pressing the button
          const currentdate = new Date() 
          const register_stop = new Date(this.match_details.date_register_stop)

          if (currentdate < register_stop) {
              this.allow_game_create = true
          } else {
            this.allow_game_create = false
          }

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
