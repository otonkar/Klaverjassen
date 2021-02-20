<template>

  <div class="Appwheel">

    <b-container>

      <br>
      <h2>Rad van fortuin</h2>

      <hr>
      <button  v-on:click="gotoHome()" class="btn btn-secondary"> Terug naar start pagina  </button>
      <hr>

      <p>
        Stel het aantal vlakken in en geef ieder vlak een naam. Draai daarna het rad.
      </p>

      <hr>


      <!-- <button  v-on:click="doSomething()" class="btn btn-primary"> Get window size  </button>
      {{ window.width }} {{ window.height}}
      <br> <br> -->

      <div id="wheel">
        <!-- <div id="arrow"></div>
        <div id="wrapper"></div> -->
      </div>

      <div class="button_block">

        <div class="button_part">

          <div class="winner">

            <div class="name">  {{ winnerName }} </div>
            <div class="remark"> {{ winnerRemark }} </div>

          </div>

        </div>

        <br><br>

        <div class="button_part">
          <button v-bind:disabled="!activeSpinButton" v-on:click="doSpin()"  class="btn btn-success"> Draai het rad  </button>
        </div>

      </div>


      <hr>

      <button v-if="showSettingsButton" v-on:click="doShowSettings()"  class="btn btn-info"> Toon instellingen  </button>
      <button v-if="!showSettingsButton" v-on:click="doShowSettings()"  class="btn btn-info"> Verberg instellingen  </button>


      <div v-if="showSettings" class="settings"> 

        <br>
        <h5> Laad opgeslagen instellingen: </h5>
        <b-dropdown  id="dropdown-left" menu-class="w-100" v-bind:text="isLoadedDisplay" variant="info" class="m-2">
          <div  v-for="setting in allStoredSettings.data" :key="setting.ID">
            <b-dropdown-item  @click="doLoadSettings(setting.ID)"> {{ setting.name }} </b-dropdown-item>
          </div>
        </b-dropdown>

        <button v-on:click="doSetDefault()" block class="btn btn-warning"> Zet instellingen terug naar standaard  </button>

        <br><br>
        <h5> Bewaar deze instellingen </h5>
        <p>
          Zodra instellingen zijn aangepast kunnen de instellingen worden opgeslagen.
          Als een bestaande naam wordt gekozen dan worden de instellingen overschreven.
        </p>
        <b-form-input v-model="newName"  :state="null" placeholder="Naam" class="namefield"></b-form-input>
        <button v-on:click="postSettings()"  class="btn btn-success mybutton"> Bewaar  </button> 
        <button v-on:click="startDelete()"  class="btn btn-danger mybutton"> Delete  </button>
        <br><br> 

        <!-- Message before delete -->
        <b-jumbotron class="jumbotron" v-bind="{hidden: !show_delete_warning}">
          <h5>Weet u zeker dat u deze instellingen wilt verwijderen? </h5>
          <b-button class="mybutton" variant="danger" @click="stopDelete()">Annuleer</b-button>
          <b-button class="mybutton" variant="success" @click="deleteSettings()">Verwijder</b-button>
        </b-jumbotron>

        


        <div>
          <label for="sb-step">Stel het aantal vlakken in</label>
          <b-form-spinbutton
            id="nSectors"
            v-model="mySettings.nSectors"
            min="4"
            max="36"
            step="1.0"
            v-on:change="doMakeWheel()"
          ></b-form-spinbutton>
        </div>
        <br>

        <!-- <div>
          <label for="sb-step">Stel de duur in van het spinnen</label>
          <b-form-spinbutton
            id="spinTime"
            v-model="spinTime"
            min="3"
            max="30"
            step="1.0"
          ></b-form-spinbutton>
        </div>
        <br> -->

        <div>
          <label for="range-2">Stel de duur in van het spinnen: {{ mySettings.spinTime }} seconden</label>
          <b-form-input id="range-2" 
            v-model="mySettings.spinTime" 
            type="range" 
            min="1" 
            max="30" 
            step="1">
          </b-form-input>
          <!-- <div class="mt-2">Value: {{ spinTime }}</div> -->
        </div>
        <br> 

        <div>
          <label for="range-3">Font reductie factor: {{ mySettings.fontFactor }}</label>
          <b-form-input id="range-3"
            v-on:change="doMakeWheel()" 
            v-model="mySettings.fontFactor" 
            type="range" 
            min="5" 
            max="30" 
            step="1">
          </b-form-input>
          <!-- <div class="mt-2">Value: {{ spinTime }}</div> -->
        </div>
        <br> 

        <div>
          <label for="range-3">Schaal factor grootte van het wiel: {{ mySettings.scaleCircle }}</label>
          <b-form-input id="range-3"
            v-on:change="doMakeWheel()" 
            v-model="mySettings.scaleCircle" 
            type="range" 
            min="0.1" 
            max="2.0" 
            step="0.1">
          </b-form-input>
          <!-- <div class="mt-2">Value: {{ spinTime }}</div> -->
        </div>
        <br>

        <b-container fluid>

          <b-row class="my-1">
            <b-col sm="4">
              <span>Veld</span>
            </b-col>
            <b-col sm="8">
              <span>Toelichting</span>
            </b-col>
          </b-row>

          <b-row class="my-1" v-for="index in mySettings.nSectors" :key="index">
            <b-col sm="4">
              <b-form-input v-model="myInput[index-1].name" v-on:change="doMakeWheel()"  :state="null" placeholder="Naam"></b-form-input>
            </b-col>
            <b-col sm="8">
              <b-form-input v-model="myInput[index-1].remark" :state="null" placeholder="Omschrijving"></b-form-input>
            </b-col>
          </b-row>

        </b-container>

      </div>

      <br> 
      <hr>
        <button  v-on:click="gotoHome()" class="btn btn-secondary"> Terug naar start pagina  </button>
      <hr>
      <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> 

    </b-container>

  </div>
</template>



<script>

export default {
  name: 'Appwheel',

  data () {
    return {
      test: {},
      activeSpinButton: true,       // only active when wheel is not spinning
      showSettingsButton: true,     // Show the button
      showSettings: false,          // Show the settings fields
      show_delete_warning: false,   // show the jumbotron warning for delete settings
      window: {
        width: 0,
        height: 0,
      },
      winnerName    : '??????',     // Winner name after spinning the wheel
      winnerRemark  : '------',     // Winner remark after spinning the wheel
      wrapper       : {},           // wrapper DOM element
      spinTime      : 10,           // Time in seconds for the spin duration (this is also nSpin)
      defaultSettings : {           // Default settings of the wheel
        nSectors      : 5,          // number of equal sectors in the circle, Set to >= 4
        scaleCircle   : 0.9,        // Percentage of screen that must be filled by the wheel 
        fontFactor    : 18,         // Factor between diameter and fontsize
        arrowFactor   : 18,         // relative size of arrow compared to diameter
        spinTime      : 10,         // Time in seconds for the spin duration (this is also nSpin)
        spinFactor    : 1,          // factor number of 360 spins per time:  nSpin = spinFactor * spinTime
      },
      allStoredSettings   : {
        data: {},
      },                            // Get list of all stored settings
      newName             : '',     // Set the name of the Settings to be stored
      isLoadedDisplay     : 'selecteer ...',     // Deplay name of the loaded settings
      isLoadedID          : '',     // ID of the loaded settings
      mySettings    : {},           // Current settings that apply to the wheel
      myInput       : [],           // Person input for name, remarl and color
      defaultInput   :  [
        {'name': 'Opdracht 1',  'remark': 'Doe iets geks',            'color': '#dbe2bc'},
        {'name': 'Opdracht 2',  'remark': 'Doe iets heel geks',       'color': '#e7706f'},
        {'name': 'Opdracht 3',  'remark': 'Doe iets extreem geks',    'color': '#eae56f'},
        {'name': 'Opdracht 4',  'remark': 'Doe iets bijzonder geks',  'color': '#89f26e'},
        {'name': 'Opdracht 5',  'remark': 'Doe iets kei geks',        'color': '#7de6ef'},
        {'name': 'Opdracht 6',  'remark': 'Doe iets zeer geks',       'color': '#e7706f'},
        {'name': 'Opdracht 7',  'remark': 'Doe iets super geks',      'color': '#eae56f'},
        {'name': 'Opdracht 8',  'remark': 'Doe eens normaal',         'color': '#89f26e'},
        {'name': 'Opdracht 9',  'remark': 'opmerking 9',  'color': '#7de6ef'},
        {'name': 'Opdracht 10', 'remark': 'opmerking 10', 'color': '#e7706f'},
        {'name': 'Opdracht 11', 'remark': 'opmerking 11', 'color': '#eae56f'},
        {'name': 'Opdracht 12', 'remark': 'opmerking 12', 'color': '#89f26e'},
        {'name': 'Opdracht 13', 'remark': 'opmerking 13', 'color': '#7de6ef'},
        {'name': 'Opdracht 14', 'remark': 'opmerking 14', 'color': '#e7706f'},
        {'name': 'Opdracht 15', 'remark': 'opmerking 15', 'color': '#eae56f'},
        {'name': 'Opdracht 16', 'remark': 'opmerking 16', 'color': '#89f26e'},
        {'name': 'Opdracht 17', 'remark': 'opmerking 17', 'color': '#7de6ef'},
        {'name': 'Opdracht 18', 'remark': 'opmerking 18', 'color': '#e7706f'},
        {'name': 'Opdracht 19', 'remark': 'opmerking 19', 'color': '#eae56f'},
        {'name': 'Opdracht 20', 'remark': 'opmerking 20', 'color': '#89f26e'},
        {'name': 'Opdracht 21', 'remark': 'opmerking 21', 'color': '#7de6ef'},
        {'name': 'Opdracht 22', 'remark': 'opmerking 22', 'color': '#e7706f'},
        {'name': 'Opdracht 23', 'remark': 'opmerking 23', 'color': '#eae56f'},
        {'name': 'Opdracht 24', 'remark': 'opmerking 24', 'color': '#89f26e'},
        {'name': 'Opdracht 25', 'remark': 'opmerking 25', 'color': '#7de6ef'},
        {'name': 'Opdracht 26', 'remark': 'opmerking 26', 'color': '#e7706f'},
        {'name': 'Opdracht 27', 'remark': 'opmerking 27', 'color': '#eae56f'},
        {'name': 'Opdracht 28', 'remark': 'opmerking 28', 'color': '#89f26e'},
        {'name': 'Opdracht 29', 'remark': 'opmerking 29', 'color': '#7de6ef'},
        {'name': 'Opdracht 30', 'remark': 'opmerking 30', 'color': '#e7706f'},
        {'name': 'Opdracht 31', 'remark': 'opmerking 31', 'color': '#eae56f'},
        {'name': 'Opdracht 32', 'remark': 'opmerking 32', 'color': '#89f26e'},
        {'name': 'Opdracht 33', 'remark': 'opmerking 33', 'color': '#7de6ef'},
        {'name': 'Opdracht 34', 'remark': 'opmerking 34', 'color': '#e7706f'},
        {'name': 'Opdracht 35', 'remark': 'opmerking 35', 'color': '#eae56f'},
        {'name': 'Opdracht 36', 'remark': 'opmerking 36', 'color': '#89f26e'},
      ],
    }
  },

  created() {
      window.addEventListener('resize', this.doResize);

  },

  destroyed() {
      window.removeEventListener('resize', this.doResize);
  },

  activated: async function () {
      this.user.show_header = true
      this.$store.dispatch('updateUser', this.user)

      if (this.user.user_is_logged_in === false) {
          this.$router.push({ name: 'Home' })
      } else {

        //Check that screen is mobile. If so, set full screen
        var isMobile = /Android/i.test(navigator.userAgent);
        if (isMobile) {
          // document.body.requestFullscreen()
          document.documentElement.requestFullscreen()
        }

        // !!! Copy objects in special way, otherwise both object refer to same content and are linked
        this.mySettings = JSON.parse(JSON.stringify(this.defaultSettings));
        this.myInput    = JSON.parse(JSON.stringify(this.defaultInput));
        
        this.doMakeWheel();
        this.doSetDefault();

      }
  },//END mounted
  methods: {
    gotoHome: function () {
        this.$router.push({ name: 'Home' })

        let message = 'BackTo Start'
        this.logButton(message)
    },  //END gotoLogin

    doSleep: async function (ms) {
          // To wait some time. Use in a async function
          return new Promise(resolve => setTimeout(resolve, ms));
        }, //END doSleep 

    doResize() {
        this.window.width = window.innerWidth;
        this.window.height = window.innerHeight;

        this.doMakeWheel();
    },

    doShowSettings: function () {
      this.showSettingsButton = !this.showSettingsButton
      this.showSettings = !this.showSettings

    },

    doSetDefault: function () {
      this.mySettings = JSON.parse(JSON.stringify(this.defaultSettings));
      this.myInput = JSON.parse(JSON.stringify(this.defaultInput));

      this.isLoadedDisplay  = 'selecteer ...'
      this.isLoadedID       = ''
      this.newName          = ''

      // Refresh the dropdown list
      this.getSettings()

      this.doMakeWheel();
    },

    doMakeWheel: async function () {

      // First clean all created childs from previous doMakeWheel.
      // This to support the resize that needs to rebuild the page.
      var wheel	 	= document.getElementById('wheel'); 
      while (wheel.firstChild) {
        wheel.removeChild(wheel.firstChild);
      }
      
      // wheel.querySelectorAll('*').forEach(n => n.remove());

      var topMargin = 0 ; // (1-this.mySettings.scaleCircle)/2;      // margin at top of wheel
      var angle = 360.0/(this.mySettings.nSectors);       // angle per sector
      var diameter = 0;                                   // Initialize the diameter

      // Get the elements on the screen
      // var wheel	 	= document.getElementById('wheel'); 

      // Get the actual width of the wheel in px.
      var wheelWidht  = wheel.offsetWidth;

      // use factor 0,7 so that vertically there will remain some more space around the wheel
      if (wheelWidht >= 0.7 * window.innerHeight) {
        diameter = window.innerHeight * this.mySettings.scaleCircle * 0.7;
      } else {
        diameter =  wheelWidht * this.mySettings.scaleCircle;
      }

      // Determine the fontsize of the text in the wheel
      var fontSize = diameter/this.mySettings.fontFactor;

      wheel.style.width               = '100%';
      wheel.style.height              = diameter*1.1 + 'px';
      // wheel.style.backgroundColor     = 'orange';

            /// Arrow is the indicator at the wheel
      var arrow	 	                    = document.createElement("div");
      arrow.id                        = 'arrow';
      arrow.style.width               = diameter/this.mySettings.arrowFactor + 'px';
      arrow.style.height              = diameter/this.mySettings.arrowFactor + 'px';
      arrow.style.left                = wheelWidht/2 - diameter/(this.mySettings.arrowFactor*2) + 'px';
      arrow.style.top			            = -diameter/(this.mySettings.arrowFactor*2) + 'px';
      arrow.style.position            = 'relative';
      arrow.style.border              = 'solid red';
      arrow.style.borderWidth         = '0 6px 6px 0';
      arrow.style.boxSizing           = 'border-box';
      arrow.style.display             = 'block';
      arrow.style.transform           = 'rotate(45deg)';
      wheel.appendChild(arrow);

      // Set wrapper values.
      // non dynamic value will be set in css.
      this.wrapper	 	                     = document.createElement("div"); 
      this.wrapper.id                      = 'wrapper';
      this.wrapper.style.width             = diameter + 'px';
      this.wrapper.style.height            = diameter + 'px';
      this.wrapper.style.left 						 = wheelWidht/2 - 0.5*diameter + 'px';
      this.wrapper.style.top               = topMargin * diameter + 'px';
      this.wrapper.style.backgroundColor   = 'lightgray';
      this.wrapper.style.borderRadius      =  '50%';
      this.wrapper.style.position          = 'relative';
      this.wrapper.style.boxSizing         = 'border-box';
      this.wrapper.style.overflow          = 'hidden';

      // this.wrapper.onclick = this.doSpin(this.wrapper) ;
      wheel.appendChild(this.wrapper);


      // Create a base Sector with values that apply to all sectors of the circle. 
      var sector 	 	                = document.createElement("div"); 
      sector.style.position 				= 'absolute';
      sector.style.width 						= diameter*0.6 + 'px';
      sector.style.height 					= diameter*0.6 + 'px';  // Increase so that corners are not visible
      sector.style.border						= '1px solid grey'
      // sector.style.backgroundColor 	= 'red'
      sector.style.transformOrigin 	= "0 100%";
      sector.style.left 						= diameter*0.5 + 'px';
      sector.style.top							= -diameter*0.1 + 'px';


      // Create an array to store all sectors of the circle
      let sectors = [];

      // Each sector will be rotated 
      for (var i = 0; i < (this.mySettings.nSectors); i++) {
        sectors[i] = sector.cloneNode(true);
        sectors[i].style.transform			= `rotate(${-i*angle}deg) skew(-${90-angle}deg)`;
        sectors[i].style.backgroundColor = this.myInput[i].color
        // sectors[i].classList.add('sectors');
        
        this.wrapper.appendChild(sectors[i]);   
      }


      // Create the base elements to store text in a sector
      var myText 	 	                = document.createElement("span");
      myText.style.position 				= 'absolute';
      myText.style.width						= diameter*0.5-fontSize/2 + 'px';
      myText.style.height = '20px;'
      myText.style.textAlign 				= 'right';
      myText.style.padding					= '0px 0px 0px 0px';
      myText.style.fontFamily				= 'Arial';
      myText.style.color            = 'black';
      myText.style.fontSize					= fontSize + 'px';
      myText.style.fontWeight				= 'bold';
      myText.style.zIndex           = "10";
      myText.style.transformOrigin 	= "0 " + fontSize/2 + "px";
      myText.style.left 						= diameter*0.5 + 'px';
      myText.style.top							= diameter*0.5-fontSize/1.5 + 'px'
      // myText.style.border						= '1px solid blue'
      myText.style.transform				= `rotate(-${2*angle + angle/2}deg)`;


      // Array to store the text elements for the sectors
      let texts = [];

      for (i = 0; i < (this.mySettings.nSectors); i++) {
        texts[i] = myText.cloneNode(true);
        texts[i].style.transform			= `rotate(-${i*angle + angle/2}deg)`;
        texts[i].style.color          = 'black';
        texts[i].innerHTML            = this.myInput[i].name;

        this.wrapper.appendChild(texts[i]);
        
      }

    }, //END doMakeWheel

    doSpin: async function () {

      this.activeSpinButton = false;
      this.winnerName       = '??????';
      this.winnerRemark     = '------'

      var angle = 360.0/(this.mySettings.nSectors);            // angle per sector

      // console.log('click to Spin')

      // Get the elements on the screen
      // var wrapper	 	= document.getElementById('wrapper'); 

      // reset rotation
      this.wrapper.style.transition	= 'transform 0.01s';
      this.wrapper.style.WebkitTransition = 'transform 0.01s';
      this.wrapper.style.transform		= 'rotate(0deg)';
      await this.doSleep(500);

      // Random value [0 -360] degrees for spin
      var rand = Math.floor(Math.random() * 360 );

      // Totaal rotation including random part
      // Take spinTime and nSpin the same, so that 1 cycle per second
      var totRotation = rand + this.mySettings.spinTime * this.mySettings.spinFactor * 360;

      // Selector arrow on middle line
      // var selected = Math.floor(rand/angle)

      // Selector arrow on middle top. needs to add 90 degrees in calculation
      // By adding 90deg rand+90 can be greater than 360, so look at remainder
      var remainder = (rand + 90) % 360
      var selected = Math.floor(remainder/angle)
      // console.log(rand, angle, remainder, selected, inputText[selected])

      // Rotate
      this.wrapper.style.transition	= `transform ${this.mySettings.spinTime}s`;
      this.wrapper.style.WebkitTransition = `transform ${this.mySettings.spinTime}s`;
      this.wrapper.style.transform		= `rotate(${totRotation}deg)`;

      await this.doSleep(this.mySettings.spinTime*1000 + 500)
      this.winnerName = this.myInput[selected].name
      this.winnerRemark = this.myInput[selected].remark
      // alert('Winnaar: ' + this.winner )



      this.activeSpinButton = true;
      
    }, // End doSpin

    getSettings: async function () {
      // get the list of settings
      const api_request = require('axios')

      await api_request({
          method: 'get',
          url: this.appSettings.url_wheel,
      })
        .then(response => {
          if (response) {
            this.allStoredSettings = response.data
            // console.log(this.allStoredSettings)
          }


        })
        .catch(() => {
            // alert('Fout')
            // console.log('Fout bij het ophalen van de wedstrijdlijst')
        })

    },

    postSettings: async function () {
      // make sure the request  WILL use the interceptors
      const api_request = require('axios')

      if (this.newName === '') {
        alert('Vul een naam in.')
        return
      }

      var doUpdate = false

      // Check that the newName already exists
      for (var setting in this.allStoredSettings.data) {
        if (this.allStoredSettings.data[setting].name === this.newName) {
          // alert('Deze naam bestaat al. Kies een andere naam')
          // return
          doUpdate = true
        }
      }

      var myData = {
        name          : this.newName,
        user          : 'xxxxx',
        userSettings  : this.mySettings,
        userInput     : this.myInput
      }

      // In case of Update
      if (doUpdate) {

        await api_request({
            method: 'put',
            url: this.appSettings.url_wheel + this.isLoadedID + '/',
            data: myData
        })
          .then(response => {
            if (response) {
              // console.log(response.data)
              alert('Instellingen aangepast voor : ' + this.newName);
              // this.newName = '';

              // Refresh the dropdown list
              this.getSettings()
            }


          })
          .catch(() => {
              // alert('Fout')
              // console.log('Fout bij het ophalen van de wedstrijdlijst')
          })
      
      } else {

        await api_request({
            method: 'post',
            url: this.appSettings.url_wheel,
            data: myData
        })
          .then(response => {
            if (response) {
              // console.log(response.data)
              alert('Instellingen bewaard voor : ' + this.newName);

              // Refresh the dropdown list
              this.getSettings()
            }


          })
          .catch(() => {
              // alert('Fout')
              // console.log('Fout bij het ophalen van de wedstrijdlijst')
          })

      } //END else

    },

    startDelete: function () {
      this.show_delete_warning = true

    },

    stopDelete: function () {
      this.show_delete_warning = false
    },

    deleteSettings: async function () {
      // delete the settings
      const api_request = require('axios')

      this.show_delete_warning = false

      if (this.newName === '') {
        alert('Laad eerst bestaande instellingen.')
        return
      }

      var isValidID = false

      // Check that the newName and isLoaded belong to the same settings
      for (var setting in this.allStoredSettings.data) {
        if (this.allStoredSettings.data[setting].name === this.newName) {
          if (this.allStoredSettings.data[setting].ID === this.isLoadedID) {
            isValidID = true
          }

        }
      }

      if (!isValidID) {
        alert('De naam de van instellingen komt niet overeen met de huidige geladen instellingen. \
        \nLaad de instellingen eerst opnieuw.')
        return
      }

      await api_request({
          method: 'delete',
          url: this.appSettings.url_wheel + this.isLoadedID + '/',
      })
        .then(response => {
          if (response) {
            alert('Instellingen verwijderd voor : ' + this.newName);

            // Reset display values
            this.isLoadedDisplay  = 'selecteer ...'
            this.isLoadedID       = ''
            this.newName          = ''

            // Refresh the dropdown list
            this.getSettings()
          }


        })
        .catch(() => {
            // alert('Fout')
            // console.log('Fout bij het ophalen van de wedstrijdlijst')
        })

    },

    doLoadSettings: function (selected) {
      // Load the selected settings based on ID


      var selectedSettings = {};

      for (var setting in this.allStoredSettings.data) {
        if (this.allStoredSettings.data[setting].ID === selected) {
          selectedSettings = this.allStoredSettings.data[setting]
        }
      }

      // console.log(selectedSettings.ID, selectedSettings.name)
      // console.log(selectedSettings.userSettings)

      this.mySettings = JSON.parse(selectedSettings.userSettings);
      this.myInput    = JSON.parse(selectedSettings.userInput);

      this.isLoadedDisplay  = selectedSettings.name
      this.isLoadedID       = selectedSettings.ID

      // Set newName to the current loaded settings, so that by default these
      // settings can be updated
      this.newName = selectedSettings.name

      this.doMakeWheel();
    

    },

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

<style scoped lang='scss'>

.button_block {
  width: 100%;
  margin: auto;
  // border: 2px solid blue;
  text-align: center;
}

.button_part {
  display: inline-block;
  // width: 100%;
  margin: 0px 10px 0px 10px;
  // border: 2px solid red;
  text-align: center;
}

.namefield {
  max-width: 200px;
}

.mybutton {
  margin: 10px 40px 0px 0px;
}

.winner {
  width: 100%;
  // margin: 0px auto 20px auto;
  text-align: center;
}

.name {
  color: darkblue;
  font-size: 30px;
  font-weight: bold;
}

.remark {
  color: blue;
  font-size: 20px;
  font-weight: bold;
}

// #wheel {
// }

// #wrapper {
// 	// width: 300px;
// 	// height: 300px;
// 	// border: 3px solid blue;
// 	border-radius: 50%;
//   position: relative;
//   box-sizing: border-box;
//   overflow: hidden;
//   // background: lightgray;
// }

// .sector {
//   // background-color: yellow;
//   border: 1px solid blue;
//   // box-sizing: border-box;
// }

// .sector {
//   background: #ccc;
//   // border: 1px solid red;
//   box-sizing: border-box;

//   &:nth-child(4n) {
//     background:#eae56f;
//   }

//   &:nth-child(4n+1) {
//     background:#89f26e;
//   }

//   &:nth-child(4n+2) {
//     background:#7de6ef;
//   }

//   &:nth-child(4n+3) {
//     background:#e7706f;
//   }

//   // &:nth-child(odd) {
//   //   background:red;
//   // }

//   // &:nth-child(even) {
//   //   background: green;
//   // }

//   &:nth-child(1) {
//     background:lighten( green, 20% );
//     background:lighten( rgb(119, 195, 117), 20% );
//   }

//   // &:hover {
//   //   background: gold;
//   //   ;
//   // }

// }

// #arrow {
//   // width: 30px;
//   // height: 30px;
//   position: relative;
//   border: solid red;
//   border-width: 0 6px 6px 0;
//   box-sizing: border-box;
//   display: block;
//   // top: -100px;
//   // padding: 3px;
//   transform: rotate(45deg);
//   -webkit-transform: rotate(45deg);
// }


</style>
