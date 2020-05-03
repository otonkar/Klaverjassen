<template>
  <div class="Appchat o_fullscreen">

      <!-- <div class="card-holder hearts_ace"></div>
      <div class="card-holder hearts_two"></div>
      <div class="card-holder hearts_three"></div>
      <div class="card-holder hearts_four"></div>
      <div class="card-holder hearts_five"></div>
      <div class="card-holder hearts_six"></div>
      <div class="card-holder hearts_seven"></div>
      <div class="card-holder hearts_eight"></div>
      <div class="card-holder hearts_nine"></div>
      <div class="card-holder hearts_ten"></div>
      <div class="card-holder hearts_jack"></div>
      <div class="card-holder hearts_queen"></div>
      <div class="card-holder hearts_king"></div>
      <br>

      <div class="card-holder spades_ace"></div>
      <div class="card-holder spades_two"></div>
      <div class="card-holder spades_three"></div>
      <div class="card-holder spades_four"></div>
      <div class="card-holder spades_five"></div>
      <div class="card-holder spades_six"></div>
      <div class="card-holder spades_seven"></div>
      <div class="card-holder spades_eight"></div>
      <div class="card-holder spades_nine"></div>
      <div class="card-holder spades_ten"></div>
      <div class="card-holder spades_jack"></div>
      <div class="card-holder spades_queen"></div>
      <div class="card-holder spades_king"></div>
      <br>

      <div class="card-holder diamonds_ace"></div>
      <div class="card-holder diamonds_two"></div>
      <div class="card-holder diamonds_three"></div>
      <div class="card-holder diamonds_four"></div>
      <div class="card-holder diamonds_five"></div>
      <div class="card-holder diamonds_six"></div>
      <div class="card-holder diamonds_seven"></div>
      <div class="card-holder diamonds_eight"></div>
      <div class="card-holder diamonds_nine"></div>
      <div class="card-holder diamonds_ten"></div>
      <div class="card-holder diamonds_jack"></div>
      <div class="card-holder diamonds_queen"></div>
      <div class="card-holder diamonds_king"></div>
      <br>

      <div class="card-holder cubs_ace"></div>
      <div class="card-holder cubs_two"></div>
      <div class="card-holder cubs_three"></div>
      <div class="card-holder cubs_four"></div>
      <div class="card-holder cubs_five"></div>
      <div class="card-holder cubs_six"></div>
      <div class="card-holder cubs_seven"></div>
      <div class="card-holder cubs_eight"></div>
      <div class="card-holder cubs_nine"></div>
      <div class="card-holder cubs_ten"></div>
      <div class="card-holder cubs_jack"></div>
      <div class="card-holder cubs_queen"></div>
      <div class="card-holder cubs_king"></div>
      <br> -->

      <!-- Empty placeholders to put the card played -->
      <div class="card-holder  play_p0 "></div>
      <div class="card-holder  play_p1 "></div>
      <div class="card-holder  play_p2 "></div>
      <div class="card-holder  play_p3 "></div>

      <!-- Base place to start throwing cards for players 1,2,3 -->
      <div class="card-holder  hand_p1  red_back "></div>
      <div class="card-holder  hand_p2  red_back "></div>
      <div class="card-holder  hand_p3  red_back "></div>

      <!-- Create empty places for the handcards -->
      <div class="card-holder card-active hand_p0-0 "></div>

      <!-- Show the hand of player 0 -->
      <div v-bind:class="card_class"></div>
      <div class="card-holder card-active hand_p0-1 cubs_king"></div>
      <div @click="doPlayCard(1)" class="card-holder card-active hand_p0-2 cubs_queen"></div>
      <div class="card-holder card-active hand_p0-3 cubs_jack"></div>
      <div class="card-holder card-active hand_p0-4 cubs_ten"></div>
      <div class="card-holder card-active hand_p0-5 cubs_nine"></div>
      <div class="card-holder card-active hand_p0-6 cubs_eight"></div>
      <div class="card-holder card-active hand_p0-7 cubs_seven"></div>

  </div>
</template>


<script>

export default {
  name: 'Appchat',
  data () {
    return {
      title: 'test page',
      card_class: {
          'card-holder': true,
          'card-active': true,
          'hand_p0-0': true,
          'play_p0': false,
          'cubs_ace': true
        },
                // "card-holder card-active hand_p0-1 cubs_king",
        // "card-holder card-active hand_p0-2 cubs_queen",
        // "card-holder card-active hand_p0-3 cubs_jack",
        // "card-holder card-active hand_p0-4 cubs_ten",
        // "card-holder card-active hand_p0-5 cubs_nine",
        // "card-holder card-active hand_p0-6 cubs_eight",
        // "card-holder card-active hand_p0-7 cubs_seven"
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

      // Do not display the header
      this.user.show_header = false
      this.$store.dispatch('updateUser', this.user)
      
    }//END if-else

  },//END mounted
  methods: {
    doPlayCard: async function () {
      
      this.card_class['hand_p0-0'] = false
      this.card_class['play_p0'] = true


      // console.log(card)
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
// function with input px and output vw
// @function get-vw($font)
//   @if $vw-enable
//     $vw-context: $vw-viewport * 0.01 * 1px

//     @return $font / $vw-context * 1vw

//   @return $font


// Define variables
$height_header: 0px;
$width_card: 60px;
$height_card: $width_card * 1.4;

.o_fullscreen {
  height: calc(100vh - #{$height_header});
  width:100vw;
  background-color: green;
  // margin: 0 auto;    // To center
  text-align: center;
  padding: 5px 5px 5px calc(0*#{$width_card}); //take into consideration the overlap of cards
}

// Player card bottom
.play_p0 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 0.5*#{$height_card} );
  transition-property: display, position, left, top;
  transition-duration: 0.7s;
}

// player card left
.play_p1 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 1.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
}

// player card top
.play_p2 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 1.5*#{$height_card} );
}

// player card right
.play_p3 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 + 0.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
}

// Hand of other players to start from playing a card to the middle
.hand_p1 {
  display: block;
  position: fixed;
  left: calc( 0.25*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
}

.hand_p2 {
  display: block;
  position: fixed;
  left: calc( 100vw/2 - 0.5*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  - 3.0*#{$height_card} );
  transform: rotateZ(90deg);
}

.hand_p3 {
  display: block;
  position: fixed;
  right: calc( 0.25*#{$width_card} );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} - 0.5*#{$height_card} );
}

// Calulate the total space per card. 
// 8 cards should fit on the screen. 
// maximalize the spacing beteeen the cards 

$side_margin: 5px;   // minimal margin on left and right side of screen. 
$max_margin: 10px;
$margin: 10px;
// $N: 8;               // Number of cards to fit on screen
// $margin: 2px; 
// $dummy1: $N - 1;
// $dummy2: calc(100vw - 2 * #{$side_margin} - 8 * #{$width_card});
// $margin: calc(#{$dummy2} / #{$dummy1});
// $margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / 7);
// $margin: calc(#{$dummy2} / #{$dummy1});
// $margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / ($N - 1));
// calc( (100vw - 2*#{$side_margin} - 8*#{$width_card} ) / (#{$N}-7) );  // spzce between cards
// (100vw - 2*$side_margin - 8*$width_card ) / ($N-7) ;
$margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / 7);
// CANNOT limit margin to < 10 px.

// make the margin flexible when the screen is snaller than xxxpx
// @media screen and (min-width: 480px) {
//       $margin: calc((100vw - 2 * #{$side_margin} - 8 * #{$width_card}) / 7);
// } 


.hand_p0-0 {
  $pos: -4;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-1 {
  $pos: -3;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-2 {
  $pos: -2;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-3 {
  $pos: -1;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-4 {
  $pos: -0;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-5 {
  $pos: 1;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-6 {
  $pos: 2;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.hand_p0-7 {
  $pos: 3;    // position of the card
  display: block;
  position: fixed;
  left: calc( 50vw +  (#{$pos}*#{$width_card} +  (#{$pos} + 0.5) * #{$margin} ) );
  top: calc( (100vh - #{$height_header}) / 2  + #{$height_header} + 2.0*#{$height_card} );
}

.card-holder{
  width:$width_card;
  height:$height_card;
  box-shadow:2px 2px 2px rgba(0,0,0,.8);
  border-radius: 5px;
  background-color: rgb(11, 97, 11);
  // position:relative;
  // display:inline-block;
  margin-top:2px;
  margin-left: 2px;
  // margin-left: calc(-0.50*#{$width_card});   // Overlap the cards

  transform-style: preserve-3d;
  backface-visibility: hidden;

  background-repeat:no-repeat;
  background-position: 0% 0%;
  background-size: 100% 100%;
}

.card-active:hover {
  box-shadow:0px 5px 10px rgba(0,0,0,.7);
  transform:translate(0px,-5px);
}
.card-active:active{
  transform:scale(.9);
}


//******** Define the cards **************************************** */

.hearts_ace {
  background-image: url('../assets/Cards/AH.png');
}

.hearts_two {
  background-image: url('../assets/Cards/2H.png');
}

.hearts_three {
  background-image: url('../assets/Cards/3H.png');
}

.hearts_four {
  background-image: url('../assets/Cards/4H.png');
}

.hearts_five {
  background-image: url('../assets/Cards/5H.png');
}

.hearts_six {
  background-image: url('../assets/Cards/6H.png');
}

.hearts_seven {
  background-image: url('../assets/Cards/7H.png');
}

.hearts_eight {
  background-image: url('../assets/Cards/8H.png');
}

.hearts_nine {
  background-image: url('../assets/Cards/9H.png');
}

.hearts_ten {
  background-image: url('../assets/Cards/10H.png');
}

.hearts_jack {
  background-image: url('../assets/Cards/JH.png');
}

.hearts_queen {
  background-image: url('../assets/Cards/QH.png');
}

.hearts_king {
  background-image: url('../assets/Cards/KH.png');
}


//************************************************ */

.spades_ace {
  background-image: url('../assets/Cards/AS.png');
}

.spades_two {
  background-image: url('../assets/Cards/2S.png');
}

.spades_three {
  background-image: url('../assets/Cards/3S.png');
}

.spades_four {
  background-image: url('../assets/Cards/4S.png');
}

.spades_five {
  background-image: url('../assets/Cards/5S.png');
}

.spades_six {
  background-image: url('../assets/Cards/6S.png');
}

.spades_seven {
  background-image: url('../assets/Cards/7S.png');
}

.spades_eight {
  background-image: url('../assets/Cards/8S.png');
}

.spades_nine {
  background-image: url('../assets/Cards/9S.png');
}

.spades_ten {
  background-image: url('../assets/Cards/10S.png');
}

.spades_jack {
  background-image: url('../assets/Cards/JS.png');
}

.spades_queen {
  background-image: url('../assets/Cards/QS.png');
}

.spades_king {
  background-image: url('../assets/Cards/KS.png');
}

//************************************************ */

.diamonds_ace {
  background-image: url('../assets/Cards/Ace_diamonds.png');
}

.diamonds_two {
  background-image: url('../assets/Cards/2D.png');
}

.diamonds_three {
  background-image: url('../assets/Cards/3D.png');
}

.diamonds_four {
  background-image: url('../assets/Cards/4D.png');
}

.diamonds_five {
  background-image: url('../assets/Cards/5D.png');
}

.diamonds_six {
  background-image: url('../assets/Cards/6D.png');
}

.diamonds_seven {
  background-image: url('../assets/Cards/7D.png');
}

.diamonds_eight {
  background-image: url('../assets/Cards/8D.png');
}

.diamonds_nine {
  background-image: url('../assets/Cards/9D.png');
}

.diamonds_ten {
  background-image: url('../assets/Cards/10D.png');
}

.diamonds_jack {
  background-image: url('../assets/Cards/JD.png');
}

.diamonds_queen {
  background-image: url('../assets/Cards/QD.png');
}

.diamonds_king {
  background-image: url('../assets/Cards/KD.png');
}

//************************************************ */

.cubs_ace {
  background-image: url('../assets/Cards/AC.png');
}

.cubs_two {
  background-image: url('../assets/Cards/2C.png');
}

.cubs_three {
  background-image: url('../assets/Cards/3C.png');
}

.cubs_four {
  background-image: url('../assets/Cards/4C.png');
}

.cubs_five {
  background-image: url('../assets/Cards/5C.png');
}

.cubs_six {
  background-image: url('../assets/Cards/6C.png');
}

.cubs_seven {
  background-image: url('../assets/Cards/7C.png');
}

.cubs_eight {
  background-image: url('../assets/Cards/8C.png');
}

.cubs_nine {
  background-image: url('../assets/Cards/9C.png');
}

.cubs_ten {
  background-image: url('../assets/Cards/10C.png');
}

.cubs_jack {
  background-image: url('../assets/Cards/JC.png');
}

.cubs_queen {
  background-image: url('../assets/Cards/QC.png');
}

.cubs_king {
  background-image: url('../assets/Cards/KC.png');
}

//************************************************ */

.red_back {
  background-image: url('../assets/Cards/red_back.png');
}






</style>
