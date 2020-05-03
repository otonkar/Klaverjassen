<template>

    <!-- Only show header when user is logged in -->
    <div v-if="user.user_is_logged_in === true && this.user.show_header === true" class="Appheader">

        <div>
        <b-navbar toggleable="lg" type="light" variant="success">
            <b-navbar-brand >Welkom {{ user.username }}</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <!-- <b-nav-item href="#">Link</b-nav-item>
                    <b-nav-item href="#" disabled>Disabled</b-nav-item> -->
                </b-navbar-nav>

                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">
                    <!-- <b-nav-form>
                    <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                    <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                    </b-nav-form> -->

                    <!-- <b-nav-item-dropdown text="Lang" right>
                        <b-dropdown-item href="#">EN</b-dropdown-item>
                        <b-dropdown-item href="#">ES</b-dropdown-item>
                        <b-dropdown-item href="#">RU</b-dropdown-item>
                        <b-dropdown-item href="#">FA</b-dropdown-item>
                    </b-nav-item-dropdown> -->

                    <!-- <b-nav-item-dropdown right>
                        <template v-slot:button-content>
                            <em>User</em>
                        </template>
                        <b-dropdown-item href="#">Profile</b-dropdown-item>
                        <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                    </b-nav-item-dropdown> -->

                    <!-- <b-nav-item @click="showLogoutModal()">Uitloggen</b-nav-item> -->
                    <b-button @click="gotoHome()" size="sm" class="my-2 my-sm-0 btn-primary" type="submit">Ga naar Home</b-button>
                    <b-button @click="$bvModal.show('logout-modal')" size="sm" class="my-2 my-sm-0 btn-danger" type="submit">Uitloggen</b-button>

                </b-navbar-nav>

            </b-collapse>

        </b-navbar>
        </div>

<div>

  <b-modal id="logout-modal" hide-footer>
    <template v-slot:modal-title>
      Bevestig
    </template>
    <div class="d-block text-center">
      <h3>Wilt u uitloggen?</h3>
    </div>
    <b-button class="mt-3" block @click="$bvModal.hide('logout-modal')">Ga terug</b-button>
    <b-button class="mt-3" block @click="doLogout()" variant="danger">Logout</b-button>
  </b-modal>
</div>

    </div><!--div-Appheader-->
</template>

<script>

export default {
    name: 'Appheader',
    data () {
    return {
        title: 'Home page'
    }
    },
    mounted: function () {
        // request for full screen
        // document.body.requestFullscreen()
        // console.log(this.$route.name)
    },
    methods: {
        gotoHome: function () {
            this.$router.push({ name: 'Home' })
        },  //END gotoHome
        doLogout: async function () {
            const api_request = require('axios')
            await api_request({
                method: 'post',
                url: this.appSettings.url_logout,
                data: {
                }
            })
                .then(response => {
                    if (response.status) {
                        // console.log(response.status)
                    }
                    // console.log('*******!!!', localStorage.getItem('access-token'))
                    // on Logout remove the tokens
                    // note that refresh token is still valid untill expired,
                    // because we do not have a blacklist for refresh tokens
                    localStorage.removeItem('access-token')
                    localStorage.removeItem('refresh-token')
                    // console.log('logout access token', localStorage.getItem('access-token'))
                    // console.log('logout refresh token', localStorage.getItem('refresh-token'))

                    // Keep other items on localStore, like error report
                    // localStorage.clear()
                    // console.log('DUMMY4')
                    
                    this.user.user_is_logged_in = false
                    this.$router.push({ name: 'Login' }) 
                })
                .catch(() => {
                    // console.log('DUMMY5')
                    // console.log(error)
                    localStorage.removeItem('access-token')
                    localStorage.removeItem('refresh-token')
                    this.user.user_is_logged_in = false
                })
            
            // Reload the  application
            window.location.reload();
        },
        showLogoutModal() {
            this.$refs['logout-modal'].show()
        }
    },
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

<style lang="scss">

</style>
