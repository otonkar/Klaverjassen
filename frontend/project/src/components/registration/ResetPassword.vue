<template>
    <div class="Appresetpassword">

      <br>  

      <div class="container col-xl-4 col-lg-6" >

        <button  v-on:click="gotoLogin()" class="btn btn-secondary"> Terug naar Login  </button>
        <br><br>
          
        <div class="card">
            <article class="card-body">
                <h4 class="card-title text-center mb-4 mt-1">Wachtwoord vergeten</h4>
                <hr>
                <p class="text-info text-center">
                    Aanvragen wachtwoord reset code <br>
                </p>

                <!-- <p>
                    Geef uw gebruikersnaam om een password resetcode aan te vragen. <br>
                    Als u uw gebruikersnaam niet meer weet kunt u ook uw geregistreerde email adres gebruiken.
                    Echter, dit werkt alleen als u slechts 1 gebruikersnaam heeft aangemaakt met dit mail adres.
                </p> -->

                <!-- <form id="login-form" method="post" > -->
                    <div class="form-group">
                        <span class="text-primary "> Geef uw gebruikersnaam  </span>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                            </div>
                            <!-- <input name="" class="form-control" placeholder="Email address" type="email"> -->
                            <input ref="usernameA" v-model="input.username" class="form-control" placeholder="gebruikers naam" type="text">
                        </div> <!-- input-group.// -->
                    </div> <!-- form-group// -->

                    <div class="form-group">
                        <span class="text-primary "> of geef uw geregistreerde e-mail adres  </span>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                            </div>
                            <input ref="email" v-model="input.email" class="form-control" placeholder="Email adres" type="email">
                        <!-- <div ref="f-email" class="invalid-feedback ">Vul een correct mail adres in (user@xxx.com) </div> -->
                        </div> <!-- input-group.// -->
                        <small  class="form-text text-muted">
                            Het geregistreerde email adres werkt alleen als u slechts 1 gebruikersnaam heeft aangemaakt met dit email adres
                        </small>
                    </div> <!-- form-group// -->

                    <div v-if="show_error_message === true">
                        <p class="text-danger">{{ errors.response.data['message'] }}</p>
                    </div>

                    <div class="form-group">
                        <button type="submit" v-on:click="doRequestResetCode()" class="btn btn-primary btn-block"> Reset code aanvragen  </button>
                    </div> <!-- form-group// -->
                    <br>


                    <p class="text-info text-center">
                        Opnieuw instellen wachtwoord <br>
                    </p>
                    <small>
                        Zodra u een code per mail heeft ontvangen is deze 15 minuten geldig.
                        Vul de ontvangen gebruikersnaam en code hieronder in en kies een nieuw wachtwoord.
                    </small>
                    <br> <br>

                    <div class="form-group">
                        <span class="text-primary "> Geef uw gebruikersnaam  </span>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                            </div>
                            <!-- <input name="" class="form-control" placeholder="Email address" type="email"> -->
                            <input ref="username" v-model="input_pwreset.username" class="form-control" placeholder="gebruikers naam" type="text">
                            <div ref="f-username" class="invalid-feedback "> {{ error_message["username"] }} </div>
                        </div> <!-- input-group.// -->
                        <!-- <small id="passwordHelpBlock" class="form-text text-muted">
                            Dit is de naam waarmee u inlogt en die getoond wordt als spelersnaam. 
                            <br> Gebruik alleen letter en cijfers.
                        </small> -->
                    </div> <!-- form-group// -->

                    <div class="form-group">
                        <span class="text-primary "> Geef uw toegestuurde code  </span>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-lock"></i> </span>
                            </div>
                            <input ref="reset_code" v-model="input_pwreset.reset_code" class="form-control" placeholder="code" type="text">
                        <div ref="f-reset_code" class="invalid-feedback ">{{ error_message["reset_code"] }} </div>
                        </div> <!-- input-group.// -->
                    </div> <!-- form-group// -->

                    <div class="form-group">
                        <span class="text-primary "> Geef een nieuwe wachtwoord  </span>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-lock"></i> </span>
                            </div>
                            <input ref="password" v-model="input_pwreset.password" class="form-control" placeholder="Wachtwoord" type="password">
                        <div ref="f-password" class="invalid-feedback ">{{ error_message["password"] }} </div>
                        </div> <!-- input-group.// -->
                        <small class="form-text text-muted">
                            Het wachtwoord kan 8 of meer karakters bevatten. Uitsluitend cijfers is niet toegestaan.
                            </small>
                    </div> <!-- form-group// -->

                    <div class="form-grouptFm354AF">
                        <span class="text-primary "> Herhaal uw nieuwe wachtwoord  </span>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text"> <i class="fa fa-lock"></i> </span>
                            </div>
                            <input ref="password2" v-model="input_pwreset.password2" class="form-control" placeholder="Herhaal wachtwoord" type="password">
                        <div ref="f-password2" class="invalid-feedback ">Vul hetzelfde correcte wachtwoord in</div>
                        </div> <!-- input-group.// -->
                        <!-- <small id="passwordHelpBlock" class="form-text text-muted">
                            Herhaal het wachtwoord
                        </small> -->
                    </div> <!-- form-group// -->

                    <br>

                    <div v-if="show_error_message_password === true">
                        <p ref="message" class="text-danger">{{ errors.response.data['message'] }}</p>
                    </div>

                    <br>
                    <div class="form-group">
                        <button type="submit" v-on:click="doResetPassword()" class="btn btn-primary btn-block"> Instellen nieuw wachtwoord  </button>
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
        name: 'Appresetpassword',
        data () {
        return {
            title: 'Password vergeten',
            show_error_message: false,              // Show the messages for request reset_code
            show_error_message_password: false,     // show the messages for password reset
            pwreset_success: false,                 // Is true when API password reset is successful
            input_pwreset: {                        // Store the values for the reset password
                username: '',
                password: '',
                password2: '',
                reset_code: ''
            },                        
            input: {
                username    : '',
                email       : '',
                password    : ''
            },
            // log errors on input fieds
            input_ok: {
                username    : false,
                reset_code  : false,
                password    : false,
                password2   : false
            },
            // Initital errror messages, before being updated from the registration API
            error_message : {
                username    : 'Vul een gebruikersnaam in.',
                reset_code  : 'Vul de reset_code in',
                password    : 'Vul een  correct wachtwoord in',
                password2   : ''
            },
            registration_success: false,
            errors: {
                response: {
                    data: {
                        message: ''
                    }
                }
            },         // to store the errors from the API call
            data: {}
        }
        },
        activated: function () {
            document.title = 'Klaverjasfun - Password vergeten'
            this.show_error_message = false
            this.show_error_message_password = false
            this.pwreset_success = false
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

            doRequestResetCode: async function () {
                // reset error messages
                this.pwreset_success = false
                this.show_error_message = false
                // this.errors = {}
                // console.log('DUMMY1', this.input)

                // Do not use 'api_request' or axios, so that this call will not use the interceptors
                const axios = require('axios')
                const api_call = axios.create()

                await api_call({
                    method: 'post',
                    url: this.appSettings.url_resetcode,
                    data: this.input
                })
                .then(response => {
                    // console.log('response: ',response)
                    if (response.status === 200) {
                        alert("Nieuwe reset code is verstuurd")
                        // console.log('Success')
                    }
                })
                .catch(error => {
                    // console.log('Registratie niet gelukt')
                    // console.log(error)
                    // alert("FOUT: Code is niet verstuurd!")
                    this.errors = error
                    this.show_error_message = true
                    // console.log(this.errors.response.data)
                })


                // this.show_input_reset = true
            },

            doResetPassword: async function () {
                // reset error messages
                this.show_error_message_password = false
                // this.errors = {}

                // Define the items for which error messages from the API must be displayed
                // Only response items with the keys will be shown
                var ref_list = ['username', 'reset_code', 'password']

                // Validate that all fields contain a value
                // If not set the error
                for (var key in this.input_pwreset) {
                    var value = this.input_pwreset[key]
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
                // console.log('DUMMY1')

                // Validate that the passwords are the same
                if (this.input_pwreset.password !== this.input_pwreset.password2) {
                    // Only show error on password2
                    this.$refs.password2.classList.remove("is-valid")
                    this.$refs.password2.classList.add("is-invalid")
                    this.input_ok.password2 = false
                }//END if.  no else needed. Only check the error.

                // Validate that password length >= 8
                // Set both passwords to incorrect when this is false
                if (this.input_pwreset.password.length < 8) {
                    this.$refs.password.classList.remove("is-valid")
                    this.$refs.password.classList.add("is-invalid")
                    this.input_ok.password = false
                    this.$refs.password2.classList.remove("is-valid")
                    this.$refs.password2.classList.add("is-invalid")
                    this.input_ok.password2 = false
                }

                // console.log('DUMMY2')
                // console.log(this.input_ok)

                // only do a API request when all input is ok
                var total_ok = true   // Do AND on the fields statusses
                for (var key1 in this.input_ok) {
                    total_ok = total_ok && this.input_ok[key1]
                }
                // console.log('input_ok', this.input_ok)
                // console.log('total_ok ', total_ok)

                // Do the API call
                this.errors = {}
                if (total_ok === true) {

                    // Do not use 'api_request' or axios, so that this call will not use the interceptors
                    const axios = require('axios')
                    const api_call = axios.create()

                    await api_call({
                        method: 'post',
                        url: this.appSettings.url_resetpassword,
                        data: this.input_pwreset
                    })
                    .then(response => {
                        // console.log('response: ',response)
                        if (response.status === 201) {
                            this.pwreset_success = true
                            alert("Uw wachtwoord is aangepast")
                            // console.log('Success')
                        }
                    })
                    .catch(error => {
                        // console.log('Registratie niet gelukt')
                        // // console.log(error.response)
                        // alert("FOUT: wachtwoord niet aangepast!")
                        this.pwreset_success = false
                        this.errors = error
                        this.show_error_message_password = true
                        // console.log('errors.response', this.errors.response)
                    })

                    // the API call is done with await, so that first the call is handled
                    // Only check the errors when there are errors coming from the call
                    if (!this.pwreset_success ) {
                        // console.log('DUMMY3')
                        // console.log(this.errors.response.data)

                        // Check the error messages per data input
                        for (var key2 in this.errors.response.data) {
                            if (ref_list.includes(key2)) {
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
                            }
                        }//END for 
                    }//END if check errors
                    // console.log(this.error_message)

                } //END if axios request

            }, //END doResetPassword
            
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
  