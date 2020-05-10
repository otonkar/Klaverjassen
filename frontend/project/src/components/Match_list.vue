<template>
  <div class="Appmatch_list">

    <b-container>

      <br>
      <h2>Overzicht wedstrijden</h2>

      <hr>
      <button  v-on:click="gotoMatches()" class="btn btn-secondary"> Terug naar wedstrijd pagina  </button>
      <hr>
      <!-- <button  v-on:click="$router.go(-1)" class="btn btn-primary"> Ga naar home pagina  </button> -->
      <br>

      <div v-for="item in match_list" v-bind:key="item.matchID">
    
        <!-- <b-button v-on:click="gotoMatchDetails(item.matchID)" block v-bind:variant="item.status_color">{{ item.matchID }} ({{ item.owner.username }})</b-button> -->
        <b-button v-on:click=" gotoGamesOverview(item.matchID)" block v-bind:variant="item.status_color">{{ item.matchID }} ({{ item.owner.username }})</b-button>

        <br>

      </div>

      

    </b-container>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Appmatchlist',
  data () {
    return {
      title: 'Match list page',
      test: {},
      match_list: {},
      result_test: {},
      match_color: '',          // Color to show
    }
  },
  activated: function () {
      // console.log(this.$route.name)
      // Do not show full screen on login page
      // document.exitFullscreen();
      if (this.user.user_is_logged_in === false) {
          this.$router.push({ name: 'Home' })
      } else {
          this.user.show_header = true
          this.$store.dispatch('updateUser', this.user)
          this.getMatchList()
      }//END if
  },//END mounted
  methods: {
    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    },  //END gotoLogin
    gotoMatches: function () {
      this.$router.push({ name: 'Matches' })
    },  //END gotoMatches
    gotoMatchDetails: function (id) {
      this.$router.push({ name: 'Match_details', params: {id} })
    },
    gotoGamesOverview: function (matchID) {
      // goto to new page and send 1 or more parameters in a params object
        this.$router.push({ name: 'Games_overview', params: { matchID: matchID } })
    }, //END gotoGamesOverview 
    getMatchList: function () {
      // make sure the request  WILL use the interceptors
      const api_request = require('axios')

      api_request({
          method: 'get',
          url: this.appSettings.url_match_list,

      })
        .then(response => {
            if (response) {
            //   // console.log(response)
              // // console.log('new access token: ', response.data.access)
            }

            // Store the matches in localStore
            this.match_list = response.data
            // // console.log('***', this.match_list)


            localStorage.setItem('match_list', response.data)
        })
        .catch(() => {
            // console.log(error)
            // User needs to be redirected to Login page
            // This is done by the interceptor
            alert('Fout bij het ophalen van de wedstrijdlijst')
            // console.log('Fout bij het ophalen van de wedstrijdlijst')
        })

    }
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
