<template>


  <div class="Appgames_slagen" v-if="isLoaded && is_allowed">
      <!-- loaded : game {{ gameID}}, leg {{leg+1}} -->



        <!-- <br>
        <h4>Slagen game: {{ gameID }}, ronde: {{ leg.leg + 1 }} </h4>
        <hr>
        <p>De speler die uitkwam is aangegeven met groene kleur</p>
        <p>
            Gegevens deze rounde:
            <ul>
                <li>speler aangenomen: {{ leg.player_aangenomen }}</li>
                <li>Gespeelde troef: {{ game_slagen[0].troef }}</li>
            </ul>

        </p>
        <p></p> -->


        <h5>Slagen potje: {{ gameID }}, ronde: {{ leg + 1 }} </h5>
        <p>
            Troef : {{ troef_name }} <br>
            Aangenomen door speler: {{ game_slagen[0].position_start + 1 }} <br>
            Telling team A (speler 1,3):</strong> {{ tot_scoreA }} + {{ tot_roemA }} = {{ tot_scoreA  + tot_roemA}} <br>
            Telling team B (speler 2,4):</strong> {{ tot_scoreB }} + {{ tot_roemB }} = {{ tot_scoreB  + tot_roemB}} <br> 

        </p>
        <div class="Table">
            <b-table-simple small responsive>
                
                <!-- <colgroup><col></colgroup>
                <colgroup><col><col><col><col></colgroup>
                <colgroup><col><col></colgroup> -->
                <!-- <colgroup><col><col></colgroup> -->
                <b-thead head-variant="light">
                <b-tr >
                    <b-th colspan="1" class="text-center" ></b-th>
                    <b-th colspan="4" class="text-center" >speler</b-th>
                    <!-- <b-th colspan="1" class="text-center" ></b-th>
                    <b-th colspan="1" class="text-center" ></b-th>
                    <b-th colspan="1" class="text-center" ></b-th> -->
                </b-tr>
                <b-tr >
                    <b-th colspan="1" >#</b-th>
                    <b-th colspan="1" class="text-center" >1</b-th>
                    <b-th colspan="1" class="text-center" >2</b-th>
                    <b-th colspan="1" class="text-center" >3</b-th>
                    <b-th colspan="1" class="text-center" >4</b-th>
                    <b-th colspan="1" class="text-center" >win</b-th>
                    <b-th colspan="1" class="text-center" >pnt</b-th>
                    <b-th colspan="1" class="text-center" >roem</b-th>
                </b-tr>
                </b-thead>
                <b-tbody >
                    <b-tr v-for="slag in game_slagen" v-bind:key="slag.id">
                    <b-th class="success"> {{ slag.n_slag + 1 }} </b-th>
                    <b-th v-bind:variant="[slag.position_start===0 ? 'success': 'light']" class="text-center"> <img v-bind:src="slag.cards_slag[0]['color']" width="15px">  {{ slag.cards_slag[0]['rank'] }}    </b-th>
                    <b-th v-bind:variant="[slag.position_start===1 ? 'success': 'light']" class="text-center"> <img v-bind:src="slag.cards_slag[1]['color']" width="15px">  {{ slag.cards_slag[1]['rank'] }}    </b-th>
                    <b-td v-bind:variant="[slag.position_start===2 ? 'success': 'light']" class="text-center"> <img v-bind:src="slag.cards_slag[2]['color']" width="15px">  {{ slag.cards_slag[2]['rank'] }}   </b-td>
                    <b-td v-bind:variant="[slag.position_start===3 ? 'success': 'light']" class="text-center"> <img v-bind:src="slag.cards_slag[3]['color']" width="15px">  {{ slag.cards_slag[3]['rank'] }}  </b-td>
                    <b-td variant="light" class="text-center"> {{ slag.player_won + 1 }}  </b-td>
                    <b-td variant="light" class="text-center"> {{ slag.score }}  </b-td>
                    <b-td variant="light" class="text-center"> {{ slag.roem }}  </b-td>
                    </b-tr>
                </b-tbody>
                <b-tfoot>
                <!-- <b-tr>
                    <b-th>Totaal</b-th>
                    <b-th variant="warning"> {{ game_score[1][0] }} </b-th>
                    <b-th variant="warning"> {{ game_score[1][1] }} </b-th>
                    <b-td variant="warning"> {{ game_score[1][2] }} </b-td>
                    <b-td variant="warning"> {{ game_score[1][3] }} </b-td>
                    
                </b-tr> -->
                </b-tfoot>
            </b-table-simple>
        </div>

         <b-button variant="primary" @click="doCloseSlagen()" >Sluiten</b-button>

  </div>
  <div v-else>
      <h3>Geen toegang</h3>
      <!-- loaded : game {{ gameID}}, leg {{leg+1}} -->
      <p>
          Het is niet toegestaan de slagen van een potje in te zien als de wedstrijd nog niet is afgelopen. 
          Alleen als je zelf al een potje binnen deze wedstrijd hebt afgerond, of als je zelf speler bent van dit potje, 
          dan mogen deze slagen getoond worden
      </p>
  </div>
</template>

<script>

// Want to use this component with simple input
//  * gameID
//  * leg  (integer)
// This component can be use to show the slagen of both completed and not completed legs


export default {
  name: 'Appgameslagen',
  props: {
    gameID: Number,
    leg: Number,
  },

  data () {
    return {
        title: 'Game details page',
        isLoaded: false,            // to rerender the page when data is loaded
        errors: {},
        game_slagen: [], 
        my_image: require('@/assets/clubs.png'),                      // Variable to store the image name
        test: false,
        // leg: 0,
        // gameID: 0,
        troef_name: '----',
        tot_scoreA: 0,
        tot_scoreB: 0,
        tot_roemA: 0,
        tot_roemB: 0,
        is_allowed: false,          // Indicates that user is allowed to see the legs of this game
        event_data: []              // data coming from the changeLeg event
    }
  },

  mounted: async function () {
        // On mount set that the component must listen on the even 'changeLeg'

        this.$root.$on('changeLeg', async data => await this.doUpdateSlagen(data) )
        // console.log('Mounted: ', this.gameID, this.leg)

        // On mount make sure that the original data is loaded.
        // In next steps  the data is updated by the event
        await this.doGetSlagen(this.gameID, this.leg)
  },

  // Do not use mounted, otherwise no new game will be loaded
  activated: async function () {
        // console.log(this.$route.name)
        // Do not show full screen on login page
        // document.exitFullscreen();
        if (this.user.user_is_logged_in === false) {

                this.$router.push({ name: 'Home' })

        } else {

            // console.log('activated', this.gameID, this.leg)
            
            // Do NOT get the slagen here, because these will result in doubled numbers of the score,
            // because also the event will update the data
            await this.doGetSlagen(this.gameID, this.leg)

        }//END if
  },//END activated

  methods: {

    goBack: function () {
        this.variables.show_slagen = false
        this.game_slagen = []
        this.$store.dispatch('updateVariables', this.variables)
        this.$router.go(-1)
    },  //END goBack

    // getImage: function (img) {
    //     // img = '"' + img + '"'
    //     this.my_image = img
    //     // console.log(my_image)

    //     return img

    // }, //END getImage

    doUpdateSlagen: async function (data) {
        // In the event both the game and leg are updated

        this.event_data = data
        await this.doGetSlagen(this.event_data[1], this.event_data[0])

    },

    doGetSlagen: async function (gameID, lega) {
        // Show the current score of the game

        // reset the count of score
        // Note: when the activated and the event run simulanuously that they will both update the
        // this. variables. This is result in double counts. 
        // There do the internal calculations with local variables and at the end copy the value to the
        // global (this.) version
        this.tot_scoreA = 0
        this.tot_scoreB = 0
        this.tot_roemA = 0
        this.tot_roemB = 0
        let tot_scoreA = 0
        let tot_scoreB = 0
        let tot_roemA = 0
        let tot_roemB = 0
        this.game_slagen = []    // to avoid doubled scores 
        // Need to reset this so that when switching to another game 
        // the correct information will be shown.
        this.is_allowed = false
        this.isLoaded = false

       // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')
        // console.log('DUMMY5')

        // Get all the players of a match
        await api_request({
            method: 'get',
            url: this.appSettings.url_game_slagen + 'gameID=' + gameID + '&leg=' + lega
            // data: this.input
        })
        .then(response => {
            if (response.status === 200) {
                this.game_slagen = response.data[0]
                this.is_allowed = response.data[1]
                // console.log('doGetSlagen is_allowed:', this.is_allowed)
                // console.log('length of array slagen: ', this.game_slagen.length)
            }
        })
        .catch(() => {
            // console.log('Get game score failed')
            // console.log(error.response)
        })

        // Determine the troef and show it on the screen
        // use the info from the first round (slag)
        if (this.game_slagen.length !== 0 ) {
            var troef = this.game_slagen[0].troef
            var tmp = {'clubs': 'Klaver','hearts': 'Harten','spades': 'Schoppen', 'diamonds': 'Ruiten'}
            this.troef_name = tmp[troef]
            this.show_game_slagen = true
        }

        for (var item in this.game_slagen) {
            // // console.log(this.game_slagen[item].cards_slag)
            var slag = JSON.parse(this.game_slagen[item].cards_slag)
            // // console.log(slag[0]['color'])

            var converted_cards = []
            var converted_card = {}
            for (var card in slag) {
                converted_card = this.convertCard(slag[card])
                converted_cards.push(converted_card)
            }
            // // console.log(converted_cards)
            this.game_slagen[item].cards_slag = converted_cards
            
            // var converted_card = this.convertCard(this.game_slagen[item].cards_slag[0])
            // // console.log(converted_card)

            // Determine the score of this leg
            if (this.game_slagen[item].teamA_won === true) {
                // console.log('**', this.game_slagen[item].score)
                tot_scoreA = tot_scoreA + this.game_slagen[item].score
                tot_roemA = tot_roemA + this.game_slagen[item].roem
                // console.log('ScoreA :', tot_scoreA, this.game_slagen[item].score)
            } else {
                tot_scoreB = tot_scoreB + this.game_slagen[item].score
                tot_roemB = tot_roemB + this.game_slagen[item].roem
            }

            this.tot_scoreA = tot_scoreA
            this.tot_roemA = tot_roemA
            this.tot_scoreB = tot_scoreB
            this.tot_roemB = tot_roemB

        }

        // console.log(this.game_slagen)

        this.isLoaded = true

        // this.$forceUpdate()

    }, //END doGetScores

    doCloseSlagen: function () {
        this.variables.show_slagen = false
        this.game_slagen = []
        this.$store.dispatch('updateVariables', this.variables)

    }, //END doCloseSlagen

    convertCard:function (card) {
        // Convert the cards:  spades-eight => ./spades.png - 8
        // card is like {'color': 'spades, 'rank': 'ten'}
        // This to show this in the Games slagen
        var map_rank = {
            'seven'     : '7',
            'eight'     : '8',
            'nine'      : '9',
            'ten'       : '10',
            'jack'      : 'J',
            'queen'     : 'Q',
            'king'      : 'K',
            'ace'       : 'A'
        }
        
        var map_color = {
            'clubs'     : require('@/assets/clubs.png'),
            'hearts'    : require('@/assets/hearts.png'),
            'spades'    : require('@/assets/spades.png'),
            'diamonds'  : require('@/assets/diamonds.png')
        }

        var converted_card = {
            'color'     : map_color[card.color],
            'rank'      : map_rank[card.rank]
        }

        // // console.log('Converted card : ', card, converted_card)


        return converted_card
    },
       
  },  //END methods
  computed: {
    user () {
      return this.$store.state.user
    },
    appSettings () {
      return this.$store.state.appSettings
    },
    variables () {
      return this.$store.state.variables
    }
  }
}
</script>

<style scoped lang='scss'>

.Table {
    background-color: white;
}


</style>
