<template>
  <div class="Appremarks">

    <b-container v-if="isLoaded">

        <br>
        <h2> Berichten </h2>

        <hr>
        <b-col><b-button v-on:click="gotoHome()"  class="btn btn-secondary"> Terug naar start pagina  </b-button></b-col>
        <hr>

        <p>
          Op deze pagina kan de beheerder berichten plaatsen. 
          Ook kunnen gebruikers van dit spel opmerkingen plaatsen of feedback geven, zoals:
          <ul>
            <li>het delen van eigen ervaringen met het spelen van dit spel</li>
            <li>het melden van bugs</li>
            <li>het geven van tips en suggesties voor verbeteringen</li>
            <li>het stellen van vragen</li>
          </ul>
        </p>
        <hr>

          <!-- Show confirm send feedback  -->
        <b-jumbotron class="jumbotron" v-bind="{hidden: !show_confirm_create_remark}">
          <p> Weet je zeker dat je de opmerking wilt plaatsen?</p>
          <p> 
            {{ remarkText }}
          </p>
          <br>
          <b-row>
              <b-col><b-button block @click="show_confirm_create_remark = !show_confirm_create_remark"  class="btn btn-danger"> Nee  </b-button></b-col>
              <b-col><b-button block v-on:click="doCreateRemark()"  class="btn btn-success"> Ja  </b-button></b-col>
          </b-row>
        </b-jumbotron>

        <h4> Maak nieuw bericht </h4>

        <div>
          <b-form-textarea
          id="textarea"
          v-model="remarkText"
          placeholder="Schrijf hier uw bericht"
          rows="3"
          max-rows="6"
          ></b-form-textarea>

        </div>
        <br>

        <b-row>
            <b-col><b-button block @click="doStopRemark()"  class="btn btn-warning"> Verwijder tekst  </b-button></b-col>
            <b-col><b-button block @click="doStartRemark()" variant="primary"  class="btn"> Plaats bericht </b-button></b-col>
        </b-row>
        <hr>

        <h4> Overzicht berichten </h4>

        <div v-for="remark in remarks" v-bind:key="remark.remarkID">
          <p>
            Bericht: {{remark.remarkID }} <br>
            gemaakt door: <b>{{ remark.user.username }}</b>, 
            {{remark.date_created}}
          </p>
          <div>
            <b-form-textarea
              id="textarea"
              v-model="remark.remark"
              rows="3"
              max-rows="6"
            ></b-form-textarea>

          </div>
          <hr>
        </div>

        <b-col><b-button v-on:click="gotoHome()"  class="btn btn-secondary"> Terug naar start pagina  </b-button></b-col>
        <hr>


    </b-container>

  </div>
</template>

<script>
// import Appgamedetails from '../components/Game_details.vue'


export default {
  name: 'Appremarks',
  // components: {
  //   'app-gamedetails': Appgamedetails
  // },
  data () {
    return {
        isLoaded: false,          // to rerender the page when data is loaded
        remarkText: '',           // Text that contains the remark
        remarks: [],               // List of all remarks
        show_confirm_create_remark: false,    // Show the warning that remark is created
    }
  },

  // Do not use mounted, otherwise no new game will be loaded
  activated: async function () {
      document.title = 'Klaverjasfun'

      if (this.user.user_is_logged_in === false) {

            this.$router.push({ name: 'Home' })

      } else {

        //Check that screen is mobile. If so, set full screen
        var isMobile = /Android/i.test(navigator.userAgent);
        if (isMobile) {
          // document.body.requestFullscreen()
          document.documentElement.requestFullscreen()
        }

        this.doGetRemarks();
        this.isLoaded = true;

      }//END if
  },//END activated
  methods: {

    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    },  //END gotoLogin

    doStartRemark: function () {

      if (this.remarkText.length !== 0) {
        this.show_confirm_create_remark = true
      } else {
        alert('Vul eerst de feedback opmerking in.');
      }
    },

    doStopRemark: function () {
        this.remarkText = ''
    },  //END doStopRemark


    doGetRemarks: async function () {

      // Do  use 'api_request' or axios, so that this call WILL use the interceptors
      const api_request = require('axios')

      await api_request({
            method: 'get',
            url: this.appSettings.url_remarks_list,
        })
      .then(response => {
          if (response.status === 200) {
              this.remarks = response.data
          }
      })
      .catch(error => {
      })

    },  //END doCreateRemark

    doCreateRemark: async function () {

      // Do  use 'api_request' or axios, so that this call WILL use the interceptors
      const api_request = require('axios')

      if (this.remarkText.length !== 0) {

        this.show_confirm_create_remark = false

        await api_request({
          method: 'post',
          url: this.appSettings.url_remarks_create,
          data: {
              user: this.user.id,
              remark: this.remarkText,
          }
        })
        .then(response => {
          if (response.status === 201) {
              alert('Opmerking is opgeslagen');
              this.remarkText = '';
              this.doGetRemarks();
          }
        })
        .catch(error => {
          alert('Opmerking is niet opgeslagen door een fout.');
        })

      } else {
          alert('Vul eerst de feedback opmerking in.');
      }
        
    },  //END doCreateRemark

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
