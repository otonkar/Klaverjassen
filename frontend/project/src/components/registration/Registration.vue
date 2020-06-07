<template>
    <div class="Appregistration">

      <br><br>  

      <div class="container col-xl-4 col-lg-6" >
          
        <div class="card">
            <article class="card-body">
                <h4 class="card-title text-center mb-4 mt-1">Registreren</h4>
                <hr>
                <p class="text-info text-center">
                    Registreer als nieuwe gebruiker <br>
                </p>

                <!-- <form id="login-form" method="post" > -->
                    <div class="form-group">
                        <!-- <span class="text-primary "> Geef de gebruikersnaam  </span> -->
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                            </div>
                            <!-- <input name="" class="form-control" placeholder="Email address" type="email"> -->
                            <input ref="username" v-model="input.username" class="form-control" placeholder="gebruikers naam" type="text">
                            <div ref="f-username" class="invalid-feedback "> {{ error_message["username"] }} </div>
                        </div> <!-- input-group.// -->
                        <small id="passwordHelpBlock" class="form-text text-muted">
                            Dit is de naam waarmee u inlogt en die getoond wordt als spelersnaam. 
                            <br> Gebruik alleen letter en cijfers.
                        </small>
                    </div> <!-- form-group// -->
                    <div class="form-group">
                        <!-- <span class="text-primary "> Geef uw voornaam  </span> -->
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                            </div>
                            <!-- <input name="" class="form-control" placeholder="Email address" type="email"> -->
                            <input ref="first_name" v-model="input.first_name" class="form-control" placeholder="Roepnaam" type="text">
                            <div ref="f-username" class="invalid-feedback ">Vul een voornaam in. </div>
                        </div> <!-- input-group.// -->
                        <small id="passwordHelpBlock" class="form-text text-muted">
                            De naam waarmee u geboren bent, maar die niemand kent
                        </small>
                    </div> <!-- form-group// -->
                    <div class="form-group">
                        <!-- <span class="text-primary "> Geef uw achternaam  </span> -->
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                            </div>
                            <!-- <input name="" class="form-control" placeholder="Email address" type="email"> -->
                            <input ref="last_name" v-model="input.last_name" class="form-control" placeholder="Achternaam" type="text">
                        <div ref="f-username" class="invalid-feedback ">Vul een achternaam in </div>
                        </div> <!-- input-group.// -->
                        <small id="passwordHelpBlock" class="form-text text-muted">
                            Uw achternaam zoals geregistreerd bij het ministerie van justitie
                        </small>
                    </div> <!-- form-group// -->
                    <div class="form-group">
                        <!-- <span class="text-primary "> Geef uw e-mail adres  </span> -->
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                            </div>
                            <input ref="email" v-model="input.email" class="form-control" placeholder="Email adres" type="email">
                        <div ref="f-username" class="invalid-feedback ">Vul een correct mail adres in (user@xxx.com) </div>
                        </div> <!-- input-group.// -->
                        <small id="passwordHelpBlock" class="form-text text-muted">
                            Dit is het mail adres dat wordt gebruikt bij wachtwoord vergeten
                        </small>
                    </div> <!-- form-group// -->
                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-lock"></i> </span>
                            </div>
                            <input ref="password" v-model="input.password" class="form-control" placeholder="Wachtwoord" type="password">
                        <div ref="f-password" class="invalid-feedback ">{{ error_message["password"] }} </div>
                        </div> <!-- input-group.// -->
                        <small id="passwordHelpBlock" class="form-text text-muted">
                            Het wachtwoord kan 8 of meer karakters bevatten. Uitsluitend cijfers is niet toegestaan.
                            </small>
                    </div> <!-- form-group// -->
                    <div class="form-group">
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-lock"></i> </span>
                            </div>
                            <input ref="password2" v-model="input.password2" class="form-control" placeholder="Herhaal wachtwoord" type="password">
                        <div ref="f-username" class="invalid-feedback ">Vul hetzelfde correcte wachtwoord in</div>
                        </div> <!-- input-group.// -->
                        <small id="passwordHelpBlock" class="form-text text-muted">
                            Herhaal het wachtwoord
                        </small>
                    </div> <!-- form-group// -->
                    <div class="form-group">
                        <button type="submit" v-on:click="doRegistration()" class="btn btn-primary btn-block"> Registreren  </button>
                    </div> <!-- form-group// -->
                     <div class="form-group">
                        <button type="submit" v-on:click="gotoLogin()" class="btn btn-secondary btn-block"> Ga terug naar Login  </button>
                    </div> <!-- form-group// -->

                <!-- </form> -->

            </article>
        </div> <!-- card.// -->
              <p class="small text-muted">Coronaright, 2020</p>

      </div>
    
    </div>
</template>


<script>
// import axios from 'axios'

    export default {
        name: 'Appregistration',
        data () {
        return {
            title: 'Registration page',
            input: {
                username    : '',
                first_name  : '',
                last_name   : '',
                email       : '',
                password    : ''
            },
            // log errors on input fieds
            input_ok: {
                username    : false,
                first_name  : false,
                last_name   : false,
                email       : false,
                password    : false,
                password2   : false
            },
            // Initital errror messages, before being updated from the registration API
            error_message : {
                username    : 'Vul een andere gebruikersnaam in.',
                first_name  : false,
                last_name   : false,
                email       : false,
                password    : 'Vul een  correct wachtwoord in',
                password2   : false
            },
            registration_success: false,
            errors: {},         // to store the errors from the API call
            data: {}
        }
        },
        activated: function () {
            document.title = 'Klaverjasfun - Registration'
        },
        mounted: function () {
            // console.log(this.$route.name)
            // Do not show full screen on login page
            // document.exitFullscreen();
        },
        methods: {
            gotoLogin: function () {
                this.$router.push({ name: 'Login' })
            },  //END gotoLogin
            
            doRegistration: async function () {
            
            // Do not use 'api_request' or axios, so that this call will not use the interceptors
            const axios = require('axios')
            const api_call = axios.create()

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

            // Validate that the passwords are the same
            if (this.input.password !== this.input.password2) {
                // Only show error on password2
                this.$refs.password2.classList.remove("is-valid")
                this.$refs.password2.classList.add("is-invalid")
                this.input_ok.password2 = false
            }//END if.  no else needed. Only check the error.

            // Validate that password length >= 8
            // Set both passwords to incorrect when this is false
            if (this.input.password.length < 8) {
                this.$refs.password.classList.remove("is-valid")
                this.$refs.password.classList.add("is-invalid")
                this.input_ok.password = false
                this.$refs.password2.classList.remove("is-valid")
                this.$refs.password2.classList.add("is-invalid")
                this.input_ok.password2 = false
            }

            // only do a API request when all input is ok
            // Note Django will do further validations on password, mail, etc.
            // The API will receive the error messages in that situation
            var total_ok = true   // Do AND on the fields statusses
            for (var key1 in this.input_ok) {
                total_ok = total_ok && this.input_ok[key1]
            }
            // console.log(total_ok)

            // Do the API call
            this.errors = {}
            if (total_ok === true) {

                await api_call({
                    method: 'post',
                    url: this.appSettings.url_registration,
                    data: this.input
                })
                .then(response => {
                    // console.log('status registration: ',response.status)
                    if (response.status === 201) {
                        alert("Registratie is gelukt")
                        this.registration_success = true
                        this.$router.push({ name: 'Login' }) 
                    }
                })
                .catch(error => {
                    // console.log('Registratie niet gelukt')
                    // // console.log(error.response)
                    this.errors = error
                })
            }
                
            // console.log("DUMMY")

            // the API call is done with await, so that first the call is handled
            // Only check the errors when there are errors coming from the call
            if (!this.registration_success ) {
                // console.log('DUMMY3')
                // console.log(this.errors.response.data)

                // Check the error messages per data input
                for (var key2 in this.errors.response.data) {
                    // console.log(key2)
                    // Note when key exists then it mean there was an error message on that data field
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
  