<template>
  <div class="Appgames_score">

    <b-container v-if="isLoaded" >

        <br>
        <h2>Score game {{ gameID }} </h2>
        <hr>

        <b-row>
            <b-col><b-button block v-on:click="goBack()"  class="btn btn-secondary"> Terug  </b-button></b-col>
            <b-col></b-col>
        </b-row>
        <br>
        <p>Klik op de ronde om de gespeelde slagen te zien</p>

        <div class="Table">
            <b-table-simple small caption-top responsive>
                
                <colgroup><col></colgroup>
                <colgroup><col><col></colgroup>
                <colgroup><col><col></colgroup>
                <b-thead head-variant="light">
                <b-tr >
                    <b-th colspan="1" ></b-th>
                    <b-th colspan="2" variant="">Team A</b-th>
                    <b-th colspan="2">Team B</b-th>
                </b-tr>
                <b-tr >
                    <b-th>Ronde</b-th>
                    <b-th variant="">Score</b-th>
                    <b-th variant="">Roem</b-th>
                    <b-th>Score</b-th>
                    <b-th>Roem</b-th>
                </b-tr>
                </b-thead>
                <b-tbody >
                    <b-tr @click="showSlagen(gameID, leg.leg)" v-for="leg in game_score[0]" v-bind:key="leg.leg">
                    <b-th variant="light"> {{ leg.leg + 1  }} </b-th>
                    <b-th variant="light"> {{ leg.scoreA }} </b-th>
                    <b-th variant="light"> {{ leg.roemA }} </b-th>
                    <b-td variant="light"> {{ leg.scoreB }} </b-td>
                    <b-td variant="light"> {{ leg.roemB }} </b-td>
                    </b-tr>
                </b-tbody>
                <b-tfoot>
                <b-tr>
                    <b-th>Totaal</b-th>
                    <b-th variant="warning"> {{ game_score[1][0] }} </b-th>
                    <b-th variant="warning"> {{ game_score[1][1] }} </b-th>
                    <b-td variant="warning"> {{ game_score[1][2] }} </b-td>
                    <b-td variant="warning"> {{ game_score[1][3] }} </b-td>
                    
                </b-tr>
                </b-tfoot>
            </b-table-simple>
        </div>

        <keep-alive>
          <app-gameslagen
              v-if="variables.show_slagen"
              v-bind:gameID="gameID_to_show"
              v-bind:leg="leg_to_show"
          ></app-gameslagen>
        </keep-alive>

            <!-- v-bind:leg="this.leg_to_show" -->

            <!-- <b-td variant="success"> <img src="./clubs.png" width="17px"> A  </b-td> -->

    </b-container >

  </div>
</template>

<script>
import Appgameslagen from '../components/Games_slagen.vue'



export default {
  name: 'Appgamesscore',
  components: {
    'app-gameslagen': Appgameslagen
  },

  data () {
    return {
        title: 'Game details page',
        isLoaded: false,            // to rerender the page when data is loaded
        errors: {},
        game_score: [
          [],
          [0,0,0,0]
        ],                          // Store the score data fo the game
        gameID: 0,  
        gameID_to_show: 0,
        leg_to_show: 0 
    }
  },

  // Do not use mounted, otherwise no new game will be loaded
  activated: async function () {
      // console.log(this.$route.name)
      // Do not show full screen on login page
      // document.exitFullscreen();
      if (this.user.user_is_logged_in === false) {

            this.$router.push({ name: 'Home' })

      } else {

          // When coming to this screen via potjes, then no parameter is send.
          if (this.$route.params.gameID) {
            this.gameID = this.$route.params.gameID;
          }

          // Get the match details
          await this.doGetScores(this.gameID)
      
          this.user.show_header = true
          this.$store.dispatch('updateUser', this.user)

          this.isLoaded = true

      }//END if
  },//END activated

  methods: {

      goBack: function () {
        this.variables.show_slagen = false
        this.$store.dispatch('updateVariables', this.variables)
        this.$router.go(-1)
    },  //END goBack

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

    showSlagen: function (gameID, leg) {

      // this.variables.show_slagen = false
      // this.$store.dispatch('updateVariables', this.variables)

      // // Create an event to another component so that slagen will be updated
    
      this.gameID_to_show = gameID
      this.leg_to_show = leg

      // console.log(this.gameID_to_show,this.leg_to_show  )

      // console.log('Before emit', this.leg_to_show)
      this.$root.$emit('changeLeg', this.leg_to_show);

      this.variables.show_slagen = true
      this.$store.dispatch('updateVariables', this.variables)

    }, //END gotoSlagen
       
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
    }
  }
}
</script>

<style scoped lang='scss'>

.Table {
    background-color: white;
}


</style>
