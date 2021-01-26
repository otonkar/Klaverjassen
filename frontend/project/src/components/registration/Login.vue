<template>
    <div class="Applogin">

      <br><br>  

      <div class="container col-xl-7 col-lg-6" >
          
              <div class="card">
                  <article class="card-body">
                      <h4 class="card-title text-center mb-4 mt-1">Aanmelden</h4>
                      <hr>
                      <p class="text-info text-center">log in met gebruikersnaam</p>

                      <!-- <form id="login-form" method="post" > -->
                          <div class="form-group">
                              <div class="input-group">
                                  <div class="input-group-prepend">
                                      <span class="input-group-text"> <i class="fa fa-user"></i> </span>
                                  </div>
                                  <!-- <input name="" class="form-control" placeholder="Email address" type="email"> -->
                                  <input name="username" v-model="user.username" class="form-control" placeholder="gebruikersnaam" type="text">
                              </div> <!-- input-group.// -->
                          </div> <!-- form-group// -->
                          <div class="form-group">
                              <div class="input-group">
                                  <div class="input-group-prepend">
                                      <span class="input-group-text"> <i class="fa fa-lock"></i> </span>
                                  </div>
                                  <input v-on:keyup.13="doLogin()" name="password" v-model="user.password" class="form-control" placeholder="wachtwoord" type="password">
                              </div> <!-- input-group.// -->
                          </div> <!-- form-group// -->
                          <div class="form-group">
                              <button type="submit" v-on:click="doLogin()" class="btn btn-primary btn-block"> Login  </button>
                          </div> <!-- form-group// -->
                          <p class="text-center">
                            <!-- <a class="btn text-success">Paswoord vergeten?</a> -->
                            <a @click="gotoRegistration()" class="btn text-success">Registeren</a> <br>
                            <a @click="gotoPasswordReset()" class="btn text-warning">Wachtwoord vergeten</a>
                        </p>

                      <!-- </form> -->

                  </article>
              </div> <!-- card.// -->
              <p class="small text-muted">Coronaright 2021, klaverjasfun@gmail.com</p>

              <!-- <br><br><br>
              <p class="small text-muted">
              Wat werkt: <br>
              * Registreren <br>
              * inloggen <br>
              * Home pagina <br> 
              * Naar wedstrijd pagina en terug <br>
              * test request naar backend server (geeft 200 als het OK is) <br>
              </p> -->

      </div>
    
    </div>
</template>


<script>
// import axios from 'axios'

    export default {
        name: 'Applogin',
        data () {
            return {
                title: 'Login page',
                data: {},
                login_success: false
            }
        },
        activated: function () {
            document.title = 'Klaverjasfun - Login'
            // console.log(this.$route.name)
            // Do not show full screen on login page
            // document.exitFullscreen();
        },
      methods: {
          doLogin: async function () {
            // Do not use 'api_request' or axios, so that this call will not use the interceptors
            const axios = require('axios')
            const api_call = axios.create()

            // console.log('initial access token', localStorage.getItem('access-token'))
            // console.log('initial refresh token', localStorage.getItem('refresh-token'))

            await api_call({
                method: 'post',
                url: this.appSettings.url_get_token,
                data: {
                    username: this.user.username,
                    password: this.user.password
                }
            })
                .then(response => {
                    // // console.log(response.status)
                    // // console.log('login access token: ', response.data.access)
                    // // console.log('login refresh token: ', response.data.refresh)
                    this.user.user_is_logged_in = true
                    this.$store.dispatch('updateUser', this.user)
                    localStorage.setItem('username', this.user.username)

                    // Store token parameters in localStore
                   
                    localStorage.setItem('refresh-token', response.data.refresh)

                    // After successful login go to home page
                    // this.$router.push({ name: 'Home' }) 
                    this.login_success = true
                    

                })
                .catch(error => {
                    // console.log(error.response)

                    if (error.response.status === 401) {
                        alert("Incorrecte gebruikersnaam of wachtwoord")
                        let message = 'Login - Incorrecte gebruikersnaam of wachtwoord: ' + this.user.username  // + ' / ' + this.user.password
                        this.logButton(message)
                    } else {
                        alert("Inlog poging is niet gelukt. Vul zowel de gebruikersnaam als wachtwoord in") 
                        let message = 'Login - Inlog poging is niet gelukt: '  + this.user.username // + ' / ' + this.user.password
                        this.logButton(message)
                    }

                })

                if (this.login_success) {
                    let message = 'Login - Login gelukt: ' + this.user.username
                    this.logButton(message)
                    await this.gotoHome()
                    // await this.doReloadPage()
                    
                }//END if
            },  //END doLogin

            gotoHome: async function () {
                // After successful login go to home page
                this.$router.push({ name: 'Home' }) 

            },

            doReloadPage: async function () {
                // reload page from server
                window.location.reload(true)
            },

            gotoRegistration: function () {
                this.$router.push({ name: 'Registration' })
                let message = 'Registration'
                this.logButton(message)
            },  //END gotoRegistration

            gotoPasswordReset: function () {
                let message = 'Password reset'
                this.logButton(message)
                this.$router.push({ name: 'ResetPassword' })
            },//END gotoPasswordReset

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

</style>
  