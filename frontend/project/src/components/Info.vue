<template>
  <div class="Appinfo">


    <b-button block v-on:click="gotoHome()"  class="btn btn-secondary"> Terug naar Home  </b-button>

    <div>
        <b-card no-body>
            <b-tabs card>
            <b-tab title="Introductie">
                <b-card-text>

                    <p>
                        Dit is een klaverjas spel dat met 4 personen op afstand met elkaar gespeeld kan worden. 
                        Hieronder wordt op hoofdlijnen het spel beschreven. In de andere tabs wordt ingegaan 
                        op de details.  
                    </p>

                    <h5>Status ontwikkeling</h5>
                    <p>
                        Het is niet de opzet om een perfect, professioneel spel te ontwikkelen. 
                        De huidige status is dat het spel redelijk stabiel en goed genoeg is om een avondje met 
                        vrienden een potje te klaverjassen. 
                        Toch heeft het spel nog een aantal bugs, 
                        maar die kunnen redelijk opvangen worden door de Tips te volgen.
                    </p>

                    <h5>Wedstrijden en potjes</h5>
                    <p>
                        Iedere speler kan een nieuwe wedstrijd aanmaken. Binnen een wedstrijd kunnen 1 of meerdere potjes worden 
                        aangemaakt. Een potje wordt gespeeld met 4 spelers: A-team en B-team, die tegelijkertijd zijn 
                        ingelogd voor dat potje. <br>
                        Pas als 4 spelers zich bij een potje hebben aangemeld verschijnt de knop 'speel dit potje'. 
                        Als hierop wordt gedrukt wordt het speelscherm opgestart met de speelkaarten. Een kaart kan pas 
                        worden gespeeld als alle spelers in het spel zitten (aangegeven met een groene ronde bol 
                        bij de kaart). Als een speler nog niet in het spel is, wordt dit aangegeven met een rode bol
                        en kan niet gespeeld worden. Dit merk je als je met de muis over de kaarten beweegt. Alleen als 
                        alle bollen groen zijn bewegen de kaarten als je met de muis hierover beweegt. <br>
                        Alleen de speler die aan de beurt is kan daadwerkelijk een kaart spelen.
                        De beurt wordt aangegeven met de licht groene kaartpositie in het midden van spel.<br>
                        Ieder potje binnen een wedstrijd bestaat uit hetzelfde aantal rondes dat 
                        moet worden gespeeld. Ook wordt ieder potje binnen een wedstrijd met exact dezelfde set aan gedeelde
                        kaarten gespeeld. Ieder potje binnen dezelfde westrijd speelt dus precies hetzelfde spel, zodat
                        de prestaties van de teams binnen een wedstrijd vergeleken kan worden.
                    </p>

                    <h5>Rotterdamse spelvariant</h5>
                    <p>
                        De Rotterdamse variant van het klaverjasspel wordt gespeeld met de volgende regels
                        <ul>
                            <li>Dezelfde speelkleur moet worden gespeeld</li>
                            <li>Er moet worden afgetroefd als de speelkleur niet kan worden gespeeld</li>
                            <li>Als je moet troeven dan moet je een hogere troefkaart spelen dan hetgeen aan troef al op tafel liggen.
                                Kan dat niet, dan mag je een lagere troefkaart neerleggen.
                            </li>
                        </ul> 
                    </p>

                    <h5>Verplicht aannemen</h5>
                    <p>
                        Bij een nieuwe ronde moet de speler die aan de beurt is aannemen. De aanneembeurt schuift 
                        iedere ronde een speler op en wordt in het middenvlak aangegeven door de lichtgroene lege positie 
                        waar de kaart gelegd wordt. <br>
                        Alleen de speler die moet aannemen kan de troef bepalen door in het midden van het scherm op de troefkleur 
                        te klikken. Zodra de juiste troefkleur geselecteerd is kan de ronde beginnen. Zodra de eerste slag is gespeeld 
                        kan de troef niet meer worden verandert totdat de volgende ronde begint.
                    </p>

                    <h5>Wat regelt het spel</h5>
                    <p>
                        Het spel regelt de volgende delen: 
                        <ul>
                            <li>het delen van de kaarten</li>
                            <li>wie moet aannemen</li>
                            <li>wie aan de beurt is om een kaart te spelen</li>
                            <li>wie een slag heeft gewonnen</li>
                            <li>het tellen van de punten in de slagen en bijhouden van de totaal score</li>
                            <li>na een ronde vaststellen of een team 'door' of 'nat' is.</li>
                        </ul>
                        Alle overige zaken moeten de speler zelf regelen, zoals troef melden en registreren, of 
                        aangeven dat iemand heeft verzaakt.
                    </p>

                </b-card-text>
            </b-tab>

            <b-tab title="Toelichting">
                <b-card-text>

                    <h5>Inhoudsopgave</h5>
                    <p>
                        <ul>
                            <li><a href="#ref_aanmelden">Registreren en inloggen </a></li>
                            <li><a href="#ref_wachtwoord_vergeten">Wachtwoord vergeten</a></li>
                            <li><a href="#ref_terminologie">Terminologie</a></li>
                            <li><a href="#ref_wedstrijden">Wedstrijden</a></li>
                        </ul>
                    </p>

                    <p>
                        Hieronder staat een beknopte toelichting op de mogelijkheden die het spel biedt
                    </p>


                    <h3 id="ref_aanmelden">Registreren en inloggen</h3>
                    <p>
                        Een speler kan toegang krijgen tot het spel door zicht eerst te registreren 
                        en vervolgens in te loggen
                    </p>
                    <h5>Registreren</h5>
                    <p>
                        Als je nog geen gebruikers account hebt dan kan je jezelf registeren via de inlog pagina.
                        Bij het registreren moet een gebruikersnaam worden gekozen. Dit is de naam die wordt gebruikt 
                        bij het inloggen en die wordt getoond in het spel.
                    </p>
                    <p>
                        Er moet een geldig e-mail adres worden opgegeven. Dit e-mail adres wordt gebruikt als u uw 
                        wachtwoord bent vergeten en een nieuw wachtwoord moet worden vastgelegd.
                    </p>
                    <p>
                        Het wachtwoord dat u kiest moet voldoen aan de volgende voorwaarden:
                        <ul>
                            <li>Het wachtwoord mag bestaan uit cijfers en letters</li>
                            <li>Wachtwoord bevat minimaal 8 characters</li>
                            <li>Wachtwoord mag niet uit alleen cijfers bestaan</li>
                            <li>Wachtwoord mag niet te eenvoudig zijn</li>
                        </ul>
                    </p>

                    <h5>Inloggen</h5>
                    <p>
                        Als je niet bent ingelogd dan wordt je eerst automatisch doorgezet naar de login pagina.
                        Gebruik je gebruikersnaam en wachtwoord. 
                    </p>

                    <h5>Uitloggen</h5>
                    <p>
                        In het top menu bij de drie horizontale streepje (zichtbaar bij small scherm) zit de knop om 
                        uit te loggen. Als je niet uitlogt en later weer naar het spel gaat dan kan je weer verder. 
                        De inlog rechten zijn maar een aantal uren geldig. Daarna moet weer worden ingelogd.
                    </p>

                    <h3 id=ref_wachtwoord_vergeten>Wachtwoord vergeten</h3>
                    <p>
                        Als u uw wachtwoord bent vergeten dan kunt u een nieuw wachtwoord instellen via 
                        'wachtwoord vergeten' bij het inlog menu.
                        
                    </p>

                    <h5>Opvragen wachtwoord resetcode</h5>
                    <p>
                        Om uw wachtwoord te kunnen wijzigen heeft u een wachtwoord resetcode nodig. 
                        Deze kan worden aangevraagd in het scherm 'wachtwoord vergeten'. 
                        U kunt uw unieke gebruikernaam gebruiken om de code aan te vragen. In dat geval wordt direct
                        een mail gestuurd met uw reset code.
                    </p>
                    <p>
                        U kunt ook uw email adres gebruiken om de reset code aan te vragen.
                        Het kan zijn dat u meerdere gebruikersnamen heeft geregistreerd 
                        op dit email adres. In dat geval wordt eerst een mail naar u gestuurd met daarin 
                        vermeld de gebruikersnamen die op dit email adres geregistreerd staan. 
                        Daarna kunt u de juiste gebruikersnaam invullen in het 'wachtwoord vergeten' scherm, waarna
                        de resetcode naar u wordt verstuurd.
                    </p>
                    <p>
                        De resetcode is 15 minuten geldig.
                    </p>

                    <h5>Instellen nieuw wachtwoord</h5>
                    <p>
                        Zodra u een resetcode heeft onvangen kunt u in het 'wachtwoord vergeten scherm' de resetcode invullen en
                        vervolgens een nieuw wachtwoord instellen.
                    </p>

                    <h3 id=ref_terminologie>Terminologie</h3>
                    <p>
                        In het spel worden een aantal termen gebruikt die hieronder nader worden uitgelegd
                    </p>
                    <p>
                        <ul>
                            <li>
                                <b>Slag</b> <br>
                                Een slag is wanneer iedere speler een kaart speelt en een winnaar de slag kan binnenhalen (wint)
                            </li>
                            <li>
                                <b>Ronde</b>
                                Een ronde is het spelen van alle kaarten vanuit de hand van de spelers.
                                Een ronde bestaat uit het spelen van 8 slagen.
                                In een ronde wordt de troef bepaald en aan het einde van de ronde worden de punten van de slagen 
                                geteld.
                            </li>
                            <li>
                                <b>Potje</b> <br>
                                Een potje is wanneer twee teams tegen elkaar spelen (aan een tafel). Een potje heeft een 
                                vastgesteld aantal rondes dat gespeeld moet worden in het potje. 
                            </li>
                            <li>
                                <b>Wedstrijd</b> <br>
                                Binnen een wedstrijd kunnen meerdere teams aan verschillende 'tafels' 
                                een potje spelen. Alle potjes binnen dezelfde wedstrijd spelen hetzelfde aantal rondes en met exact
                                dezelfde set aan gedeelde kaarten. Hierdoor kan het resultaat van een potje vergelijken worden 
                                met de andere potjes binnen dezelfde wedstrijd.
                            </li>
                        </ul>
                    </p>

                    <h3 id=ref_wedstrijden>Wedstrijden</h3>
                    <p>
                        Via de wedstrijd pagina kunt u een overzicht opvragen van alle wedstrijden. Tevens kan iedere
                        speler een nieuwe wedstrijd aanmaken.
                    </p>

                    <h5>Nieuwe wedstrijd aanmaken</h5>
                    <p>
                        Via de knop 'Nieuwe wedstrijd maken' kan een nieuwe wedstrijd worden aangemaakt. 
                        Er verschijnt een formulier waarin een aantal velden moeten worden ingevuld.
                    </p>
                    <p>
                        <ul>
                            <li>
                                <b>Naam van de Wedstrijd</b> <br>
                                Dit is de unieke naam die wordt getoond in het overzicht met wedstrijden.
                            </li>
                            <li>
                                <b>Omschrijving</b> <br>
                                Dit kan worden gebruikt om het type wedstrijd te omschrijven, zodat anderen deze 
                                wedstrijd kunnen herkennen.
                            </li>
                            <li>
                                <b>Aantal rondes</b> <br>
                                Defineer het aantal rondes dat per potje binnen deze wedstrijd moet worden gespeeld 
                                Dit moet tussen tussen 1 en 100 liggen.
                            </li>
                            <li>
                                <b>Start datum wedstrijd</b> <br>
                                Dit is de datum vanaf wanneer de potjes van deze wedstrijd gespeeld mogen worden.
                            </li>
                            <li>
                                <b>Stop datum wedstrijd</b> <br>
                                Stop datum wedstrijd is de datum vanaf wanneer geen potjes van deze wedstrijd gespeeld mogen worden.
                            </li>
                            <li>
                                <b>Stop registreer datum</b> <br>
                                Speler kunnen zich aanmelden bij een potje. 
                                De Stop registeer datum is de datum vanaf wanneer spelers zich niet meer bij potjes van 
                                deze wedstrijd kunnen aanmelden. Deze datum moet liggen voor de Stop datum.
                            </li>
                        </ul>
                    </p>

                    <h5>Overzicht wedstrijden</h5>
                    <p>
                        Via de knop 'Overzicht wedstrijden' krijgt u een overzicht te zien van alle wedstrijden die 
                        zijn aangemaakt door alle spelers. De wedstrijd wordt getoond in een bepaalde kleur afhankelijk van de 
                        status waarin de wedstrijd zich bevindt.
                    </p>
                    <p>
                        <ul>
                            <li>
                                <b>Groen: </b> <br> 
                                Spelers mogen registreren bij potje en potje mag gestart worden.
                            </li>
                            <li>
                                <b>Geel:</b> <br>
                                
                            </li>
                        </ul>
                    </p>
                    




                    kleur 
                    aanmaken wedstrijd






                    
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
                    

                    <h5 id="ref_beurt">Beurt</h5>
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
                        Dit is spel is ter vermaak ontwikkelt 
                        en heeft op dit moment een fase bereikt waarbij het redelijk goed gespeeld kan worden. 
                        Toch ontbreken nog een aantal gewenste functionaliteiten en loopt er soms iets niet geheel goed. 
                        Mocht u bugs tegenkomen of tips en suggesties voor verbetering hebben dan kunt u die sturen 
                        naar klaverjasfun@gmail.com.
                    </p>
                    <p>
                        Hieronder staan een aantal tips om het spel goed te laten verlopen
                    </p>

                    <h5>Op afstand spelen</h5>

                    <p>
                        Dit spel biedt de mogelijkheid om met elkaar een potje te klaverjassen op afstand. 
                        Om de gezelligheid van het klaverjassen te blijven ervaren wordt aanbevolen het spel te spelen
                        terwijl je met elkaar in een video meeting zit, zoals met Zoom of Microsoft Teams.
                    </p>

                    <h5>Keuze browsers</h5>
                    <p>
                        Het spel is geen aparte app, maar wordt gespeeld vanuit de browser. 
                        Dit kan vanaf een PC, laptop, tablet of mobiele telefoon. 
                        Ervaring dusverre geeft aan dat het spel goed werkt met Google Chrome, 
                        Firefox Opera en Vivaldi browsers. <br>
                        Bekend is dat de huidige versie niet goed samenwerkt met Apple apparatuur en Internet Explorer. 
                    </p>

                    <h5>Gebruik de buttons</h5>
                    <p>
                        Gebruik de buttons van het spel om door het spel te navigeren. 
                        Gebruik NIET de 'Go-back' knop van de browser om terug te gaan naar een vorig scherm.
                    </p>

                    <h5>Scherm layout</h5>
                    <p>
                        Dit spel werkt op zowel PC, laptop als mobiel. Het scherm pas zich automatisch aan.
                        Op de PC kan de browser het best worden ingesteld met een smalle breedte.
                        Op tablet of telefoon moet je het toestel rechtop houden, ofwel in portait stand. 
                        In een landscape stand passen de kaarten niet geheel op het scherm en staan de kaarten te ver uit elkaar. <br>
                        Op mobiele telefoon en tablet wordt de browser gebruikt in 'fullscreen' modus, waardoor het spel 
                        er uitziet als een app.
                    </p>

                    <h5>Goede internet connectie</h5>
                    <p>
                        Om het spel goed te kunnen spelen moeten all spelers tegelijkertijd in verbinding staan met het spel. 
                        Bij een slechte verbinding van een speler kan het spel haperen. Zodra een speler even connectie verliest 
                        zal de huidige slag worden gereset. De kaarten van deze slag moeten dan weer opnieuw gespeeld worden.
                    </p>

                    <h5>Reset een slag</h5>
                    <p>
                        Soms wordt een kaart gespeeld, maar wordt dit niet goed getoond bij de andere spelers. 
                        Ga dan naar de Actie-knop en kies Reset-slag. 
                        Hiermee kan de gehele slag opnieuw worden gespeeld. <br>
                        Ook kan de reset worden gebruik indien een speler per ongeluk een verkeerde kaart heeft neergelegd.<br><br>
                        Zodra een slag eenmaal is genomen (vastgelegd), kan deze niet meer gereset worden.
                    </p>

                    <h5>Roem</h5>
                    <p>
                        Het is de verantwoordelijkheid van de spelers zelf om roem te registreren.
                        Roem moet worden vastgelegd door de speler die de slag wint. 
                        Zodra alle kaarten van een slag zijn gespeeld dan verschijnt bij de speler die de slag gewonnen heeft 
                        een tweetal knoppen: knop om roem vast te leggen en een knop om de slag te nemen. <br>
                        Eerst moet de roem worden geregisteerd en dan pas de slag worden 'binnengehaald'. 
                        Als een slag is binnengehaald, kan de roem niet meer worden aangepast. 
                        Hooguit kan in een volgende slag ter correctie een negatieve roem worden vastgelegd.
                    </p>

                    <h5>Synchronisatie</h5>
                    <p>
                        Speel de kaarten niet te snel achter elkaar om synchronisatie issues te vermijden.
                    </p>


                    <h5>Reset in browser</h5>
                    <p>
                        Mocht het spel niet meer goed werken dan kan je het best het https adres nog een keer intikken
                        in de browser zodat de pagina's opnieuw geladen worden. Tip: doe dit twee keer achter elkaar. De gegevens 
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
                        Dit is spel is ontwikkeld door Ole Karlsen.
                        De drijver om dit spel op te zetten was drieledig. <br> <br>
                        <ul>
                            <li>Een tijdverdrijf te vinden gedurende de Corona lockdown periode</li>
                            <li>Kennis vergroting</li>
                            <li>Een leuke manier vinden om op afstand met elkaar een spel te kunnen spelen</li>
                        </ul>
                    </p>
                    <p>
                        Het is niet de opzet om een perfect, professioneel spel te ontwikkelen. De huidige status is 
                        dat het spel redelijk stabiel en goed genoeg is om een avondje met vrienden een potje te klaverjassen.
                        Toch heeft het spel nog een aantal bugs, maar die kunnen redelijk opvangen worden door de Tips te volgen.
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
