<template>
  <div class="Apptestluck">

    <b-container>

      <br>
      <h2>Test jouw geluk</h2>

      <hr>
      <button  v-on:click="gotoHome()" class="btn btn-secondary"> Terug naar start pagina  </button>
      <hr>


      
      <p>
        Hoeveel geluk heb jij? Test dit door een munt te tossen. Doel is om zo vaak mogelijk 'KOP' te krijgen.
        Na iedere poging wordt het percentage getoond van de mensen die minder vaak 'KOP' zou krijgen dan jij.
      </p>

      <p>
        Tos de munt meerdere malen. Probeer zo lang mogelijk een hoge score te houden. 
        Bij een hoger aantal pogingen zal normaal gesproken het percentage naar de 50% gaan. 
        Ben jij die geluksvogel die na 100 keer tossen een score van 95% of hoger kan halen, waarmee je 
        tot de top 5% behoort?
      </p>
      <p>
        Druk op de groene knop om de munt te tossen. 
        Je kan opnieuw beginnen door op de knop 'Start opnieuw' te drukken. 
        Hiermee wordt de score opgeslagen en de tellers weer op nul gezet.
      </p>
      <hr>

      <div class="counter_main">

        <div class="counter_block">

          <div class="counter_header">Pogingen</div>

          <div class="counter" id="id_counter">
            <div class="number" id="id_number"> {{ strnToss[0] }} </div>
            <div class="number" id="id_number"> {{ strnToss[1] }} </div>
            <div class="number" id="id_number"> {{ strnToss[2] }} </div>
            <div class="number" id="id_number"> {{ strnToss[3] }}</div>
          </div>

        </div>

        <div class="counter_block">

          <div class="counter_header">Kop</div>

          <div class="counter" id="id_counter">
            <div class="number" id="id_number"> {{ strnHeads[0] }} </div>
            <div class="number" id="id_number"> {{ strnHeads[1] }} </div>
            <div class="number" id="id_number"> {{ strnHeads[2] }} </div>
            <div class="number" id="id_number"> {{ strnHeads[3] }}</div>
          </div>

        </div>



          <!-- <div class="counter" id="id_counter">
            <div class="number" id="id_number"> {{ strnToss[0] }} </div>
            <div class="number" id="id_number"> {{ strnToss[1] }} </div>
            <div class="number" id="id_number"> {{ strnToss[2] }} </div>
            <div class="number" id="id_number"> {{ strnToss[3] }}</div>
          </div>

          <div class="counter" id="id_counter">
            <div class="number" id="id_number"> {{ strnHeads[0] }} </div>
            <div class="number" id="id_number"> {{ strnHeads[1] }} </div>
            <div class="number" id="id_number"> {{ strnHeads[2] }} </div>
            <div class="number" id="id_number"> {{ strnHeads[3] }}</div>
          </div> -->

        </div>

      <div class="result"> 
        <p>{{ result }}</p> 
      </div>

      <div class="flip-card">
        <div class="flip-card-inner">
          <div  class="flip-card-front">
            <img id="image_heads" src="../assets/Coins/coin_american_heads.png" alt="Heads">
          </div>
          <div class="flip-card-back">
            <img id="image_tails" src="../assets/Coins/coin_american_tails.png" alt="Tails" >
          </div>
        </div>
      </div>
      <br>

      <div class="chance">
         {{ chance}} %
      </div>

      <div class="button_block">
        <div class="button_part">
          <button v-bind:disabled="!activeTossButton"  v-on:click="doCoinFlip()" class="btn btn-success"> Tos de munt  </button>
        </div>
        <div class="button_part">
          <button v-bind:disabled="!activeTossButton"  v-on:click="doRestart()" class="btn btn-warning"> Start opnieuw  </button>
        </div>
        <!-- <div >
        <button v-bind:disabled="!activeTossButton"  v-on:click="doCoinFlip()" class="btn btn-success"> Tos de munt  </button>
        </div> -->
      </div>

      <hr>
      <button  v-on:click="showScore()"  class="btn btn-primary"> Toon scores  </button>
      <br>
      <br>


      <div class="Table" id="scoreTable" v-if="show_score">
        De table toont de scores van de verschillende gebruikers. 
        <b-table-simple small caption-top responsive>
          <b-thead head-variant="light">
          <b-tr >
            <!-- <b-th class="text-right">#</b-th> -->
            <b-th class="text-center" variant="">naam</b-th>
            <b-th class="text-center" variant="">Poging</b-th>
            <b-th class="text-center">Kop</b-th>
            <b-th class="text-center">kans</b-th>
          </b-tr>
          </b-thead>
          <b-tbody >
            <b-tr  v-for="item in get_list" v-bind:key="item.ID">
              <b-th variant="light" class="text-center"> {{ item.user.username  }} </b-th>
              <b-th variant="light" class="text-center"> {{ item.nToss }} </b-th>
              <b-th variant="light" class="text-center"> {{ item.nHeads }} </b-th>
              <b-td variant="light" class="text-center"> {{ ((1 - item.chance ) * 100).toFixed(6) }}% </b-td>
            </b-tr>
          </b-tbody>
          <!-- <b-tfoot>
            <b-tr>
                <b-th>Totaal</b-th>
                <b-th variant="warning" class="text-right"> {{ game_score[1][0] }} </b-th>
                <b-th variant="warning" class="text-right"> {{ game_score[1][1] }} </b-th>
                <b-td variant="warning" class="text-right"> {{ game_score[1][2] }} </b-td>
                <b-td variant="warning" class="text-right"> {{ game_score[1][3] }} </b-td>
            </b-tr>
          </b-tfoot> -->
        </b-table-simple>
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

export default {
  name: 'Apptestluck',
  data () {
    return {
      test: {},
      result_test: {},
      image_heads: '../assets/Coins/coin_american_heads.png',
      image_tails: '../assets/Coins/coin_american_tails.png',
      result: 'Kop',
      activeTossButton: true,
      nToss: 0,   // Number of tosses done
      nHeads: 0,  // Number of times with Heads as result
      strnHeads: '0000',  // String of heads count
      strnToss: '0000',
      input_data: {       // Start with getting the data from DB
        'action': 'Get'
      },
      output_data: {},    // 
      chance: 0.000000,        // Chance of the results in percentage
      get_list: {},           // List of scores
      show_score: false,      // show table with scores

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

        // Get the experiment data
        this.input_data.action = 'Get'
        await this.postData();

        // Get the list of best results
        this.input_data.action = 'List'
        await this.postData();

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

    showScore: async function () {
        this.input_data.action = 'List'
        await this.postData();
        this.show_score = !this.show_score

        // jump the the end of page
        // window.location.href = "#jumpTo"
        document.getElementById("jumpTo").scrollIntoView({behavior: 'smooth'});
    },

    postData: async function () {
      // make sure the request  WILL use the interceptors
      const api_request = require('axios')

      await api_request({
          method: 'post',
          url: this.appSettings.url_coinflip,
          data: this.input_data

      })
        .then(response => {
            if (response) {
              // console.log(response.data.data)
            }

            if (this.input_data.action === 'Log' || this.input_data.action === 'Get' ) {

              this.output_data = response.data
              this.nToss = response.data.data.nToss
              this.nHeads = response.data.data.nHeads
              // console.log(this.nToss, this.nHeads)
              // Convert the counts to a string with 4 number that can be shown in the counter block.
              this.strnHeads = this.nHeads.toString().padStart(4,0)
              this.strnToss = this.nToss.toString().padStart(4,0)

              // Convert change to percentage and convert to string
              this.chance = ((1 - response.data.data.chance ) * 100).toFixed(6)

            }

            if (this.input_data.action === 'Stop') {

              this.nToss = 0
              this.nHeads = 0
              // Convert the counts to a string with 4 number that can be shown in the counter block.
              this.strnHeads = this.nHeads.toString().padStart(4,0)
              this.strnToss = this.nToss.toString().padStart(4,0)

              this.chance = (0.00000).toFixed(6)

            }

            if (this.input_data.action === 'List') {
              this.get_list = response.data.data



            }

        })
        .catch(() => {
            // alert('Fout')
            // console.log('Fout bij het ophalen van de wedstrijdlijst')
        })

    },

    doRestart: async function () {

      // Stop the experiment
      this.input_data = {
        'action' : 'Stop',
      }
      this.postData()

    },

    doCoinFlip: async function (){
      // Let a coin spin on the screen
      // Based om the outcome count the results.

      var el_result = document.getElementsByClassName("result");
      var element2 = document.getElementsByClassName("flip-card-inner");

      this.result = '????'
      el_result[0].style.color = "black";

      // Deactivate the toss button while the coin is being tossed
      this.activeTossButton = false

      // Flip the coin. Outcome  is 1 or 2
      var rand = Math.floor((Math.random() * 2) + 1);

      // First rotate the coin quickly back to the original position
      element2[0].style.transition = "transform 0.01s"
      element2[0].style.transform = 'rotateY(0deg)'

      // Make sure tha the action of setting back to 0deg is finished
      // before the next toss is done
      await this.doSleep(500)

      // Spin the coin
      element2[0].style.transition = "transform 2.0s"
      element2[0].style.transform = 'rotateY('+ (rand + 16) * 180 + 'deg)'


      // Wait for the coin the be finished with spinning
      await this.doSleep(2000)

      // Count the number of coin flips 
      this.nToss = this.nToss + 1

      // show the result of the flip
      if (rand === 1) {
        this.result = 'MUNT'
        el_result[0].style.color = "red";

      } else {
        this.result = 'KOP'
        el_result[0].style.color = "green";
        this.nHeads = this.nHeads + 1

      }

      //Get the calculated chance
      this.input_data = {
        'action' : 'Log',
        'nToss': this.nToss, 
        'nHeads': this.nHeads,
      }
      this.postData()

      // Convert the counts to a string with 4 number that can be shown in the counter block.
      this.strnHeads = this.nHeads.toString().padStart(4,0)
      this.strnToss = this.nToss.toString().padStart(4,0)

      // Activate the button for the next coin flip.
      this.activeTossButton = true
    
    }, // END coin_flip

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

/* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
.flip-card {
  // display: block;
  margin: auto;
  background-color: white;
  // background-color: transparent;
  width: 200px;
  height: 200px;
  border-radius: 10px;;
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  position: relative;
  width: $image_width ;
  height: $image_height;
  margin: auto;
  top: 25px;
  /* transition: transform 2.0s;  Add this using the javascript*/
  transform-style: preserve-3d;
  background-color: white;
}

/* Position the front and back side */
.flip-card-front, .flip-card-back {
  position: absolute;
  // width: 100%;
  // height: 100%;
  width: $image_width;
  height: $image_height;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
}

/* Style the front side (fallback if image is missing) */
.flip-card-front {
  // background-color: #bbb;
  // color: black;
}

/* Style the back side */
.flip-card-back {
  // background-color: dodgerblue;
  // color: white;
  transform: rotateY(180deg);
}

#image_heads, #image_tails {
  width: $image_width;
  height: $image_height;
}
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


.chance {
  width: 100%;
  margin: 0 auto 5px auto;
  color: blue;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}


.result {
  // display: block;
  width: 100%;
  margin: 5px auto 5px auto;
  // margin-left: 100px;
  // margin-bottom: 10px;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}

// For the counter

.counter_main {
  width: 100%;
  margin: auto;
  // border: 1px solid red;
  text-align: center;
}

.counter_block {
  display: inline-block;
  width: auto;
  padding: 0px 3px 0px 3px;
  // border: 2px solid blue;
}

.counter_header {
  font-size: 20px;
  font-weight: bold;
  text-align: center;
  color:darkslateblue;
}

.counter {
  display: inline-block;
  height: 70px;
  width: 130px;
  margin: 2px;
  padding: 10px;
  background-color: grey;
  border-radius: 10px;
}

.number {
  display: inline-block;
  height: 50px;
  width: 25px;
  margin: 0px 0px 0px 2px;
  padding: 2px;
  background-color: honeydew;
  text-align: center;
  font-size: 30px;

}


.main_container {
  height: 46px;
  width: auto;
  padding: 3px;
  margin: 2px;
  max-width: 300px;
  background-color: #555555;
  align-content: center;
}
.container_inner {
  height: auto;
  border: none;
  background-color: #555555;
  max-width: 290px;
  vertical-align: center;
  padding-top: 12px;
  padding-left: 10px;
  align-content: center;
}
 .num_tiles {
  width:30px;
  height: 30px;
  background-color: #888888;
  color: #ffffff;
  font-size: 22px;
  text-align: center;
  line-height: 20px;
  padding: 3px;
  margin: 1.5px;
  font-family: verdana;
  vertical-align: center;
}

</style>
