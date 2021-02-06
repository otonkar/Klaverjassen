<template>
  <div class="Appplaydices">

    <b-container>

      <br>
      <h2>Gooi dobbelstenen</h2>

      <hr>
      <button  v-on:click="gotoHome()" class="btn btn-secondary"> Terug naar start pagina  </button>
      <hr>

      <p>
        Gooi met 1 of meerdere dobbelstenen
      </p>

      <div>
        <b-dropdown
          variant="primary"
          text="Kies aantal dobbelstelen"
          class="m-2"
        >
          <b-dropdown-item @click="setDices(1)">1 steen</b-dropdown-item>
          <b-dropdown-item @click="setDices(2)">2 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(3)">3 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(4)">4 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(5)">5 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(6)">6 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(7)">7 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(8)">8 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(9)">9 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(10)">10 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(11)">11 stenen</b-dropdown-item>
          <b-dropdown-item @click="setDices(12)">12 stenen</b-dropdown-item>
        </b-dropdown>
      </div>
      <br>

      <div class="dices">

        <div id="dice1" class="my_dice">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice2" class="my_dice" v-if="nDice >= 2">
          <app-dice  class="comp_dice"></app-dice>
        </div> 
        <div id="dice3"  class="my_dice" v-if="nDice >= 3">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice4" class="my_dice" v-if="nDice >= 4">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice5" class="my_dice" v-if="nDice >= 5">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice6"  class="my_dice" v-if="nDice >= 6">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice7"  class="my_dice" v-if="nDice >= 7">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice8"  class="my_dice" v-if="nDice >= 8">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice9"  class="my_dice" v-if="nDice >= 9">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice10"  class="my_dice" v-if="nDice >= 10">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice11"  class="my_dice" v-if="nDice >= 11">
          <app-dice class="comp_dice"></app-dice>
        </div>
        <div id="dice12"  class="my_dice" v-if="nDice >= 12">
          <app-dice class="comp_dice"></app-dice>
        </div>
        
        
      </div>

      <br>
      <div class="button_block">
        <div class="button_part">
          <button v-bind:disabled="!activeThrowbutton"  v-on:click="doRollDice()" class="btn btn-success"> Gooi de dobbelstenen  </button>
        </div>
        <!-- <div class="button_part">
          <button v-bind:disabled="!activeTossButton"  v-on:click="doRestart()" class="btn btn-warning"> Start opnieuw  </button>
        </div> -->
      </div>


      <div id="jumpTo"></div>

      <hr>
        <button  v-on:click="gotoHome()" class="btn btn-secondary"> Terug naar start pagina  </button>
      <hr>
      

    </b-container>

  </div>
</template>

<script>
// @ is an alias to /src
import Appdice from '../components/Dice.vue'

export default {
  name: 'Appplaydices',
  components: {
    'app-dice': Appdice
  },

  data () {
    return {
      test: {},
      activeThrowbutton: true,
      nDice: 2,
    }
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

    setDices: function (N) {
      this.nDice = N
    },


    doRollDice: async function () {
      
        var random = [];
        this.activeThrowbutton = false;

        
        // Set random value per dice
        for (var i = 1; i <= this.nDice; i++) {
          random[i-1] = Math.floor((Math.random() * 6) + 1);
        }

        // Sort the dices
        random.sort()

        // Set dice to original position quickly before rthrowing
        for (var i = 1; i <= this.nDice; i++) {
          document.getElementById('dice' + i.toString()).style.transition = "transform 0.01s";
          document.getElementById('dice' + i.toString()).style.transform = "rotateX(-10deg) rotateY(10deg) rotateZ(0deg)"
        }

        await this.doSleep(150)

        // Set dice to new position
        for (var i = 1; i <= this.nDice; i++) {
          document.getElementById('dice' + i.toString()).style.transition = "transform 2s";
          var nTurnsx = 2;
          var nTurnsy = 3;
          var nTurnsz = 2;

          if (random[i-1] === 1) {
            document.getElementById('dice' + i.toString()).style.transform = 
              "rotateX(" +  (nTurnsx*360-10).toString() + "deg) rotateY(" +  (nTurnsy*360+10).toString() + "deg) rotateZ(" +  (nTurnsz*360).toString() + "deg)"
          }

          if (random[i-1] === 2) {
            document.getElementById('dice' + i.toString()).style.transform = 
              "rotateX(" +  (nTurnsy*360-100).toString() + "deg) rotateY(" +  (nTurnsx*360).toString() + "deg) rotateZ(" +  (nTurnsz*360+10).toString() + "deg)"
          }

          if (random[i-1] === 3) {
            document.getElementById('dice' + i.toString()).style.transform = 
              "rotateX(" +  (nTurnsz*360).toString() + "deg) rotateY(" +  (nTurnsy*360-80).toString() + "deg) rotateZ(" +  (nTurnsx*360+10).toString() + "deg)"
          }

          if (random[i-1] === 4) {
            document.getElementById('dice' + i.toString()).style.transform = 
              "rotateX(" +  (nTurnsx*360).toString() + "deg) rotateY(" +  (nTurnsy*360+100).toString() + "deg) rotateZ(" +  (nTurnsz*360-10).toString() + "deg)"
          }

          if (random[i-1] === 5) {
            document.getElementById('dice' + i.toString()).style.transform = 
              "rotateX(" +  (nTurnsy*360+80).toString() + "deg) rotateY(" +  (nTurnsz*360).toString() + "deg) rotateZ(" +  (nTurnsz*360-10).toString() + "deg)"
          }

          if (random[i-1] === 6) {
            document.getElementById('dice' + i.toString()).style.transform = 
              "rotateX(" +  (nTurnsz*360+170).toString() + "deg) rotateY(" +  (nTurnsx*360-10).toString() + "deg) rotateZ(" +  (nTurnsy*360).toString() + "deg)"
          }

          // Set to side 1
          // document.getElementById('dice' + i.toString()).style.transform = "rotateX(350deg) rotateY(370deg) rotateZ(360deg)"
          //2
          // document.getElementById('dice' + i.toString()).style.transform = "rotateX(-100deg) rotateY(0deg) rotateZ(10deg)"
          //3
          // document.getElementById('dice' + i.toString()).style.transform = "rotateX(0deg) rotateY(-80deg) rotateZ(10deg)"
          //4
          // document.getElementById('dice' + i.toString()).style.transform = "rotateX(0deg) rotateY(100deg) rotateZ(-10deg)"
          //5
          // document.getElementById('dice' + i.toString()).style.transform = "rotateX(80deg) rotateY(0deg) rotateZ(-10deg)"
          // Set to side 6
          // document.getElementById('dice' + i.toString()).style.transform = "rotateX(170deg) rotateY(-10deg) rotateZ(0deg)"
        }

        await this.doSleep(2000)

        this.activeThrowbutton = true;


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

// Define variables
$image_width: 160px;
$image_height: 160px;

.dices {
  display: block;
  // position: absolute;
  // top: 0px;
  margin: 0px;
  // width: 200%;
  // border: 2px solid blue;
}

.my_dice {
  display: inline-block;
  // margin: 20px 20px 40px 20px; 
  margin: 40px 20px 30px 20px;
  width: 100px;
  height: 100px;
  // border: 2px solid red;
  transform-style: preserve-3d;
  transform: rotateX(-10deg) rotateY(10deg) rotateZ(0deg);
 

}

.comp_dice {
  display: inline-block;
  width: 100px;
  height: 100px;
  // border: 2px solid green;
  transform-style: preserve-3d;
	// transform: rotateX(-102deg) rotateY(0deg) rotateZ(12deg) scale3d(0.5, 0.5, 0.5);
  transform: scale3d(0.5, 0.5, 0.5) translate(-50px, -50px);
}



</style>
