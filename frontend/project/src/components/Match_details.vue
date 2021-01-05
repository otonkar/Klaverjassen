<template>
  <div class="Appmatch_details">

    <b-container>

        <br>
        <h2>Details wedstrijd </h2>
        <hr>
            {{ match_status }}, {{ register_status }}
        <hr>
        <!-- <button  v-on:click="gotoMatchesList()" class="btn btn-secondary"> Terug  </button> -->

          <b-row>
            <b-col><b-button block v-on:click="gotoMatchesList()"  class="btn btn-secondary"> Naar wedstrijden  </b-button></b-col>
            <b-col><b-button block v-on:click="gotoGamesOverview()" class="btn btn-success"> Naar potjes  </b-button></b-col>
        </b-row>
        <br>

        <div>

            <!-- **** MatchID **** -->
            <b-form-group
                id="fieldset-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Naam van de wedstrijd"
                label-for="input-horizontal"
            >
                <b-form-input v-model="match_details.matchID" id="matchID" size="lg" disabled></b-form-input>
            </b-form-group>

            <!-- **** Owner **** -->
            <b-form-group
                id="fieldset-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Naam eigenaar van de wedstrijd"
                label-for="input-horizontal"
            >
                <b-form-input v-model="match_details.owner.username" disabled id="owner" ></b-form-input>
            </b-form-group>

            <!-- **** description **** -->
            <b-form-group
                id="fieldset-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Omschrijving (max 500 karakters)"
                label-for="input-horizontal"
            >
                <div ref="description">
                <b-form-textarea
                    id="description"
                    v-model="match_details.description"
                    v-bind:disabled="!allow_update_match"
                    placeholder="Geef de omschrijving..."
                    rows="2"
                    max-rows="6"
                    >
                </b-form-textarea>
                </div>
                <div ref="f-n_legs" class="invalid-feedback "> {{ error_message["description"] }} </div>
            </b-form-group>

            <!-- **** n_legs **** -->
            <b-form-group
                id="fieldset-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Aantal rondes per potje"
                label-for="input-horizontal"
            >
                <input ref="n_legs" id="n_legs"  v-model="match_details.n_legs" v-bind:disabled="!allow_update_match" class="form-control" placeholder="Het aantal rondes per wedstrijd" type="text">
                <!-- <b-form-input ref="n_legs" v-model="match_details.n_legs" v-bind:disabled="!allow_update_match" ></b-form-input> -->
                <div ref="f-n_legs" class="invalid-feedback "> {{ error_message["n_legs"] }} </div>
            </b-form-group>

            <!-- **** Start datum ***** -->
            <b-form-group
                id="fieldset-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Datum dat de potjes mogen starten"
                label-for="input-horizontal"
            >
                <!-- <b-form-input v-bind:disabled="!allow_update_match" id="input-horizontal"></b-form-input> -->
                <b-form-datepicker 
                    v-model="match_details.date_match_start" 
                    v-bind:disabled="!allow_update_match"  
                    id="date_match_start" 
                    class="mb-2"
                ></b-form-datepicker>
            </b-form-group>

            <!-- **** Stop datum ***** -->
            <b-form-group
                id="fieldset-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Datum vanaf wanneer geen potjes meer gestart mogen worden"
                label-for="input-horizontal"
            >
                <!-- <b-form-input v-bind:disabled="!allow_update_match" id="input-horizontal"></b-form-input> -->
                <div ref="date_match_stop">
                <b-form-datepicker 
                    v-model="match_details.date_match_stop" 
                    v-bind:disabled="!allow_update_match"  
                    id="date_match_stop" 
                    ref="date_match_stop" 
                    class="mb-2"
                ></b-form-datepicker>
                </div>
                <div ref="f-date_match_stop" class="invalid-feedback "> {{ error_message["date_match_stop"] }} </div>
            </b-form-group>

            <!-- **** Register Stop datum ***** -->
            <b-form-group
                id="fieldset-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Datum vanaf wanneer aanmelding bij de potjes stopt"
                label-for="input-horizontal"
            >
                <!-- <b-form-input v-bind:disabled="!allow_update_match" id="input-horizontal"></b-form-input> -->
                <div ref="date_register_stop">
                <b-form-datepicker 
                    v-model="match_details.date_register_stop" 
                    v-bind:disabled="!allow_update_match"  
                    id="date_register_stop" 
                    class="mb-2"
                ></b-form-datepicker>
                </div>
                <div ref="f-date_register_stop" class="invalid-feedback "> {{ error_message["date_register_stop"] }} </div>
            </b-form-group>
        </div>

        <div class="form-group">
            <button type="submit" 
                v-on:click="updateMatchDetails()" 
                v-bind:display="!allow_update_match" 
                class="btn btn-primary btn-block"
                id="updateMatch"
            > 
                Update gegevens  
            </button>
        </div>

    </b-container>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Appmatchdetails',
  data () {
    return {
        title: 'Match details page',
        matchID: '',
        match_details: {
            owner: {
                username: ''    // Define in advance, to avoid a render error on first load of page
            }
        },
        match_status: 'test',
        register_status: '',
        match_update_success   : false ,    // Incidator that match was update
        input_ok: {             // Indicator that the input is ok or not
            // matchID             : false,
            description         : false,
            n_legs              : false,
            // date_match_start    : false,
            date_match_stop     : false,
            date_register_stop  : false
        },
        error_message : {       // initial Error messages to be deplayed in the form
            matchID             : false,
            description         : false,
            n_legs              : false,
            date_match_start    : false,
            date_match_stop     : false,
            date_register_stop  : false
        },
        allow_update_match: false,
        errors                     : {}
    }
  },
  // Do not use mounted, otherwise no new match will be loaded
  activated: function () {
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

        this.matchID = this.$route.params.id
        // // console.log('user = ', this.user)
        this.user.show_header = true
        this.$store.dispatch('updateUser', this.user)
        this.getMatchDetails()

      }//END if
  },//END mounted
  
  methods: {
    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    },  //END gotoLogin
    gotoMatchesList: function () {
      this.$router.push({ name: 'Match_list' })
    },  //END gotoMatches
    gotoGamesOverview: function () {
        // goto to new page and send 1 or more parameters in a params object
        this.$router.push({ name: 'Games_overview', params: { match_details: this.match_details } })
    },  //END gotoGamesOverview
    doHideElement: function (id) {
        var x = document.getElementById(id);
        x.style.display = "none";
    },
    doShowElement: function (id) {
        var x = document.getElementById(id);
        x.style.display = "block";
    },
    getMatchDetails: async function () {
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        await api_request({
            method: 'get',
            url: this.appSettings.url_match_details + this.matchID + '/',
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

        // disable the updating of fields when the user is not the owner
        if (this.match_details.owner.username === this.user.username) {
            this.allow_update_match = true
            this.doShowElement('updateMatch')
        } else {
            this.allow_update_match = false
            this.doHideElement('updateMatch')
        }

        //Determine the status of the match
            const currentdate = new Date() 
            const match_start = new Date(this.match_details.date_match_start)
            const match_stop = new Date(this.match_details.date_match_stop)


            if (currentdate < match_start) {
                this.match_status = 'wedstrijd nog niet gestart'
            } 
            
            if (currentdate >= match_start && currentdate < match_stop) {
                this.match_status = 'wedstrijd is bezig'
            } 
            
            if (currentdate >= match_stop) {
                this.match_status = 'wedstrijd is gesloten'
            }

            //Determine the status of registering
            const register_stop = new Date(this.match_details.date_register_stop)
            if (currentdate < register_stop) {
                this.register_status = 'inschrijving is open'
            } else {
                this.register_status = 'inschrijving is gesloten'
            }

            // If wedstrijd is closed than disable update
            // !! allow match to be update after being closed!!
            // So that the Owner can extend the stop data
            // if (this.match_status === 'wedstrijd is gesloten') {
            //     this.doHideElement('updateMatch')
            //     this.allow_update_match = false
            // }

            // Remove all error messages
            for (var key in this.input_ok) {
            this.input_ok[key] = false
            this.$refs[key].classList.remove("is-invalid")
            this.$refs[key].classList.add("is-valid")
            }

        
    },  //END getMatchDetails
        updateMatchDetails: async function () {
            
        // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')

        //@@ When a first table has started then no update of n_legs is allowd
        // @@

        // Reset all error messages
        for (var key in this.input_ok) {
        this.input_ok[key] = true
        this.$refs[key].classList.remove("is-invalid")
        this.$refs[key].classList.add("is-valid")
        }
        this.errors = {}
        

        await api_request({
            method: 'put',
            url: this.appSettings.url_match_details + this.matchID + '/',
             data: this.match_details
        })
        .then(response => {
            // console.log('Status update match details: ',response.status)
            if (response.status === 200) {
                this.match_details = response.data
                this.match_update_success = true
                alert('Update succesvol')
            }
        })
        .catch(error => {
            // console.log('Update match details failed')
            this.match_update_success = false
            // console.log(error.response)
            this.errors = error
        })

        // // the API call is done with await, so that first the call is handled
        // // Only check the errors when there are errors coming from the call
        if (!this.match_update_success ) {
            
            // console.log(this.errors.response.data)

            // Check the error messages per data input
            for (var key2 in this.errors.response.data) {
                // console.log(key2)
                // Note when key exists then it means there was an error message on that data field
                this.$refs[key2].classList.remove("is-valid")
                this.$refs[key2].classList.add("is-invalid")
                this.input_ok[key2] = false
                // this message is a list of 1 or more remarks about the datafield
                var total_message = ''
                for (var item in this.errors.response.data[key2] ) {
                        total_message = total_message  + this.errors.response.data[key2][item] + ', '
                        this.error_message[key2] = total_message
                        // console.log(this.error_message)
                        // console.log('DUMMY3')
                    }
            }//END for 
        }//END if check errors
        // console.log('DUMMY4')

        
    },  //END getMatchDetails
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
