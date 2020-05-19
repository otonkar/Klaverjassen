<template>
  <div class="Appinfo">


    <b-button block v-on:click="gotoHome()"  class="btn btn-secondary"> Terug naar Home  </b-button>

    <div>
        <b-card no-body>
            <b-tabs card>
            <b-tab title="Toelichting">
                <b-card-text>

                    <p>
                        Hieronder staat een beknopte toelichting op de mogelijkheden die het spel biedt
                    </p>
                    <h5>inloggen</h5>
                    <p>
                        Als je niet bent ingelogd dan wordt je eerst automatisch doorgezet naar de login pagina.
                        Gebruik je gebruikersnaam en wachtwoord. 
                    </p>
                    <h5>Useraccount registeren</h5>
                    <p>
                        Als je nog geen gebruikers account hebt dan kan je jezelf registeren via de inlog pagina.
                    </p>

                    <h5>Uitloggen</h5>
                    <p>
                        In het top menu bij de drie horizontale streepje (zichtbaar bij small scherm) zit de knop om 
                    uit te loggen. Als je niet uitlogd en later weer naar het spel gaat dan kan je weer verder. 
                    De inlog rechten zijn maar een aantal uren geldig. Daarna moet weer worden ingelogd.
                    </p>
                    
                    <h5>Spelen van een potje</h5>
                    <p>
                        Een portje kan pas worden gespeeld als 4 spelers zich bij het potje hebben geregistreerd.
                        Dan pas wordt een knop zichtbaar met 'Speel dit potje'. Het potje gaat verder met de ronde en
                        slag waar de laatste keer is gestopt. Pas als alle 4 de spelers in het speelscherm zitten kan 
                        een kaart worden gespeeld. 
                    </p>

                    <h5>Troef kiezen</h5>
                    <p>
                        In het midden van het scherm is de troef zichtbaar. Voordat de eerste kaart van een ronde is gespeeld
                    kan de troef worden aangepast door de speler die als eerste moet uitkomen. Door één of meerdere keren op 
                    de troef te klikken kan de gewenste troef worden gekozen. Zodra de eerste kaart van de ronde is gespeeld kan 
                    de troef niet meer worden aangepast tot aan de volgende ronde.
                    </p>
                    <p>
                        Op dit moment kan alleen de speler die als eerste moet uitkomen de troef aanpassen. 
                        Dit biedt de mogelijkheid om een spelvorm te spelen, waarbij deze speler moet aannemen en 
                        zelf de troef mag kiezen.
                    </p>
                    <p>
                        Later zal een mogelijkheid worden toegevoegd om aan te nemen en te passen.
                    </p>
                    

                    <h5>Beurt</h5>
                    <p>
                        Na iedere ronde moet een volgende speler als eerste uitkomen. Indien een speler aan de beurt is 
                    dan wordt de naam vergroot en geel aangegeven. Bij iedere slag wordt bepaald wie de slag heeft gewonnen.
                    De winnaar van de slag moet als eerste uitkomen.
                    </p>
                    


                    <h5>... toe te voegen..</h5>

                    


                </b-card-text>
            </b-tab>

            <b-tab title="Tips">
                <b-card-text>
                    <p>
                        Dit spel bevindt zich in een ontwikkelfase en kan hierdoor in een sitatie komen dat 
                        het niet meer goed functioneert. Hieronder staan een aantal tips het spel goed te laten verlopen
                    </p>

                    <h5>Gebruik de buttons</h5>
                    <p>
                        Het spel draait in een browser op de PC, tablet of telefoon. Om terug te gaan naar voorgaande schermen 
                        moeten de buttons worden gebruikt die in het spel aanwezig zijn. 
                        Gebruik niet de 'terug' knop van de browser zelf
                    </p>

                    <h5>Scherm layout</h5>
                    <p>
                        Dit spel werkt op zowel PC, laptop als mobiel. Het scherm pas zich automatisch aan.
                        Op de PC kan de browser het best worden gesteld met een smalle breedte.
                    </p>
                    <p>
                        Op tablet of telefoon moet je het toestel rechtop houden, ofwel in portait stand.
                        In een landscape stand passen de kaarten niet geheel op het scherm en staan de 
                        kaarten te ver uit elkaar.
                    </p>

                    <h5>Reset in browser</h5>
                    <p>
                        Mocht het spel niet meer goed werken dan kan je het best het http adres nog een keer intikken
                        zodat de pagina's opnieuw geladen worden. Tip: doe dit twee keer achter elkaar. De gegevens 
                        worden dan gereset. 
                    </p>
           
                    

                </b-card-text>
            </b-tab>

            <b-tab title="Backlog">
                <b-card-text>
                    <p>Hieronder staat een lijst met mogelijke verbeteringen of aanvullingen die 
                        op dit spel gemaakt kunnen worden
                    </p>
                    <ul>
                        <li>Mogelijkheid om aan te nemen of te passen</li>
                        <li>Mogelijkheid om een gehele ronde opnieuw te spelen</li>
                        <li>Het inzien van gemaakt slagen</li>
                        <li>Uitgebereidere rapportages over gemaakte scores en het vergelijken van games</li>
                        <li>Het 'afspelen' van een gespeeld potje</li>
                    </ul>
                </b-card-text>
            </b-tab>

            <b-tab title="Credits">
                <b-card-text>
                    
                    <p>
                        Dit is spel is ontwikkeld door Ole Karlsen. <br>
                        De drijver om dit spel op te zetten was drieledig. <br> <br>
                        <ul>
                            <li>Een tijdverdrijf te vinden gedurende de lockdown periode</li>
                            <li>Kennis vergroting</li>
                            <li>Een leuke manier vinden om op afstand met elkaar een spel te kunnen spelem</li>
                        </ul>
                    </p>
                    <p>
                        Dit spel bevindt zich in een ontwikkelfase en bevat daardoor nog veel 'bugs'. 
                        Als de normale flow van het spel wordt gevolgd dan werkt het redelijk. Mocht u heen en weer springen 
                        door de schermen dan is de kans aanwezig dat het spel vastloopt.
                    </p>

                    <p>
                        De bedoeling is dat de komende periode 
                        kleine verbetering worden doorgevoerd. Mocht je suggesties of feedback hebben, 
                        stuur die dan naar <br> <br>
                        mail: klaverjasfun@gmail.com
                    </p>


                </b-card-text>
            </b-tab>
            </b-tabs>
        </b-card>
    </div>



    

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Appinfo',
  data () {
    return {
      title: 'info page'
    }
  },
  activated: function () {
      // console.log(this.$route.name)
      // Do not show full screen on login page
      // document.exitFullscreen();
      this.user.show_header = true
      this.$store.dispatch('updateUser', this.user)

      if (this.user.user_is_logged_in === false) {
          this.$router.push({ name: 'Home' })
      } //END if

  },//END activated
  methods: {
    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    }  //END gotoHome

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
