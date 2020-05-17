<template>
  <div class="Appgames_slagen" v-if="isLoaded">

        <h5>Slag potje: {{ gameID }}, ronde: {{ leg + 1 }} </h5>
        <p>Troef : {{ troef_name }} </p>
        <div class="Table" v-if="show_game_slagen">
            <b-table-simple small responsive>
                
                <!-- <colgroup><col></colgroup>
                <colgroup><col><col><col><col></colgroup>
                <colgroup><col><col></colgroup> -->
                <!-- <colgroup><col><col></colgroup> -->
                <b-thead head-variant="light">
                <b-tr >
                    <b-th colspan="1" class="text-center" ></b-th>
                    <b-th colspan="4" class="text-center" >player</b-th>
                    <b-th colspan="1" class="text-center" ></b-th>
                    <b-th colspan="1" class="text-center" ></b-th>
                </b-tr>
                <b-tr >
                    <b-th colspan="1" >#</b-th>
                    <b-th colspan="1" class="text-center" >1</b-th>
                    <b-th colspan="1" class="text-center" >2</b-th>
                    <b-th colspan="1" class="text-center" >3</b-th>
                    <b-th colspan="1" class="text-center" >4</b-th>
                    <b-th colspan="1" class="text-center" >win</b-th>
                    <b-th colspan="1" class="text-center" >roem</b-th>
                </b-tr>
                </b-thead>
                <!-- game_slagen should contain 0 or 1 slag -->
                <b-tbody >
                    <b-tr >
                    <b-th class="success"> {{ game_slagen[0].n_slag + 1 }} </b-th>
                    <b-th v-bind:variant="[game_slagen[0].position_start===0 ? 'success': 'light']"> <img v-bind:src="game_slagen[0].cards_slag[0]['color']" width="15px">  {{ game_slagen[0].cards_slag[0]['rank'] }}    </b-th>
                    <b-th v-bind:variant="[game_slagen[0].position_start===1 ? 'success': 'light']"> <img v-bind:src="game_slagen[0].cards_slag[1]['color']" width="15px">  {{ game_slagen[0].cards_slag[1]['rank'] }}    </b-th>
                    <b-td v-bind:variant="[game_slagen[0].position_start===2 ? 'success': 'light']"> <img v-bind:src="game_slagen[0].cards_slag[2]['color']" width="15px">  {{ game_slagen[0].cards_slag[2]['rank'] }}   </b-td>
                    <b-td v-bind:variant="[game_slagen[0].position_start===3 ? 'success': 'light']"> <img v-bind:src="game_slagen[0].cards_slag[3]['color']" width="15px">  {{ game_slagen[0].cards_slag[3]['rank'] }}  </b-td>
                    <b-td variant="light"> {{ game_slagen[0].player_won + 1 }}  </b-td>
                    <b-td variant="light"> {{ game_slagen[0].roem }}  </b-td>
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

         <b-button variant="primary" @click="doCloseSlag()" >Sluiten</b-button>

  </div>
</template>

<script>

// Want to use this component with simple input
//  * gameID
//  * leg  (integer)
// This component can be use to show the slagen of both completed and not completed legs


export default {
  name: 'Appgamepreviousslag',
  props: {
    gameID: Number,
    leg: Number,
    round: Number,
  },

  data () {
    return {
        title: 'Game previous slag',
        isLoaded: false,            // to rerender the page when data is loaded
        errors: {},
        game_slagen: [], 
        test: false,
        // leg: 0,
        // gameID: 0,
        troef_name: '----',
        show_game_slagen: false
        
    }
  },

  mounted: function () {
        // On event changeLeg do the method doGetSlag

        // console.log('mounted : ', this.gameID, this.leg)
        this.$root.$on('changeLeg', lega => this.doGetSlag(this.gameID, lega, this.round) )
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
            // Get the match details
            await this.doGetSlag(this.gameID, this.leg, this.round)

        }//END if
  },//END activated

  methods: {

    goBack: function () {
        this.variables.show_slagen = false
        this.$store.dispatch('updateVariables', this.variables)
        this.$router.go(-1)
    },  //END goBack

    // getImage: function (img) {
    //     // img = '"' + img + '"'
    //     this.my_image = img
    //     // console.log(my_image)

    //     return img

    // }, //END getImage

    doGetSlag: async function (gameID, lega, round) {
        // Show the current score of the game

       // Do  use 'api_request' or axios, so that this call WILL use the interceptors
        const api_request = require('axios')
        // console.log('DUMMY5')

        // Get all the players of a match
        await api_request({
            method: 'get',
            url: this.appSettings.url_game_slagen + 'gameID=' + gameID + '&leg=' + lega + '&n_slag=' + round
            // data: this.input
        })
        .then(response => {
            if (response.status === 200) {
                this.game_slagen = response.data
                // // console.log(this.test)
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
        
        // Should only be 0 or 1 slag
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
        }

        // console.log(this.game_slagen)

        this.isLoaded = true

        // this.$forceUpdate()

    }, //END doGetScores

    doCloseSlag: function () {
        this.variables.show_slag = false
        this.show_game_slagen = false
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
