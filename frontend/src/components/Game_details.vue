<template>
  <div class="Appgame_details">

    <b-container v-if="isLoaded">

        <!-- <div v-for="player in sorted_players" v-bind:key="player.id"> 
            {{ player.position }}: {{ player.id }} , {{ player.player.username }} 

        </div>
        <br> -->

        <b-row v-if="allow_start_game">
            <!-- <b-col ><b-button block class="btn btn-warning"> Accepteer partner </b-button> </b-col>  -->
            <b-col></b-col>
            <b-col ><b-button @click="playGame(game, players)"  class="btn btn-success"> speel dit potje  </b-button> </b-col> 
        </b-row>

        <br>
        <b-card  class="bg-secondary text-center">
        <b-row>
            <b-col ><b-button @click="doRegister(0)" v-bind:disabled="!allow_register" block class="btn btn-light"> A: {{  sorted_players[0].player.username }} </b-button> </b-col> 
            <b-col ><b-button @click="doRegister(1)" v-bind:disabled="!allow_register" block class="btn btn-dark"> B: {{  sorted_players[1].player.username }} </b-button> </b-col> 
        </b-row>
        <br>
        <b-row>
            <b-col ><b-button @click="doRegister(3)" v-bind:disabled="!allow_register" block class="btn btn-dark"> B: {{  sorted_players[3].player.username }} </b-button> </b-col> 
            <b-col ><b-button @click="doRegister(2)" v-bind:disabled="!allow_register" block class="btn btn-light"> A: {{  sorted_players[2].player.username }} </b-button> </b-col> 
        </b-row>
        </b-card>

        <br>
        <!-- <div class="col text-center">
        <b-button class="btn btn-warning"> Accepteer partner </b-button>
        </div> -->

        <b-row>
            <!-- <b-col ><b-button block class="btn btn-warning"> Accepteer partner </b-button> </b-col>  -->
            <b-col ><b-button @click="doUnRegister()" v-bind:disabled="allow_register" block class="btn btn-danger"> Afmelden bij potje  </b-button> </b-col> 
            <b-col> <b-col><b-button block v-on:click="doRefresh()"  class="btn btn-warning"> Refresh  </b-button></b-col> </b-col> 
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
        isLoaded: false,
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
        allow_register: false,       // indicate that you are allowed to register at a game
        allow_start_game: false,
        errors: {}
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
  beforeMount: function () {
    //   this.sorted_players.position = ''
    //   this.sorted_players.player.username = ''
  },
  activated: function () {
      // console.log(this.$route.name)
      // Do not show full screen on login page
      // document.exitFullscreen();
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
    doRefresh: function () {
        this.getPlayers()
    }, //END doRefresh

    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    },  //END gotoLogin
    playGame: function (game, players) {
        this.$router.push({ name: 'Game_play', params: { 'game': game, 'players': players} })
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
            // // console.log('Status get game overview: ',response.status)
            if (response.status === 200) {
                this.players = response.data
                // console.log(this.game.matchID.matchID, this.game.gameID)
                // console.log('getPlayers in Details ', this.players)
            }
        })
        .catch(() => {
            // console.log('Get match details failed')
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
            // // console.log(this.players[obj])
            // // console.log(this.players[obj].position)
        }

        // // console.log('Counted players :', count_players)

        // Check that there were 4 players registered at this game
        this.allow_start_game = false
        if (count_players === 4) {
            // @ check that logged in player is part of the game
            for (obj in this.sorted_players) {
                if (this.sorted_players[obj].player.username === this.user.username) {
                    this.allow_start_game = true
                }
            }
        }
        // AND check that legs_completed < n_legs
        // Note legs_completed = 0 implies that 0 legs have been played. 
        this.allow_start_game = this.allow_start_game && (this.game.legs_completed < this.game.matchID.n_legs )

        // AND check that match_stop date has not been passed
        // When already started the game is allowed to finish 
        // But is allowed when game has already started
        const currentdate = new Date() 
        const match_stop = new Date(this.game.matchID.date_match_stop)
        var allow = currentdate < match_stop
        // console.log(currentdate, match_stop, allow)
        // console.log(this.game)

        // Check that game has already started
        var allow1 = this.game.gameStatus === 'wordt gespeeld'
        
        this.allow_start_game = this.allow_start_game && (allow || allow1)

        // console.log('allow1 ',this.game.gameID, this.game.gameStatus, allow1, this.allow_start_game)








        // Determine that person is not already registered at this game
        // Filter the players based on name of current user.
        // // console.log(this.sorted_players[0].player.username)
        // // console.log(this.sorted_players.filter(this.filterOnUsername).length)

        if (this.sorted_players.filter(this.filterOnUsername).length === 0) {
            this.allow_register = true
        } else {
            this.allow_register = false
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
            url: this.appSettings.url_user_details + this.user.username 
            // data: this.input
        })
        .then(response => {
            // // console.log('Status get user id: ',response.status)
            if (response.status === 200) {
                this.user.id = response.data.id
                // // console.log(response.data.id)
            }
        })
        .catch(() => {
            // console.log('Get userdetails failed')
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


        await api_request({
            method: 'post',
            url: this.appSettings.url_game_players_create,
            data: {
                position: position,
                gameID: this.game.gameID,
                player: this.user.id
            }
        })
        .then(response => {
            // console.log('Status create player: ',response.status)
            if (response.status === 201) {
                // console.log(response)
            }
        })
        .catch(() => {
            // console.log('Create player failed')
            // console.log(error.response)
        })

        this.getPlayers()

    },//END doRegister

    doUnRegister: async function () {
        // Register a player to a game

        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        // Determine on which position the user is registered and get the ID
        var id = ''
        for (var obj in this.sorted_players) {
            if (this.sorted_players[obj].player.username === this.user.username) {
                id = this.sorted_players[obj].id
                // // console.log(this.sorted_players[obj].player.username, this.sorted_players[obj].id )
            }
        }

        // // console.log('GamePlayer ID = ', id)

        // Next remove this player from the game
        await api_request({
            method: 'delete',
            url: this.appSettings.url_game_players_rud + id + '/'
            // data: this.input
        })
        .then(response => {
            // console.log('Status delete player: ',response.status)
            // // console.log(response)
            if (response.status === 200) {
                // // console.log(response.data.id)
            }
        })
        .catch(() => {
            // console.log('Delete player failed')
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
