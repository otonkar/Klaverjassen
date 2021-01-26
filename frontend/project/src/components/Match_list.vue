<template>
  <div class="Appmatch_list">

    <b-container>

      <br>
      <h2>Overzicht wedstrijden</h2>

      <hr>
      <button  v-on:click="gotoMatches()" class="btn btn-secondary"> Terug naar wedstrijd pagina  </button>
      <hr>
      <p>
        Op deze pagina ziet u een overzicht van alle geregistreerde wedstrijden, met tussen haakjes de gebruikersnaam 
        van de eigenaar. Door op een wedstrijd te klikken komt u in het overzicht van de potjes.
      </p>
      <hr>

      <h5>Filter op wedstrijden</h5>

      <p>
       U kunt de lijst gevonden wedstrijden in perken door filters te gebruiken.
      </p>

      <div>
        <b-form>
          <b-form-input
            v-model="filterName"
            id="filterName"
            placeholder="Geef (deel van) wedstrijdnaam"
          ></b-form-input>

          <b-form-input
            v-model="filterDescription"
            id="filterDescription"
            placeholder="Geef (deel van) omschrijving wedstrijd"
          ></b-form-input>

          <b-form-input
            v-model="filterOwner"
            id="filterOwner"
            placeholder="Geef (deel van) gebruikersnaam eigenaar"
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

      <!-- Pop up Explanation of status -->
      <div>
        <b-modal hide-footer v-model="show_explanation_status">
          <h5>Uitleg wedstrijd status</h5>
          <p>
              Wedstrijden hebben een status, aangegeven door een kleur.
              De status is afhankelijk van de combinatie van start/stop datum van de wedstrijd en of de registratie stop 
              datum gepasseerd is (registratie periode is Open/Gesloten). Onderstaande tabel geeft een overzicht.
          </p>

          <div class="Table">
            <b-table-simple small caption-top responsive>
                
                <colgroup><col></colgroup>
                <colgroup><col><col></colgroup>
                <b-thead head-variant="light">
                <b-tr >
                    <b-th colspan="1" ></b-th>
                    <b-th class="text-center" colspan="2" variant="">Registratie</b-th>
                </b-tr>
                <b-tr >
                    <b-th class="text-right"></b-th>
                    <b-th class="text-center" variant="">Open</b-th>
                    <b-th class="text-center" variant="">Gesloten</b-th>

                </b-tr>
                </b-thead>
                <b-tbody >
                    <b-tr>
                      <b-th variant="light" class="text-right"> Niet gestart </b-th>
                      <b-th variant="light" class="text-center"> Blauw </b-th>
                      <b-th variant="light" class="text-center"> Grijs </b-th>
                    </b-tr>
                    <b-tr>
                      <b-th variant="light" class="text-right"> Gestart </b-th>
                      <b-th variant="light" class="text-center"> Groen </b-th>
                      <b-th variant="light" class="text-center"> Geel </b-th>
                    </b-tr>
                    <b-tr>
                      <b-th variant="light" class="text-right"> Gestopt </b-th>
                      <b-th variant="light" class="text-center">  -  </b-th>
                      <b-th variant="light" class="text-center"> Rood </b-th>
                    </b-tr>
                </b-tbody>

            </b-table-simple>
          </div>

          <p>
            De registatie stop datum moet liggen voor de wedstrijd stop datum. De status waarbij de wedstrijd is gestopped, 
            maar waarbij de registratie nog toegestaan is, kan daarom niet voorkomen.
          </p>

          <b-button class="mt-3" block @click="show_explanation_status=!show_explanation_status" variant="secondary">Sluiten</b-button>
          <br>

          <p>
            De eigenaar van een wedstrijd heeft de mogelijkheid de start/stop datums aan te passen. 
            Hierdoor kan de status van een wedstrijd gewijzigd worden. Dit kan inhouden dat al potjes in een 
            wedstrijd zijn gestart, terwijl daarna de wedstrijd start datum wordt aangepast naar tijdstip zodat nog 
            geen potjes gestart mogen worden.
            
          </p>
          <p>
            Hieronder volgt een nadere uitleg.
            <ul>
              <li>
                  <b>Blauw:</b> <br>
                  Wedstrijd is nog niet gestart, registratie bij een potje mag nog plaatsvinden. <br>
                  Spelers mogen potjes aanmaken, zich aan- en afmelden bij een potje.
                  Nieuwe potjes mogen niet gestart worden om te spelen. 
                  Wel mag een reeds gestart potje worden uitgespeeld.
              </li>
              <li>
                  <b>Grijs:</b> <br>
                  Wedstrijd is nog niet gestart, registratie mag niet meer plaatsvinden. <br>
                  Spelers mogen geen potjes aanmaken, zich aan- en afmelden bij een potje of een potje starten om te spelen.
                  Wel mag een reeds gestart potje worden uitgespeeld.
                  
              </li>
              <li>
                  <b>Groen: </b> <br> 
                  Wedstrijd is gestart, maar nog niet gestopt en registratie mag nog plaatsvinden. <br>
                  Spelers mogen potjes aanmaken, potjes starten en zich aan/af melden bij potjes.
              </li>
              <li>
                  <b>Geel:</b> <br>
                  Wedstrijd is gestart, maar nog niet gestopt en registratie mag niet meer plaatsvinden. <br>
                  Spelers mogen potjes aanmaken en zich niet meer aan- en afmelden bij een potje.
                  Wel mag een potje gestart worden om te spelen.                                
              </li>
              <li>
                  <b>Rood:</b> <br>
                  Wedstrijd is gestopt. <br>
                  Spelers mogen geen potjes meer aanmaken of zich aanmelden bij potje.
                  Potjes mogen niet meer gestart worden. Reeds gestarte potjes mogen wel afgespeeld worden.
                  Spelers van buiten dit potje mogen de gespeelde slagen inzien.
              </li>
            </ul>
          </p>

          <b-button class="mt-3" block @click="show_explanation_status=!show_explanation_status" variant="secondary">Sluiten</b-button>
        </b-modal>
        
      </div>

       <!-- <b-button v-on:click="clearFilters()" variant="primary" class="btn"> Verwijder filters  </b-button>  -->

       <b-row>
            <b-col><b-button v-on:click="clearFilters()" block variant="primary" class="btn"> Verwijder filters  </b-button></b-col>
            <b-col><b-button @click="show_explanation_status=!show_explanation_status"  block variant="secondary" class="btn"> Uitleg status  </b-button></b-col>
      </b-row>


      <hr>
      <h4>Getoonde wedstrijden ({{filterMatches.length }}/{{count}})</h4>
      <br>

      <div v-for="item in filterMatches" v-bind:key="item.matchID">
    
        <b-button v-on:click=" gotoGamesOverview(item.matchID, item.status_color)" block v-bind:variant="item.status_color">{{ item.matchID }} ({{ item.owner.username }})</b-button>
        <div class="comment">
          <b>Omschrijving: </b> {{item.description | shorten(600)}}
        </div>
        <br>

      </div>

      <hr>
      <button  v-on:click="gotoMatches()" class="btn btn-secondary"> Terug naar wedstrijd pagina  </button>
      <hr>

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
      test: '', 
      count: 0,   // Count the number of match results
      test: {},
      match_list: [],
      result_test: {},
      match_color: '',          // Color to show
      filterName:'',             // used to filter on name of match
      filterOwner: '',          // used to filter on owner of match
      filterStatus: '',
      filterDescription: '',
      show_explanation_status: false,     // Show jumbotron with explanation
      match_statusses: [
        {'text': 'Selecteer filter op status', 'value': ''},
        {'text': 'Status blauw', 'value': 'primary'},
        {'text': 'Status geel', 'value': 'warning'},
        {'text': 'Status grijs', 'value': 'secondary'},
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
          var isMobile = /Android/i.test(navigator.userAgent);
          if (isMobile) {
            document.documentElement.requestFullscreen()
          }
          // console.log('Navigator:', navigator.appCodeName)
          // console.log('Navigator:', navigator.userAgent)
          // this.test = navigator.userAgent

          this.user.show_header = true
          this.$store.dispatch('updateUser', this.user)
          this.count = 0
          this.getMatchList()
      }//END if
  },//END mounted
  methods: {

    gotoMatches: function () {
      this.$router.push({ name: 'Matches' })

      let message = 'BackTo Wedstrijden'
      this.logButton(message)
    },  //END gotoMatches

    gotoGamesOverview: function (matchID, status_color) {
      // goto to new page and send 1 or more parameters in a params object
        this.$router.push({ name: 'Games_overview', params: { matchID: matchID, status_color:status_color } })

        let message = 'Start/Wedstrijden/MatchList/Potjes: ' + matchID
        this.logButton(message)
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
            this.count = this.match_list.length


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

<style scoped lang='scss'>

.comment {
  margin: 2px 10px 0px 10px;
  font-size: 0.9em;
  color: #555555;
  font-family: sans-serif;
  line-height: 1.2;
  // font-weight: bold;
}

</style>
