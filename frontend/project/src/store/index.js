import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: '',
      password: '',   
      id: '',                     // Needed to register in django based on pk
      user_is_logged_in: false,    // used to decided which elements to show on pages
      // Store the tokens on localStore, so that these can be used 
      //   when a user uses the application a next time (when still valid)
      // access_token: '',
      // refresh_token: '',
      show_header: true
      
    },
    appSettings: {
      // url_api_base            : 'http://192.168.2.80:8000/',
      // url_api_base            : 'http://192.168.2.80:7000/',
      // url_api_base            : 'https://klaverjasfun.nl/api/',
      // url_api_base            : 'http://klaverjasfun.nl:5000/',
      url_api_base            : 'http://145.53.40.4:8000/',
      // url_Websocket           : 'ws:192.168.2.80:8000/ws/game/',
      // url_Websocket           : 'wss:klaverjasfun.nl/ws/game/',
      // url_Websocket           : 'ws:klaverjasfun.nl:5000/ws/game/',
      url_Websocket           : 'ws:145.53.40.4:8000/ws/game/',
      url_get_token           : 'registration/token/',
      url_refresh_token       : 'registration/token/refresh/',
      url_logout              : 'registration/logout/',
      url_registration        : 'registration/signup/',
      url_match_create        : 'klaverjas/matches/create/',
      url_match_list          : 'klaverjas/matches/list',
      url_match_details       : 'klaverjas/matches/',
      url_games_create        : 'klaverjas/games/create',
      url_games_list          : 'klaverjas/games/search/?',
      url_game_score          : 'klaverjas/games/score/?',
      url_game_slagen         : 'klaverjas/games/slagen/?',
      url_game_players        : 'klaverjas/players/search/?',
      url_game_players_create : 'klaverjas/players/create/',
      url_game_players_rud    : 'klaverjas/players/',                     // Retreive, Update, Delete
      url_user_details        : 'klaverjas/users/',
      url_test                : 'test/',
    },
    variables: {                                                        // To store variables like show block on screen
      show_slagen             : false                                   // To show the slagen component
    },
    window_size: {
      width: 0,
      height: 0
    },
  },//END state
  mutations: {
    updateUser: (state, payload) => {
      state.user = payload
    },
    updateWindow_size: (state, payload) => {
      state.window_size = payload
    },
    updateVariables: (state, payload) => {
      state.variables = payload
    },
  },//END Mutations
  actions: {
    updateUser: (context, payload) => {
      context.commit('updateUser', payload)
    },
    updateWindow_size: (context, payload) => {
      context.commit('updateWindow_size', payload)
    },
    updateVariables: (context, payload) => {
      context.commit('updateVariables', payload)
    },
  },//END actions
  modules: {
  }
})
