<template>
  <div class="Apphome">

    <!-- Only show button when user is not logged in -->
     <div v-if="user.user_is_logged_in === false">
        <b-container>
          <br><br>
          <div class="container col-xl-4 col-lg-6" >
              <button  v-on:click="gotoLogin()" class="btn btn-primary"> Ga naar Login pagina  </button>
          </div>
          <br><br>
          <h3>Disclaimer</h3>
          <p>
            Deze site betreft een persoonlijk project om ervaring op te doen met het maken van een spel. <br>
            De opzet was om dit spel op afstand met een eigen groep vrienden te spelen in de Corona periode. <br>
            Iedereen is vrij om zich te registreren en het spel te spelen. <br>
            Echter, ieder doet dit geheel op eigen risico en er kunnen geen rechten aan het gebruik van dit spel worden ontleend. <br>
            <b>De beheerder kan zien welke stomme fouten door spelers worden gemaakt. <br>
            Het is volledig aan de beheerder om stomme fouten bekend te maken met naam en toenaam op alle sociale media.</b>
            
          </p>

          <p>Kijk voor een gedetaileerdere uitleg naar de toelichting op de homepage als je bent ingelogd.</p>

          <h3>Het spel</h3>
          <p>
            Het betreft een spel om op afstand met elkaar te kunnen klaverjassen in de Rotterdamse variant.
            Er kan een wedstrijd worden aangemaakt. Binnen een wedstrijd kunnen vervolgens 1 of meerdere tafels/potjes worden aangemaakt. 
            Spelers kunnen zich bij een potje aanmelden. Zodra 4 spelers bij een potje zijn aangemeld kan het potje gespeeld worden. 
            Binnen een wedstrijd wordt ieder potje (tafel) met precies dezelfde set gedeelde kaarten gespeeld. 
            Hierdoor is het mogelijk de score van ieder potje binnen een wedstrijd met elkaar te vergelijken.
          </p>
          <p>
            Tijdens het spelen van het spel moeten de 4 spelers aangemeld zijn in het potje, zodat alle informatie tegelijk naar alle 4 de spelers
            kan worden verzonden.
            Er moet verplicht worden aangenomen, waarbij de speler die moet aannemen de troef kan selecteren (door in het midden op de troefkleur te klikken).
            Het spel geeft aan wie aan de beurt is om een kaart te spelen. Zodra een slag is gespeeld bepaalt het spel wie de slag heeft gewonnen en geeft 
            de volgende beurt aan de winnaar van de slag. Als alle slagen gespeeld zijn berekend het spel de score en bepaalt of de aangenomen partij 'door'
            of 'nat' is. Alle overige zaken moeten de spelers zelf regelen, zoals roem melden of verzaken melden.
          </p>

          <h3>Spel in ontwikkeling</h3>
          <p>
            Het spel heeft op dit moment een fase bereikt waarbij het redelijk goed gespeeld kan worden. Toch ontbreken nog een aantal
            gewenste funtionaliteiten en loopt er soms iets niet geheel goed. 
            Mocht u bugs tegenkomen of tips en suggesties voor verbetering hebben dan kunt u die sturen naar klaverjasfun@gmail.com. 
          </p>

          <h3>Tips bij spelen</h3>
          <p>
            Hieronder volgen een aantal tips bij het spelen van het spel
          
            <ul>
              <li>Speel het spel met elkaar in een video meeting (Teams, Zoom, etc.) </li>
              <li>Bekend is dat de huidige versie niet goed samenwerkt met Apple apparatuur en Internet Explorer. 
                Gebruik bij voorkeur Chrome of Firefox. (Opera en Vivaldi browsers lijken ook goed te werken)</li>
              <li>Gebruik de buttons van het spel om door het spel te navigeren. 
                Gebruik NIET de 'Go-back' knop van de browser om terug te gaan naar een vorig scherm.
              </li>
              <li>
                Dit spel werkt op zowel PC, laptop als mobiel. 
                Het scherm past zich automatisch aan. 
                Op de PC kan de browser het best worden ingesteld met een smalle breedte.
                Op tablet of telefoon moet je het toestel rechtop houden, ofwel in portait stand. 
                In een landscape stand passen de kaarten niet geheel op het scherm en staan de kaarten te ver uit elkaar.
              </li>
              <li>Alle spelers moeten tegelijkertijd in verbinding staan met het spel. Bij een slechte verbinding van een speler kan het spel haperen.</li>
              <li>Soms wordt een kaart gespeeld, maar wordt dit niet getoond. Ga dan naar de Acties-knop en kies Reset-slag. 
                Hiermee kan de gehele slag opnieuw worden gespeeld. </li>
              <li>Roem moet worden vastgelegd door de speler die de slag wint. Eerst moet de roem worden gemeld en dan pas de slag worden 'binnengehaald'. 
                Als een slag is binnengehaald, kan de roem niet meer worden aangepast. Hooguit kan in een volgende slag ter correctie een negatieve roem worden vastgelegd.
              </li>
              <li>Een gespeelde kaart kan worden teruggenomen door de gehele slag te resetten voordat de slag is binnengehaald. 
                Iedere speler moet dan opnieuw zijn kaart spelen.
              </li>
              <li>Speel de kaarten niet te snel achter elkaar om synchronisatie issues te vermijden</li>
              <li>Het spel biedt nog geen mogelijkheden om persoonlijke gegevens te wijzigen of registratie te verwijderen. 
                Wilt u dat uw registratie wordt verwijderd, stuur dan een mail naar klaverjasfun@gmail.com.  </li>
          </ul>

          </p>

            
          <!-- <h3>Releases</h3>
          <p>
            Hieronder volgt een kort overzicht van de toegevoegde functionaliteiten per release
          </p>
          <h5>Release 003</h5>
          <ul>
            <li>Do not allow to change the number of legs (rondes) of a match when a first round (slag) has been registered</li>
            <li>Log the login of users login and the registration of new users</li>
            <li>Send mail to admin when a new user registers</li>
            <li>Improve game overview layout</li>
            <li>Improve text alignment in score view for game</li>
            <li>Add score of round (slagen) to the overview of rounds  played in the leg (ronde)</li>
            <li>Show the totalcount of points of a round. In case of 'nat gaan' you can see the actual counted points</li>
            <li>Not allowed to (un)registere to game (potje) when game is 'uitgespeeld'</li>
            <li>When game is 'uitgespeeld' show the match bar in red color</li>
            <li>Make sure all screens for mobile and tablet are full screen (except at login/home)</li>
            <li>Forgotten password handling using reset code, send html based mail and use reset code expiration</li>
            <li>For given email address send the usernames that belong to this email address</li>
          </ul>

          <h5>Release 002</h5>
          <ul>
            <li>Support melden verzaken</li>
            <li>Change app title to be shown in the browser tab</li> 
            <li>Auto refresh in 3 seconds the game overview and game details</li> 
            <li>Move the button for 'selecteer troef' and 'neem slag' to a higher position above the player cards</li> 
            <li>In game play screen create a single dropdown button for multiple type of actions</li> 
            <li>In game play screen show to which team (A/B) a player belongs</li> 
            <li>When showing the played 'slagen', show the troef that was active</li> 
            <li>Improve the Redis image</li> 
            <li>Show only the previous slag during the game</li> 
            <li>Show original position of player on screen, so that player knows which player they are when looking back to the slagen</li> 
            <li>Show original player number in the games details (overview)</li> 
            <li>Make the code independent of dev / prod environment</li>
          </ul> -->

        </b-container>
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

      <br><br><br>
      <p>version: {{ appSettings.x_version}} </p>

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
      //Check that screen is mobile. If so, set full screen
      var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
      if (isMobile) {
        // document.body.requestFullscreen()
        document.documentElement.requestFullscreen()
      }
      
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
