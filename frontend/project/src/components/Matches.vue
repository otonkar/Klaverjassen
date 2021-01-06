<template>
  <div class="Appmatches">

    <b-container>

      <br>
      <h2>Wedstrijden</h2>

      <hr>
      <button  v-on:click="gotoHome()" class="btn btn-secondary"> Terug naar start pagina  </button>
      <hr>


      <div>
        <b-button v-on:click="gotoMatchList()" block variant="info">Overzicht wedstrijden</b-button>
        <b-button v-on:click="gotoMatchCreate()" block variant="info">Nieuwe wedstrijd maken</b-button>
      </div>

      <br>
      <hr>
      
      <!-- <button  v-on:click="$router.go(-1)" class="btn btn-primary"> Ga naar home pagina  </button> -->

    </b-container>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Appmatches',
  data () {
    return {
      title: 'Matches page',
      test: {},
      result_test: {}
    }
  },
  activated: function () {
      // console.log(this.$route.name)
      // Do not show full screen on login page
      // document.exitFullscreen();
      this.user.show_header = true
      this.$store.dispatch('updateUser', this.user)

      if (this.user.user_is_logged_in === false) {
          this.$router.push({ name: 'Home' })
      } else {

        //Check that screen is mobile. If so, set full screen
        var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
        if (isMobile) {
          // document.body.requestFullscreen()
          document.documentElement.requestFullscreen()
        }

      }
  },//END mounted
  methods: {
    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    },  //END gotoLogin
    gotoMatchCreate: function () {
      this.$router.push({ name: 'Match_create' })
    },  //END gotoMatchCreate
    gotoMatchList: function () {
      this.$router.push({ name: 'Match_list' })
    },  //END gotoMatchList
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
