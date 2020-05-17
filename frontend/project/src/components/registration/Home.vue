<template>
  <div class="Apphome">

    <!-- Only show button when user is not logged in -->
     <div v-if="user.user_is_logged_in === false">
      <br><br>
      <div class="container col-xl-4 col-lg-6" >
          <button  v-on:click="gotoLogin()" class="btn btn-primary"> Ga naar Login pagina  </button>
      </div>
     </div>

    <!-- When user is logged in show the contents of the home page.
    The base of the home page is a container -->
    <div v-else>
    <b-container>

      <br>
      <h2>Start</h2>

      <div>
        <b-button v-on:click="gotoMatches" block variant="info">Ga naar wedstrijden</b-button>
        <!-- <b-button v-on:click="gotoChat" block variant="info">test chat</b-button> -->
        <!-- <b-button v-on:click="gotoViezePlaatjes" block variant="info">hele vieze plaatjes</b-button> -->
        <b-button v-on:click="gotoInfo" block variant="info">Toelichting</b-button>
      </div>

    <br>
    <hr>
      <!-- <button  v-on:click="doTest()" class="btn btn-primary"> Test request  </button>
      {{ result_test }} -->

      <br><br>
      <!-- <button  v-on:click="getWindowSize()" class="btn btn-primary"> Get window size  </button> -->
      <!-- <p>Current windowsize is {{ window_size.width }}, {{ window_size.height }} </p> -->

    </b-container>
    </div>



  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Apphome',
  data () {
    return {
      title: 'Login page',
      test: {},
      result_test: {}
    }
  },
  activated: function () {
    document.title = 'Klaverjasfun'
    // console.log(this.$route.name)

    if (this.user.user_is_logged_in === false) {
      // there may be a valid refresh token stored in localStore
      // Do a request so that the refresh token is used to get an access token
      this.checkRefreshValid()

    } else {
      this.user.show_header = true
      this.$store.dispatch('updateUser', this.user)
      // document.body.requestFullscreen()
    } //END if-else

  },  //END mounted
  methods: {
    doToggleLogout: function () {
      // No relevant function anymore
      var x = document.getElementById("myDIV");
      if (x.style.display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      } //END if-else
    },  //END doToggleLogout
    gotoLogin: function () {
      this.$router.push({ name: 'Login' })
    },  //END gotoLogin
    gotoChat: function () {
      this.$router.push({ name: 'Chat' })
    },  //END gotoChat
    gotoMatches: function () {
      this.$router.push({ name: 'Matches' })
    },  //END gotoMatches
    gotoInfo: function () {
      this.$router.push({ name: 'Info' })
    },  //END gotoInfo
    gotoViezePlaatjes: function () {
      // alert("Dacht ik wel...  teller + 1 is doorgestuurd")
      alert("Deze dienst kost EUR 50,00 per maand. U bent aangemeld.")
    },  //END gotoViezePlaatjes
    checkRefreshValid: async function () {
      // Create api call that will not use the interceptors
      const axios = require('axios')
      const api_call = axios.create()

      const refresh_token = localStorage.getItem('refresh-token')
      // // console.log('initial access token', localStorage.getItem('access-token'))
      // // console.log('initial refresh token', localStorage.getItem('refresh-token'))

      await api_call({
          method: 'post',
          url: this.appSettings.url_refresh_token,
          data: {
              refresh: refresh_token
          }
      })
          .then(response => {
              if (response) {
                // // console.log(response)
                // // console.log('new access token: ', response.data.access)
              }
              this.user.user_is_logged_in = true
              // Get the user from localstore
              this.user.username = localStorage.getItem('username')
              this.$store.dispatch('updateUser', this.user)

              // Store token parameters in localStore
              localStorage.setItem('access-token', response.data.access)
          })
          .catch( () => {
              // console.log(error)
              // User needs to be redirected to Login page
              // This is done by the interceptor
              // console.log('Could not refresh the token')
          })
    },  //END checkRefreshValid
    // getWindowSize: function () {
    //   this.window_size.width = window.innerWidth
    //   || document.documentElement.clientWidth
    //   || document.body.clientWidth;

    //   this.window_size.height = window.innerHeight
    //   || document.documentElement.clientHeight
    //   || document.body.clientHeight;

    //   // // console.log(this.window_size)

    //   this.$store.dispatch('updateWindow_size', this.window_size)

    // },  //END GetWindowSize
    doTest: async function () {
      const api_request = require('axios')
      this.result_test = 'Nieuwe gegevens ophalen'

      await api_request({
          method: 'post',
          url: this.appSettings.url_test,
          data: {
          }
      })
          .then(response => {
              this.result_test = [response.status]
              // console.log('doTest: ', response.status)
          })
          .catch(error => {
              if (error.response) {
                this.result_test = ['Error in response']
                // console.log('doTest: ', error)
              } else {
                // console.log('Test failed')
              }
          })
    },  //END doTest
  },  //END methods
  computed: {
    user () {
      return this.$store.state.user
    },
    appSettings () {
      return this.$store.state.appSettings
    },
    window_size () {
      return this.$store.state.window_size
    }
  }
}
</script>
