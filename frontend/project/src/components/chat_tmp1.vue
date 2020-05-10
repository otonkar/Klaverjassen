<template>
  <div class="Appchat o_fullscreen">

      <div class="card_AA"></div>
      <div class="card_BB"></div>
      <div class="card_CC"></div>

      <!-- *** Card player 0 -->
      <!-- <div class="card_p0">
        <div class="card">
            <span class="card__suit card__suit--top">A</span>
            <span class="card__number">♣</span>
        </div>
      </div> -->

      <!-- *** Card player 1 -->
      <div class="card_p1">
        <div class="card">
            <span class="card__suit card__suit--top">J</span>
            <span class="card__number">♣</span>
            <!-- <span class="card__suit card__suit--bottom">♣</span> -->
        </div>
      </div>

      <!-- *** Card player 2 -->
      <div class="card_p2">
        <div class="card">
            <span class="card__suit card__suit--top">Q</span>
            <span class="card__number">♣</span>
            <!-- <span class="card__suit card__suit--bottom">♣</span> -->
        </div>
      </div>

       <!-- *** Card player 3 -->
      <div class="card_p3">
        <div class="card">
            <span class="card__suit card__suit--top">10</span>
            <span class="card__number">♣</span>
            <!-- <span class="card__suit card__suit--bottom">♣</span> -->
        </div>
      </div>

      <!-- <div v-bind:class="setCardClass" :click="doPlayCard()"> -->
        <!-- <div :class="cardClass" @click="doPlayCard()">
          <div class="card">
              <span class="card__suit card__suit--top">A</span>
              <span class="card__number">♣</span>
          </div>
        </div> -->

      <!-- <div v-for="card in cards" v-bind:key="card[1]"> 
        <div :class="cardClass" @click="doPlayCard()">
          <div class="card">
              <span class="card__suit card__suit--top">{{ card[1] }}</span>
              <span class="card__number">{{ card[0] }}</span>
          </div>
        </div>
      </div> -->

      <!-- <div v-for="(card, index) in cards" v-bind:key="index"> -->

      <!-- <div class="player_hand"> -->

        <!-- <div class="card">
          <span class="card__suit card__suit--top">{{ card[1] }}</span>
          <span class="card__number">{{ card[0] }}</span>
        </div> -->

      <!-- </div> -->



        <!-- <div  v-for="(card, index) in cards" 
              v-bind:key="index" 
              v-bind:class="{'card_DD': !play_card[index], 'card_p0': play_card[index]}" 
              v-bind:hidden="remove[index]"
              @click="doPlayCard(index)"
          >
          <div class="card">
              <span class="card__suit card__suit--top">{{ card[1] }}</span>
              <span class="card__number">{{ card[0] }}</span>
          </div>
        </div> -->


          <div class="ole">
          <div class="card card_DD">
              <span class="card__suit card__suit--top">7</span>
              <span class="card__number">♣</span>
          </div>
          </div>

          <div class="ole">
          <div class="card card_DD1">
              <span class="card__suit card__suit--top">8</span>
              <span class="card__number">♣</span>
          </div>
          </div>





      <!-- <div class="player_hand"> -->

        <!-- <div class="card_DD">
          <div class="card">
              <span class="card__suit card__suit--top">B</span>
              <span class="card__number">♣</span>
          </div>
        </div>

        <div class="card_DD">
          <div class="card">
              <span class="card__suit card__suit--top">7</span>
              <span class="card__number">♣</span>
          </div>
        </div>

        <div class="card_DD">
          <div class="card">
              <span class="card__suit card__suit--top">8</span>
              <span class="card__number">♣</span>
          </div>
        </div>

        <div class="card_DD">
          <div class="card">
              <span class="card__suit card__suit--top">9</span>
              <span class="card__number">♣</span>
          </div>
        </div>

        <div class="card_DD">
          <div class="card">
              <span class="card__suit card__suit--top">10</span>
              <span class="card__number">♣</span>
          </div>
        </div> -->

        <!-- <div v-bind:class="{'card_DD': !play[5], 'card_p0': play[5]}" @click="play[5]=!play[5]">
          <div class="card">
              <span class="card__suit card__suit--top">Q</span>
              <span class="card__number">♣</span>
          </div>
        </div>

        <div v-bind:class="{'card_DD': !play[6], 'card_p0': play[6]}" @click="play[6]=!play[6]">
          <div class="card">
              <span class="card__suit card__suit--top">B</span>
              <span class="card__number">♣</span>
          </div>
        </div> -->

        <!-- <div v-bind:class="{'card_DD': !test[7], 'card_p0': test[7]}" @click="doPlayCard(7)">
          <div class="card">
              <span class="card__suit card__suit--top">A</span>
              <span class="card__number">♣</span>
          </div>
        </div> -->

      <!-- </div> -->

  </div>
</template>


<script>

export default {
  name: 'Appchat',
  data () {
    return {
      title: 'Chat page',
      roomName: '',
      message: '',
      status: '',
      dialogs: [],
      cardClass: {
        "card_DD": true, 
        "card_p0": false
      },
      cards: [
        ['♣', '7'],
        ['♣', '8'],
        ['♣', '9'],
        ['♣', '10'],
        ['♣', 'J'],
        ['♣', 'Q'],
        ['♣', 'K'],
        ['♣', 'A'],
      ],
      play_card: [          // when the card is played the class needs to change
        false, false, false, false, 
        false, false, false, false, 
      ],
      played_cards: [],   // log the card number of the played cards
      remove: [           // Determine which card not to display
        false, false, false, false, 
        false, false, false, false, 
      ],  // To indicate which card must be removed on next play
      previous_card: '',
      play1: false
    }
  },
  created() {
      
  },
  activated: function () {
    // console.log(this.$route.name)

    if (this.user.user_is_logged_in === false) {
      // there may be a valid refresh token stored in localStore
      // Do a request so that the refresh token is used to get an access token
      // console.log('Not logged in')

    } else {
      // console.log('Test chat page')
      // document.body.requestFullscreen()
      this.user.show_header = false
      this.$store.dispatch('updateUser', this.user)

    } //END if-else

  },  //END mounted
  methods: {
    doPlayCard: async function (card) {

      // Do not display the previous card om the stack
      this.remove[this.previous_card] = true  // has been removed
      // console.log(this.remove)


      // // console.log(card, this.test[card])
      this.play_card[card] = true
      
      this.previous_card = card
      this.$forceUpdate()

    }
    
  },  //END methods
  computed: {
    user () {
      return this.$store.state.user
    },
    appSettings () {
      return this.$store.state.appSettings
    },
    window_size () {
      return this.$store.state.window_size
    }
  }
}
</script>

<style scoped lang='scss'>
// Define variables
$height_header: 0px;
$height_card: 65px;
$width_card: 40px;

.o_fullscreen {
  height: calc(100vh - #{$height_header});
  width:100vw;
  background-color: blue;
  // margin: 0 auto;    // To center
  text-align: center
}

.o_halfscreen1 {
  height: calc( (100vh - #{$height_header}) / 2 );
  background-color: red;
  display: block;
}

.o_halfscreen2 {
  height: calc( (100vh - #{$height_header}) / 2 );
  background-color: green;
  display: block;
}

// .centerhole {
//   position: fixed;
//   top: 100%;
//   left: 50%;
//   /* bring your own prefixes */
//   transform: translate(-50%, -50%);
//   background-color: black;
//   width: 75px;
//   height: 100px;
// }

.toppart {
  height: calc(0.5 * 100vh - #{$height_header}/2 - #{$height_card}/2);
  width:100vw;
  display: block;
  background-color: yellow;
}

.bottompart {
  height: calc(0.5 * 100vh - #{$height_header}/2 - #{$height_card}/2);
  width:100vw;
  display: block;
  background-color: pink;
  position: absolute;
  bottom: 0px;
}

.middlepart {
  height: #{$height_card};
  width: 100vw;
  display: block;
  position: relative;
  top: 0px;
  transform: translate(0%, -50%);
  background-color: grey;
}

// Player card bottom
.card_AA {
  height: #{$height_card};
  width: #{$width_card};
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 2.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 1.5*#{$height_card} );
  background-color: red;
}

.card_BB {
  height: #{$height_card};
  width: #{$width_card};
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 2.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
  background-color: grey;
}

.card_CC {
  height: #{$height_card};
  width: #{$width_card};
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 2.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 0.5*#{$height_card} );
  background-color: green;
}

.card_DD {
  // height: #{$height_card};
  // width: #{$width_card};
  display: inline-block;
  position: fixed;
  // float: left;
  // left: calc( 100vw/2 - 2.5*#{$width_card} );
  top: calc(  100vh - 3.5*#{$width_card} - 15px );
  margin-right: 5px;
  margin-bottom: 7px;
  // transform: rotateZ( 360deg );
}

.card_DD1 {
  // height: #{$height_card};
  // width: #{$width_card};
  display: inline-block;
  position: fixed;
  // float: left;
  left: calc( 100vw/2 - 1.5*#{$width_card} );
  top: calc(  100vh - 3.5*#{$width_card} - 15px );
  margin-right: 5px;
  margin-bottom: 7px;
  // transform: rotateZ( 360deg );
}

.ole:nth-of-type(1) {
  background: red;
  // left: calc( 100vw/2 - 2.5*#{$width_card} );
  // transform: translate(0px, 0px);
}

.ole:nth-of-type(2) {
  background: grey;
  // transform: translate(50px, 0px);
}



// .card_DD:active{
//   display: block;
//   position: absolute;
//   left: calc( 100vw/2 - 0.5*#{$width_card} );
//   top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 0.5*#{$height_card} );
// }


.card_p0 {
  height: #{$height_card};
  width: #{$width_card};
  display: block;
  position: fixed;
  left: 0px;
  top: 0px;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 0.5*#{$height_card} );
  border-radius: 5px;
  background-color: white;
  transition-property: display, position, left, top transform;
  transition-duration: 0.7s;
}

// player card left
.card_p1 {
  height: #{$height_card};
  width: #{$width_card};
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 1.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
  // background-color: grey;

}

// player card top
.card_p2 {
  height: #{$height_card};
  width: #{$width_card};
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 1.5*#{$height_card} );
  background-color: grey;
}

// player card right
.card_p3 {
  height: #{$height_card};
  width: #{$width_card};
  display: block;
  position: fixed;
  left: calc( 100vw/2 + 0.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
  background-color: grey;
}

// block to place the player cards
.player_hand { 
  height: #{1* $height_card + 10px};
  // width: calc( 5.0*#{$width_card} + 4*10px);
  display: inline-block;
  position: absolute;
  bottom: 5px;
  left: calc( 100vw/2 );
  transform: translate(-50%, -0%);
  background-color: grey;
}
    
.card {
  width: $width_card;
  height: $height_card;
  // float: left;
  margin-right: 5px;
  margin-bottom: 7px;
  border-radius: 5px;
  display: inline-block;
  // margin: 0 auto;
  // transition: transform  0.5s
}

.card:active{
  // transform:scale(0.9);
  box-shadow:5px 5px 5px rgb(230, 230, 230);
}

.card:hover {
  box-shadow:0px 3px 6px rgba(0,0,0,.7);
}

.card__suit {
  width: 100%;
  display: block;
  font-size: 1.6em;
}

.card__suit--top {
  text-align: left;
  padding-left: 5px;
}

.card__suit--bottom {
  position: absolute;
  bottom: 0px;
  text-align: left;
  transform: rotate(180deg);
  padding-left: 5px;
  display: block;
}

.card__number {
  width: 100%;
  position: absolute;
  top: 40%;
  left: 0%;
  text-align: center;
  font-size: 1.8em;
}


</style>
