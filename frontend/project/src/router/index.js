import Vue from 'vue'
import VueRouter from 'vue-router'
import Apphome from '../components/registration/Home.vue'
import Applogin from '../components/registration/Login.vue'
import Appregistration from '../components/registration/Registration.vue'
import Appresetpassword from '../components/registration/ResetPassword.vue'
import Appmatches from '../components/Matches.vue'
import Appmatchcreate from '../components/Match_create.vue'
import Appmatchlist from '../components/Match_list.vue'
import Appmatchdetails from '../components/Match_details.vue'
import Appgamesoverview from '../components/Games_overview.vue'
import Appgameplay from '../components/Game_play.vue'
import Appgamescore from '../components/Games_score.vue'
// import Appgameslagen from '../components/Games_slagen.vue'
import Appremarks from '../components/Remarks.vue'
import Appinfo from '../components/Info.vue'
import Appchat from '../components/Chat.vue'
import Apptestluck from '../components/TestLuck.vue'
import Appplaydices from '../components/PlayDices.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', name: 'Home', component: Apphome },
  { path: '/Login', name: 'Login', component: Applogin },
  { path: '/Registration', name: 'Registration', component: Appregistration },
  { path: '/ResetPassword', name: 'ResetPassword', component: Appresetpassword },
  { path: '/Matches', name: 'Matches', component: Appmatches, meta:{title: 'Wedstrijden'} },
  { path: '/Matches/Create', name: 'Match_create', component: Appmatchcreate },
  { path: '/Matches/List', name: 'Match_list', component: Appmatchlist },
  { path: '/Matches/Details/:id', name: 'Match_details', component: Appmatchdetails },
  { path: '/Matches/Games', name: 'Games_overview', component: Appgamesoverview },
  { path: '/Matches/Games/play', name: 'Game_play', component: Appgameplay },
  { path: '/Matches/Games/score', name: 'Game_score', component: Appgamescore },
  // { path: '/Matches/Games/score/slagen', name: 'Game_slagen', component: Appgameslagen },
  { path: '/Remarks', name: 'Remarks', component: Appremarks },
  { path: '/Info', name: 'Info', component: Appinfo },
  { path: '/Chat', name: 'Chat', component: Appchat },
  { path: '/Testluck', name: 'TestLuck', component: Apptestluck },
  { path: '/PlayDices', name: 'PlayDices', component: Appplaydices },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
