<template>
  <div class="Appmatch_list">

    <b-container>

      <br>
      <h2>Overzicht wedstrijden</h2>
      <!-- {{ filterStatus }}
      {{ match_list}} -->

      <hr>
      <button  v-on:click="gotoMatches()" class="btn btn-secondary"> Terug naar wedstrijd pagina  </button>
      <hr>
      <!-- <input type="text" v-model="filterName" placeholder="Filter By Name"/> -->
      <!-- <button  v-on:click="$router.go(-1)" class="btn btn-primary"> Ga naar home pagina  </button> -->

      <h5>Filter op wedstrijden</h5>
      <p>
        Om de lengte van de lijst gevonden wedstrijden in te perken kunt u filters gebruiken.
      </p>
      <!-- <div>
        <b-form inline>
          <label class="sr-only" for="inline-form-input-name">Name</label>
          <b-form-input
            v-model="filterName"
            id="filterName"
            class="mb-1 mr-sm-2 mb-sm-0"
            placeholder="Wedstrijdnaam"
          ></b-form-input>

          <label class="sr-only" for="inline-form-input-name">Owner</label>
          <b-form-input
            v-model="filterOwner"
            id="filterOwner"
            class="mb-1 mr-sm-2 mb-sm-0"
            placeholder="Eigenaar wedstrijd"
          ></b-form-input>

          <b-form-select
            id="filterStatus"
            v-model="filterStatus"
            :options="match_statusses"
            required
        ></b-form-select>

        </b-form>
      </div> -->

      <div>
        <b-form>
          <b-form-input
            v-model="filterName"
            id="filterName"
            placeholder="Wedstrijdnaam"
          ></b-form-input>

          <b-form-input
            v-model="filterDescription"
            id="filterDescription"
            placeholder="Omschrijving wedstrijd"
          ></b-form-input>

          <b-form-input
            v-model="filterOwner"
            id="filterOwner"
            placeholder="Eigenaar wedstrijd"
          ></b-form-input>

          <b-form-select
            id="filterStatus"
            v-model="filterStatus"
            :options="match_statusses"
            required
        ></b-form-select>

        </b-form>
      </div>

      <br>

       <button  v-on:click="clearFilters()" class="btn btn-secondary"> Verwijder filters  </button>


      <hr>
      <h4>Gevonden wedstrijden</h4>
      <br>

      <div v-for="item in filterMatches" v-bind:key="item.matchID">
    
        <!-- <b-button v-on:click="gotoMatchDetails(item.matchID)" block v-bind:variant="item.status_color">{{ item.matchID }} ({{ item.owner.username }})</b-button> -->
        <b-button v-on:click=" gotoGamesOverview(item.matchID, item.status_color)" block v-bind:variant="item.status_color">{{ item.matchID }} ({{ item.owner.username }})</b-button>
        <b>Omschrijving: </b> {{item.description | shorten(600)}}
        <br><br>

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
      match_list: [],
      result_test: {},
      match_color: '',          // Color to show
      filterName:'',             // used to filter on name of match
      filterOwner: '',          // used to filter on owner of match
      filterStatus: '',
      filterDescription: '',
      match_statusses: [
        {'text': 'Geen filter op status', 'value': ''},
        {'text': 'Status blauw', 'value': 'primary'},
        {'text': 'Status geel', 'value': 'warning'},
        {'text': 'Status grijs', 'value': 'secondairy'},
        {'text': 'Status groen', 'value': 'success'},       
        {'text': 'Status rood', 'value': 'danger'},
      ]
    }
  },
  activated: function () {
      // console.log(this.$route.name)
      // Do not show full screen on login page
      // document.exitFullscreen();
      if (this.user.user_is_logged_in === false) {
          this.$router.push({ name: 'Home' })
      } else {
          // make full screen on mobile/tablet
          var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
          if (isMobile) {
            // document.body.requestFullscreen()
            document.documentElement.requestFullscreen()
          }
          
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
    gotoGamesOverview: function (matchID, status_color) {
      // goto to new page and send 1 or more parameters in a params object
        this.$router.push({ name: 'Games_overview', params: { matchID: matchID, status_color:status_color } })
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

    },
    filterByName: function(matches) {
      return matches.filter(match => match.matchID.toLowerCase().includes(this.filterName.toLowerCase()) ? match : '' );
    },
    filterByOwner: function(matches) {
      return matches.filter(match => match.owner.username.toLowerCase().includes(this.filterOwner.toLowerCase()) ? match : '' );
    },
    filterByStatus: function(matches) {
      return matches.filter(match => match.status_color.toLowerCase().includes(this.filterStatus.toLowerCase()) ? match : '' );
    },
    filterByDescription: function(matches) {
      return matches.filter(match => match.description.toLowerCase().includes(this.filterDescription.toLowerCase()) ? match : '' );
    },
    clearFilters: function(){
      this.filterName = ''
      this.filterOwner = ''
      this.filterStatus = ''
      this.filterDescription = ''
    }
  },  //END methods
  filters: {
    shorten: function (text, size){

      if (!text) return '';

      text = text.toString();

      if (text.length <= size) {
        return text;
      }
      return text.substr(0, size) + '...';

    }

  }, //END filter
  computed: {
    user () {
      return this.$store.state.user
    },
    appSettings () {
      return this.$store.state.appSettings
    },
    filterMatches: function(){
      return this.filterByName( this.filterByOwner( this.filterByStatus(this.filterByDescription(this.match_list))) )
    }
  }
}
</script>
