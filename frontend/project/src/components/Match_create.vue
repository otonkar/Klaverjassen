<template>
    <div class="Appmatchcreate">

      <br>
      <b-container>
        <hr>
        <button  v-on:click="gotoMatches()" class="btn btn-secondary"> Terug naar wedstrijd pagina  </button>
        <hr>  
      </b-container>

      <div class="container col-xl-4 col-lg-6" >
          
        <!-- <button type="submit" v-on:click="gotoMatches()" class="btn btn-secondary btn-block"> Ga terug naar Wedstrijd pagina  </button>
        <br> -->

        <div class="card">
            <article class="card-body">
                <h4 class="card-title text-center mb-4 mt-1">Nieuwe wedstrijd maken</h4>
                <hr>
                <p class="text-info text-center">
                    Definieer jouw wedstrijd <br>
                </p>

                <!-- ***** matchID ***** -->
                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                        </div>
                        <input ref="matchID" id="matchID" v-model="input.matchID" class="form-control" placeholder="Nieuwe naam van de wedstrijd" type="text">
                        <div ref="f-matchID" class="invalid-feedback "> {{ error_message["matchID"] }} </div>
                        <b-tooltip target="matchID" triggers='focus hover'>
                            Naam van de wedstrijd:  kan uit maximaal 30 karakters bestaan. Gebruik alleen letters en cijfers en spaties.
                        </b-tooltip>
                    </div> <!-- input-group.// -->
                    <!-- <small id="passwordHelpBlock" class="form-text text-muted">
                        De naam van de wedstrijd kan uit maximaal 30 karakters bestaan. Gebruik alleen letters en cijfers en spaties.
                    </small> -->
                </div> <!-- form-group// -->

                <!-- ***** description ***** -->
                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                        </div>
                        <input ref="description" id="description" v-model="input.description" class="form-control" placeholder="Geef een omschrijving" type="text">
                        <!-- !!!!!!! b-form-texarea met ref werkt niet -->
                        <!-- <div ref="description">
                        <b-form-textarea ref="description" v-model="input.description" id="textarea-rows" size="sm" placeholder="Geef een omschrijving"
                        ></b-form-textarea>
                        </div> -->
                        <div ref="f-description" class="invalid-feedback "> {{ error_message["description"] }} </div>
                        <b-tooltip target="description" triggers='hover focus'>
                            Omschrijving:  deze kan uit maximaal 500 karakters bestaan. Gebruik alleen letters en cijfers en spaties.
                        </b-tooltip>
                    </div> <!-- input-group.// -->
                    <!-- <small id="passwordHelpBlock" class="form-text text-muted">
                        De omschrijving kan uit maximaal 100 karakters bestaan. Gebruik alleen letters en cijfers en spaties.
                    </small> -->
                </div> <!-- form-group// -->

                <!-- ***** n_legs ***** -->
                <div class="form-group">
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                        </div>
                        <input ref="n_legs" id="n_legs"  v-model="input.n_legs" class="form-control" placeholder="Het aantal rondes per wedstrijd" type="text">
                        <div ref="f-n_legs" class="invalid-feedback "> {{ error_message["n_legs"] }} </div>
                        <b-tooltip target="n_legs" triggers='hover focus'>
                            Aantal rondes:  hoeveel rondes gespeeld moeten worden per potje in deze wedstrijd.
                        </b-tooltip>
                    </div> <!-- input-group.// -->
                    <!-- <small id="passwordHelpBlock" class="form-text text-muted">
                        Definieer hoeveel rondes gespeeld moeten worden per potje in deze wedstrijd.            
                    </small> -->
                </div> <!-- form-group// -->

                <!-- ***** date_match_start ***** -->
                <h6>Wedstrijd start datum</h6>
                <div class="form-group">
                    <div class="input-group">
                        <!-- <input ref="date_match_start" v-model="input.date_match_start" class="form-control" placeholder="Het aantal rondes per wedstrijd" type="text"> -->
                            <div ref="date_match_start">
                            <b-form-datepicker  id="date_match_start" v-model="input.date_match_start" class="mb-2"></b-form-datepicker>
                            </div>
                            <!-- <p>Value: '{{ input.date_match_start }}'</p> -->
                        <div ref="f-date_match_start" class="invalid-feedback "> {{ error_message["date_match_start"] }} </div>
                        <!-- <b-tooltip target="date_match_start" triggers='hover focus'>
                            Dit is de datum vanaf wanneer de potjes van deze wedstrijd gespeeld mogen worden.
                        </b-tooltip> -->
                    </div> <!-- input-group.// -->
                    <small id="passwordHelpBlock" class="form-text text-muted">
                        Wedstrijd start datum is de datum vanaf wanneer de potjes van deze wedstrijd gestart mogen worden.           
                    </small>
                </div> <!-- form-group// -->

                <!-- ***** date_match_stop ***** -->
                 <h6>Wedstrijd stop datum</h6>
                <div class="form-group">
                    <div class="input-group">
                        <!-- <input ref="date_match_stop" v-model="input.date_match_stop" class="form-control" placeholder="Het aantal rondes per wedstrijd" type="text"> -->
                            <div ref="date_match_stop">
                            <b-form-datepicker  id="date_match_stop" v-model="input.date_match_stop" class="mb-2"></b-form-datepicker>
                            </div>
                            <!-- <p>Value: '{{ input.date_match_stop }}'</p> -->
                        <div ref="f-date_match_stop" class="invalid-feedback "> {{ error_message["date_match_stop"] }} </div>
                    </div> <!-- input-group.// -->
                    <small id="passwordHelpBlock" class="form-text text-muted">
                        Wedstrijd stop datum is de datum vanaf wanneer geen potjes van deze wedstrijd gespeeld mogen worden.            
                    </small>
                </div> <!-- form-group// -->

                <!-- ***** date_register_stop ***** -->
                 <h6>Registreer stop datum</h6>
                <div class="form-group">
                    <div class="input-group">
                        <!-- <input ref="date_register_stop" v-model="input.date_register_stop" class="form-control" placeholder="Het aantal rondes per wedstrijd" type="text"> -->
                            <div ref="date_register_stop">
                            <b-form-datepicker  id="date_register_stop" v-model="input.date_register_stop" class="mb-2"></b-form-datepicker>
                            </div>
                            <!-- <p>Value: '{{ input.date_register_stop }}'</p> -->
                        <div ref="f-date_register_stop" class="invalid-feedback "> {{ error_message["date_register_stop"] }} </div>
                    </div> <!-- input-group.// -->
                    <small id="passwordHelpBlock" class="form-text text-muted">
                        Registreer stop datum is de datum vanaf wanneer geen nieuwe potjes mogen worden aangemaakt en 
                        spelers zich niet meer mogen aan- of afmelden bij een potje.           
                    </small>
                </div> <!-- form-group// -->


                <!-- ***** Buttons ***** -->
                <div class="form-group">
                    <button type="submit" v-on:click="doCreateMatch()" class="btn btn-primary btn-block"> Maken wedstrijd  </button>
                </div>
                <!-- <div class="form-group">
                    <button type="submit" v-on:click="gotoMatches()" class="btn btn-secondary btn-block"> Ga terug naar Wedstrijd pagina  </button>
                </div> -->


            </article>
        </div> <!-- card.// -->
              <p class="small text-muted">Coronaright 2021</p>

      </div>
    
    </div>
</template>


<script>
// import axios from 'axios'

    export default {
        name: 'Appmatchcreate',
        data () {
        return {
            title: 'Match create',
            input: {                // To collect the input form the form
                matchID             : '',
                description         : '',
                n_legs              : '',
                date_match_start    : '',
                date_match_stop     : '',
                date_register_stop  : ''
            },
            input_ok: {             // Indicator that the input is ok or not
                matchID             : false,
                description         : false,
                n_legs              : false,
                date_match_start    : false,
                date_match_stop     : false,
                date_register_stop  : false
            },
            error_message : {       // initial Error messages to be deplayed in the form
                matchID             : 'De wedstrijd naam moet ingevuld zijn',
                description         : '',
                n_legs              : 'Het aantal rondes in een wedstrijd moet tussen de 1 en 100 liggen',
                date_match_start    : 'De start datum moet ingevuld worden.',
                date_match_stop     : 'De stop datum moet liggen na de start datum van de wedstrijd',
                date_register_stop  : 'Het stoppen van registeren moet liggen voor de stop datum van de wedstrijd'
            },
            form_success: false,                // Indicator that all form fields are ok or not
            match_create_success   : false ,    // Incidator that match was created
            errors: {},                         // to store the errors from the API call
            data: {}
        }
        },
        mounted: function () {
            // console.log(this.$route.name)
            this.user.show_header = true
            this.$store.dispatch('updateUser', this.user)
            // Do not show full screen on login page
            // document.exitFullscreen();
            if (this.user.user_is_logged_in === false) {
                this.$router.push({ name: 'Home' })
            } //END if
        },//END mounted
        methods: {
            gotoMatches: function () {
                this.$router.push({ name: 'Matches' })
            },  //END gotoLogin
            doCreateMatch: async function () {
            
            // Do  use 'api_request' or axios, so that this call WILL use the interceptors
            const api_request = require('axios')

            // console.log('****',this.input.matchID.length)

            // Validate that all fields contain a value
            // When a field is empty set the error
            // Validate that all fields contain a value
            // If not set the error
            for (var key in this.input) {
                var value = this.input[key]
                if (value.length === 0) {
                    this.$refs[key].classList.remove("is-valid")
                    this.$refs[key].classList.add("is-invalid")
                    this.input_ok[key] = false  // 
                } else {
                    this.$refs[key].classList.add("is-valid")
                    this.$refs[key].classList.remove("is-invalid")
                    this.input_ok[key] = true  // 
                }
            }//END for

            // Validate that matchID is <= 30 karakters
            if (this.input.matchID.length > 30) {
                // 
                this.$refs.matchID.classList.remove("is-valid")
                this.$refs.matchID.classList.add("is-invalid")
                this.input_ok.matchID = false
                this.error_message['matchID'] = 'Wedstrijd naam moet korter zijn dan 30 karakters'
            } 

            // Validate that description is <= 500 karakters
            if (this.input.description.length > 500) {
                // 
                var count = this.input.description.length
                this.$refs.description.classList.remove("is-valid")
                this.$refs.description.classList.add("is-invalid")
                this.input_ok.description = false
                this.error_message['description'] = count + 'karakters. Omschrijving moet korter zijn dan 500 karakters'
            } else {
                this.$refs.description.classList.remove("is-invalid")
                this.$refs.description.classList.add("is-valid")
                this.input_ok.description = true
            }

            // Validate that n_legs is a number between 1 and (including) 100
            if (this.input.n_legs <1 || this.input.n_legs > 100) { 
                this.$refs.n_legs.classList.remove("is-valid")
                this.$refs.n_legs.classList.add("is-invalid")
                this.input_ok.n_legs = false
                this.error_message['n_legs'] = 'Kies getal uit [1, 2, 3,.... , 100]'
            }

            // Validate that match stop is later than match start
            if (this.input.date_match_start >= this.input.date_match_stop) {
                this.$refs.date_match_stop.classList.remove("is-valid")
                this.$refs.date_match_stop.classList.add("is-invalid")
                this.input_ok.date_match_stop = false
                this.error_message['date_match_stop'] = 'Stop datum moet later zijn dan start datum van de wedstrijd'
            }

            // Validate that register stop is earlier than match stop
            if (this.input.date_register_stop >= this.input.date_match_stop) {
                this.$refs.date_register_stop.classList.remove("is-valid")
                this.$refs.date_register_stop.classList.add("is-invalid")
                this.input_ok.date_register_stop = false
                this.error_message['date_register_stop'] = 'Registeren moet eerder stoppen dan de wedstrijd'
            }

            // only do a API request when all input is ok
            // Note Django will do further validations.
            // The API will receive the error messages in that situation
            var total_ok = true   // Do AND on the fields statusses to determine that all is ok
            for (var key1 in this.input_ok) {
                total_ok = total_ok && this.input_ok[key1]
            }

            // Do the API call
            this.errors = {}
            if (total_ok === true) {

                await api_request({
                    method: 'post',
                    url: this.appSettings.url_match_create,
                    data: this.input
                })
                .then(response => {
                    // console.log('Status match create: ',response.status)
                    if (response.status === 201) {
                        alert("Wedstrijd is aangemaakt")
                        this.match_create_success = true
                        this.$router.push({ name: 'Matches' }) 
                    }
                })
                .catch(error => {
                    // console.log('Aanmaken wedstrijd niet gelukt')
                    // console.log(error.response)
                    this.errors = error
                })
            }
                
            // // console.log("DUMMY")

            // // the API call is done with await, so that first the call is handled
            // // Only check the errors when there are errors coming from the call
            if (!this.match_create_success ) {
                // console.log('DUMMY3')
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
                        }
                }//END for 
            }//END if check errors
            
            
            },  //END doRegistration
        },  //END methods 
      computed: {
        user () {
            return this.$store.state.user
        },
        appSettings () {
            return this.$store.state.appSettings
        },
      }
    }
</script>


<style scoped lang='scss'>
body {
  background-color: rgb(199, 122, 148);
}
</style>
  