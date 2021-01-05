<template>
  <div class="Appinfo">


    <b-button block v-on:click="gotoHome()"  class="btn btn-secondary"> Terug naar Home  </b-button>

    <div>
        <b-card no-body>
            <b-tabs card>
            <b-tab title="Introductie">
                <b-card-text>

                    <p>
                        Dit is een klaverjasspel dat met 4 personen on-line met elkaar gespeeld kan worden. 
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
                        Iedere speler kan een nieuwe wedstrijd aanmaken. 
                        Zodra een wedstrijd is aangemaakt en de de registratieperiode voor deze wedstrijd begonnen is, dan 
                        kunnen binnen deze wedstrijd 1 of meerdere potjes worden aangemaakt.
                        Een potje wordt gespeeld met 4 spelers: A-team en B-team. die tegelijkertijd zijn 
                        ingelogd voor dat potje.
                    </p>
                    <p>
                        Pas als 4 spelers zich bij een potje hebben aangemeld verschijnt de knop 'speel dit potje'. 
                        Als hierop wordt gedrukt wordt het speelscherm opgestart met de speelkaarten. Een kaart kan pas 
                        worden gespeeld als alle spelers in het spel zitten (aangegeven met een groene ronde bol 
                        bij de kaart). Als een speler nog niet in het spel is, wordt dit aangegeven met een rode bol
                        en kan niet gespeeld worden. Dit merk je als je met de muis over de kaarten beweegt. Alleen als 
                        alle bollen groen zijn bewegen de kaarten als je met de muis hierover beweegt. 
                        Alleen de speler die aan de beurt is kan daadwerkelijk een kaart spelen.
                        De beurt wordt aangegeven met de licht groene kaartpositie in het midden van spel.
                    </p>
                    <p>
                        Ieder potje binnen een wedstrijd bestaat uit hetzelfde aantal rondes dat 
                        moet worden gespeeld. Ook wordt ieder potje binnen een wedstrijd met exact dezelfde set aan gedeelde
                        kaarten gespeeld. Ieder potje binnen dezelfde westrijd speelt dus precies hetzelfde spel, zodat
                        de prestaties van de teams binnen een wedstrijd vergeleken kan worden.
                    </p>
                        
                        
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

                    <h5 id="inhoudsopgave">Inhoudsopgave</h5>
                    <p>
                        <ul>
                            <li><a href="#ref_aanmelden">Registreren en inloggen </a></li>
                            <li><a href="#ref_wachtwoord_vergeten">Wachtwoord vergeten</a></li>
                            <li><a href="#ref_terminologie">Terminologie</a></li>
                            <li><a href="#ref_wedstrijden">Wedstrijden</a></li>
                            <li><a href="#ref_potjes">Potjes</a></li>
                            <li><a href="#ref_speel_potje">Het spelen van een Potje</a></li>
                            <li><a href="#ref_melden_verzaken">Melden verzaken</a></li>
                            <li><a href="#ref_berichten">Berichten</a></li>
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
                        Als je nog geen gebruikersaccount hebt dan kan je jezelf registeren via de inlog pagina.
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

                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>

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

                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>

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
                                dezelfde set aan gedeelde kaarten. Hierdoor kan het resultaat van een potje vergeleken worden 
                                met de andere potjes binnen dezelfde wedstrijd.
                            </li>
                        </ul>
                    </p>

                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>

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
                                Stop datum wedstrijd is de datum vanaf wanneer geen potjes van deze wedstrijd gestart mogen worden.
                                Potjes die al gestart zijn mogen worden uitgespeeld.
                            </li>
                            <li>
                                <b>Stop registreer datum</b> <br>
                                De Stop registeer datum is de datum vanaf wanneer spelers geen potjes meer kunnen aanmaken 
                                en zich niet meer bij potjes van deze wedstrijd kunnen aanmelden. 
                            </li>
                        </ul>
                    </p>

                    <h5 id="kleur">Overzicht wedstrijden</h5>
                    <p>
                        Via de knop 'Overzicht wedstrijden' krijgt u een overzicht te zien van alle wedstrijden die 
                        zijn aangemaakt door alle spelers. De wedstrijd wordt getoond in een bepaalde kleur afhankelijk van de 
                        status waarin de wedstrijd zich bevindt.
                    </p>
                    <p>
                        <ul>
                            <li>
                                <b>Blauw:</b> <br>
                                Wedstrijd is nog niet gestart, registratie bij een potje mag nog plaatsvinden. <br>
                                Spelers mogen potjes aanmaken, zich aan- en afmelden bij een potje.
                                Nieuwe potjes mogen niet gestart worden om te spelen. 
                                Wel mag een reeds gestart potje worden uitgespeeld.
                            </li>
                            <li>
                                <b>Grijs:</b> <br>
                                Wedstrijd is nog niet gestart, registratie mag niet meer plaatsvinden. <br>
                                Spelers mogen geen potjes aanmaken, zich aan- en afmelden bij een potje of een potje starten om te spelen.
                                Wel mag een reeds gestart potje worden uitgespeeld.
                                
                            </li>
                            <li>
                                <b>Groen: </b> <br> 
                                Wedstrijd is gestart, maar nog niet gestopt en registratie mag nog plaatsvinden. <br>
                                Spelers mogen potjes aanmaken, potjes starten en zich aan/af melden bij potjes.
                            </li>
                            <li>
                                <b>Geel:</b> <br>
                                Wedstrijd is gestart, maar nog niet gestopt en registratie mag niet meer plaatsvinden. <br>
                                Spelers mogen potjes aanmaken en zich niet meer aan- en afmelden bij een potje.
                                Wel mag een potje gestart worden om te spelen.                               
                            </li>
                            <li>
                                <b>Rood:</b> <br>
                                Wedstrijd is gestopt. <br>
                                Spelers mogen geen potjes meer aanmaken of zich aanmelden bij potje.
                                Potjes mogen niet meer gestart worden. Reeds gestarte potjes mogen wel afgespeeld worden.
                                Spelers van buiten dit potje mogen de gespeelde slagen inzien.
                            </li>
                        </ul>
                    </p>

                    <h5>Filter op wedstrijd</h5>
                    <p>
                        In het overzicht van wedstrijden heeft u de mogelijkheid de lijst met wedstrijden te verkleinen 
                        door 1 of meerdere filters te gebruiken. U kunt dit doen door een zoekterm in het veld van het 
                        filter te plaatsen. Hierdoor wordt de lijst gefilterd op de betreffende term. Ook kunt u via een 
                        dropdown menu filteren op de status (kleur) van de wedstrijd. Middels de knop 'Verwijder filters'
                        worden alle filters verwijderd en is de volledige lijst met wedstrijden zichtbaar.
                    </p>

                    <h5>Wedstrijd details</h5>
                    <p>
                        Vanuit het 'Overzicht potjes' kan via 'Wedstrijd details' de informatie van de wedstrijd 
                        worden opgevraagd. Ook is het mogelijk bepaalde details aan te passen. Hiervoor gelden de volgende 
                        regels:
                        <ul>
                            <li>Alleen de eigenaar van de wedstrijd mag de details aanpassen</li>
                            <li>Naam van wedstrijd en eigenaar kunnen niet worden aangepast</li>
                            <li>Het aantal rondjes per potje kan alleen worden aangepast zolang geen enkel potje
                                van deze wedstrijd is gestart.
                            </li>
                        </ul>
                    </p>

                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>


                    <h3 id=ref_potjes>Potjes</h3>
                    <p>
                        Als vanuit 'Overzicht wedstrijden' op een wedstrijd wordt geklikt dan kom je in het scherm van 
                        'Overzicht potjes'. Vanuit dit scherm kunnen nieuwe potjes binnen de wedstrijd worden aangemaakt 
                        en kunnen spelers zich aanmelden bij een portje om te spelen. Dit kan echter alleen wanneer de wedstrijd 
                        de juiste <a href="#kleur">status </a> (kleur) hiervoor heeft en zolang het betreffende potje nog niet is uitgespeeld.
                    </p>

                    <h5>Nieuw potje aanmaken</h5>
                    <p>
                        Alleen als de wedstrijd in een status is dat nog nieuwe potjes mogen worden aangemaakt zal een knop 
                        zichtbaar zijn met 'Nieuw potje aanmaken'. Iedere speler kan dan een nieuwe potje aanmaken. Het nieuwe potje
                        krijgt een ID met een nummer dat uniek is voor het potje.  
                    </p>

                    <h5>Status van een potje</h5>
                    <p>
                        Een potje kan zich in de volgende statussen bevinden:

                        <ul>
                            <li>
                                <b>niet gestart</b> <br>
                                Het potje wordt aangegeven met een blauwe balk als het potje nog niet is gestart.
                            </li>
                            <li>
                                <b>wordt gespeeld</b> <br>
                                Zodra de eerste slag is geregistreerd, maar nog niet alle rondes volledig zijn gespeeld, bevindt het potje zich
                                in de status 'wordt gespeeld'. Het potje wordt dan aangegeven met een blauwe balk.
                            </li>
                            <li>
                                <b>uitgespeeld</b> <br>
                                Zodra de alle rondes van het potjes zijn gespeeld is het potje afgelopen. Het potje wordt dan aangegeven met een rode balk.
                            </li>
                        </ul>
                    </p>

                    <h5>Aanmelden/afmelden bij een potje</h5>
                    <p>
                       Een speler kan zich aanmelden bij een potje door op 1 van de speelposities te klikken. 
                       Als een speelpositie nog niet is bezet dan wordt dit aangegeven door '--geen speler--'. 
                       Als een speler op een spelerspositie klikt die al bezet is door een andere speler, dan wordt de andere speler
                       verwijderd en de nieuwe speler toegevoegd aan het potje. Een speler kan maar 1 keer binnen een potje zijn aangemeld. 
                       Als een speler is aangemeld wordt de knop 'Afmelden bij potje' actief, zodat een speler zich weer kan afmelden. 
                       Ook als een potje eenmaal begonnen is kan nog van speler worden gewisseld.
                    </p>

                    <h5>Mail versturen naar spelers</h5>
                    <p>
                        Zodra u bent aangemeld bij een potje heeft u de mogelijkheid een anonieme mail te sturen naar de andere 
                        spelers van dit potje. Anoniem houdt in dat alleen uw gebruikersnaam wordt getoond in de mail. Uw 
                        echte naam of e-mail adres worden niet verstuurd. Middels deze mail kunt u informatie uitwisselen 
                        over speeltijden en datum, de te gebuiken video meeting software. U kunt er ook voor kiezen uw echte mail 
                        adres of telefoonnummer te delen, zodat direct nader afgestemd kan worden
                    </p>
                    <p>
                        De andere spelers van het potje kunnen op dezelfde wijze een mail versturen.
                    </p>


                    <h5>A en B Teams</h5>
                    <p>
                        De speelposities binnen een potjes zijn genummerd van 1 t/m 4. Spelers 1 en 3 vormen het A-team, spelers 2 en 4 het B-team. 
                        In het spel zitten de spelers van hetzelfde team tegenover elkaar. 
                    </p>

                    <h5>Score en slagen van een potje bekijken</h5>
                    <p>
                        Zodra een potjes is gestart worden de speelde slagen, rondes en scores geregistreerd. Door vanuit 'Overzicht potjes' op de balk 
                        van een bepaald potje te klikken verschijnt de score zoals tot dusverre gespeeld van dat potje. Door vervolgens op de regel van een bepaalde 
                        ronde te klikken verschijnt onder de score het overzicht van de gespeelde slagen van de betreffede ronde en de puntentelling.
                    </p>
                    <p>
                        Zodra een potje is uitgespeeld wordt de eindscore zichtbaar in het 'Overzicht potjes'
                    </p>

                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>


                    <h3 id=ref_speel_potje>Het spelen van een potje</h3>
                    <p>
                        Een portje kan worden gespeeld zodra alle 4 de spelers zich bij het potje hebben geregistreerd.
                        In dat geval wordt een knop zichtbaar met 'Speel dit potje'. Door hierop te klikken komt u in het speelscherm
                    </p>

                    <h5>Het speelscherm</h5>
                    <p>
                       U als speler zit op de positie aan de onderkant van het scherm. Hier ziet u uw gebruikersnaam en tussen haakjes of u behoort tot
                       team-A of team-B en u ziet uw speelpositie. Tegenover u zit uw medespeler. Uw tegenstander zitten links en rechts van het scherm. 
                    </p>
                    <p>
                        Bij de speelpositie van de andere spelers staat een bolletje dat groen of rood gekleurd kan zijn. Dit bolletje geeft aan of de 
                        betreffende speler nog aanwezig (geconnecteerd is) met het spel (groen) of niet (rood). Zolang 1 van de bolletjes rood gekleurd is 
                        kunnen geen kaarten gespeeld worden.
                    </p>
                    <p>
                       In het midden van de het scherm ziet u de troef die geldt voor de betreffende ronde. Om de troef heen ziet u 4 kaartposities. 
                       Hier worden de kaarten van een slag zichtbaar die worden gespeeld. Wanneer een lege kaartpositie een lichtgroene kleur heeft 
                       dan geeft dit aan dat die betreffende speler aan de beurt is om te spelen. Alleen deze speler kan daadwerkelijk zijn kaart spelen. 
                       De kaartpositie is ook lichtgroen in het begin van de ronde om aan te geven welke speler de troef kan bepalen en daarna moet uitkomen.
                    </p>
                    <p>
                        Aan de linkerkant van het scherm wordt de roem getoond zoals die is gemeld binnen de ronde die wordt gespeeld.
                    </p>

                    <h5>Actie knoppen</h5>
                    <p>
                        Rechtsboven in het scherm bevindt zich een knop met 'Acties'. 
                        Door hierop de klikken kunnen een aantal acties worden gekozen:

                        <ul>
                            <li>
                                <b>Reset slag</b> <br>
                                Hiermee worden alle tot dusverre gespeelde kaarten van een slag teruggenomen, zodat de gehele slag 
                                opnieuw gespeeld moet worden. Dit kan alleen als de slag nog niet is 'genomen'. 
                                Reset slag kan nodig zijn indien een speler per ongeluk een verkeerde kaart heeft gespeeld en dit wilt corrigeren. 
                                Ook kan reset slag worden gebruikt indien de gespeeld kaart door het spel niet goed wordt getoond.
                            </li>
                            <li>
                                <b>Bekijk score</b> <br>
                                Hiermee is het mogelijk de stand tot dusverre in het potje te bekijken. 
                                In dit score overzicht is het niet mogelijk om de afzonderlijke slagen terug te zien.
                            </li>
                            <li>
                                <b>Vorige slag</b> <br>
                                Hiermee is het mogelijk om de gespeelde kaarten van de vorige slag in te zien. 
                            </li>
                            <li>
                                <b>Melden verzaken</b> <br>
                                Hiermee wordt de procedure opgestart om verzaken te melden.
                            </li>
                        </ul>
                    </p>

                    <h5>Troef kiezen</h5>
                    <p>
                        In het midden van het scherm is de troef zichtbaar. Voordat de eerste kaart van een ronde is gespeeld
                        kan de troef worden aangepast door de speler die als eerste moet uitkomen. Door één of meerdere keren op 
                        de troef te klikken kan de gewenste troef worden gekozen. Zodra de eerste kaart van de ronde is gespeeld kan 
                        de troef niet meer worden aangepast tot aan de volgende ronde.
                    </p>
                    <p>
                        De speler die binnen een ronde als eerste moet uitkomen kan de troef naar wens aanpassen.
                        Dit is tevens de speler die de ronde moet aannemen. 
                    </p>
                   

                    <h5 >Beurt</h5>
                    <p>
                        Na iedere gespeelde ronde moet een volgende speler aanmenen en als eerste uitkomen. Bij iedere slag wordt bepaald wie de slag heeft gewonnen.
                        De winnaar van de vorige slag moet uitkomen bij de nieuwe slag. Wie aan de beurt is om aan te nemen of een kaart te spelen wordt aangegeven
                        door een lichtgroene kleur van de lege kaartpositie in het midden van het scherm.
                        Alleen deze speler kan daadwerkelijk zijn kaart spelen. Als andere spelers hun kaart proberen te spelen dan zal deze een klein beetje bewegen om 
                        aan te geven dat het spel gaande is, maar dat deze speler nog niet daadwerkelijk mag spelen. Indien 1 van de indicatiebollejes rood is zullen 
                        de kaarten niet bewegen om aan te geven dat niet iedereen meer in het spel zit.
                    </p>
                    
                    <h5>Kaart spelen en reset slag</h5>
                    <p>
                        De speler die aan de beurt is kan een kaart spelen door op de betreffende kaart te klikken. 
                        De kaart zal zich dan vervolgens naar het midden van het scherm begeven. De beurt gaat daarna over naar de volgende speler.
                        Een gespeeld kaart kan niet worden teruggenomen. 
                    </p>

                    <h5>Roem melden en slag nemen</h5>
                    <p>
                        Zodra alle spelers hun kaart hebben gespeeld bepaalt het spel welke speler de slag heeft gewonnen. 
                        Bij deze speler verschijnen vervolgens twee koppen: een knop om roem te melden en een knop om de slag te pakken. 
                        Indien de slag roem heeft dan moet de speler deze eerst registreren en daarna pas de slag nemen. Zodra de slag genomen is 
                        kan de roem niet meer worden aangepast voor deze slag. Hooguit kan bij een foute roem registatie in de eventuele volgende slag 
                        een correctie plaatsvinden door een negatieve of positieve roem toe te kennen.
                    </p>

                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>

                    <h3 id=ref_melden_verzaken>Melden verzaken</h3>
                    <p>
                        Het spel checkt niet of een speler verzaakt. Spelers moeten zelf constateren of iemand verzaakt heeft of niet. 
                        Indien een speler denkt dat iemand verzaakt heeft dan kan hij dat melden. Er zal vervolgens een procedure worden gestart 
                        waarmee de spelers met elkaar kunnen evalueren of iemand daadwerkelijk verzaakt heeft. Het einde van de procedure resulteert erin dat 
                        de melding goed was of dat er een false melding was. In beide gevallen zullen alle punten , roem en 100 extra roem moeten worden 
                        toegekend aan het A-team of B-team.
                    </p>
                    <p>
                        Melden verzaken kan alleen als de ronde nog niet is afgerond, dat wil zeggen wanneer de laatste slag van de ronde nog niet is genomen.<br>
                        <b>Zorg er daarom voor dat verzaken wordt gemeld voordat de laatste slag wordt geregistreerd (slag wordt genomen).</b>
                    </p>

                    <h5>Opstarten procedure verzaken</h5>
                    <p>
                        Via de knop acties kan 'Melden verzaken' worden geactiveerd. Bij de speler (melder) die dit heeft aangeklikt verschijnt eerst een melding 
                        met de vraag of de melder daadwerkelijk het verzaken wilt melden of de procedure wilt stoppen. Indien de procedure wordt gestopt kan het 
                        spel gewoon verder gaan. Echter, indien de melder doorgaat dan zullen verdere stappen worden gezet en uiteindelijk alle punten aan een bepaald 
                        team moeten worden toegekend.
                    </p>

                    <h5>Doorgaan met melden verzaken</h5>
                    <p>
                        Als de melder heeft besloten door te gaan met het melden van verzaken verschijnt bij alle ander spelers een bericht op het scherm dat 
                        dat de melder een melding van verzaken doet. Bij de melder zelf verschijnt een nieuwe melding met uitleg hoe hij verder moet handelen. 
                        Alle spelers krijgen de mogelijkheid om de tot dusverre gespeelde slagen van de betreffende ronde in te zien, zodat met elkaar overlegd kan worden
                        over de juistheid van de melding. Zodra de spelers het met elkaar eens zijn moet de melder selecteren welke team alle punten, roem en 100 extra roem 
                        krijgt toegewezen. Zodra hij dat heeft gedaan zien de melder en de andere spelers welke keuze is gemaakt. Daarna kan
                        begonnen worden aan de volgende ronde.
                    </p>

                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>

                    <h3 id=ref_berichten>Berichten</h3>
                    <p>
                        Via de home pagina kunt u naar berichten gaan. 
                        Op deze pagina kunnen gebruikers van dit spel opmerkingen plaatsen of feedback geven, zoals:
                        <ul>
                            <li>het delen van eigen ervaringen met het spelen van dit spel</li>
                            <li>het melden van bugs</li>
                            <li>het geven van tips en suggesties voor verbeteringen</li>
                            <li>het stellen van vragen</li>
                        </ul>
                    </p>
                    <p>
                        Ook de beheerder kan een bericht plaatsen om updates te geven over de ontwikkeling van het spel.
                    </p>


                    <p> <a href="#inhoudsopgave">terug naar inhoudsopgave...</a></p>

                </b-card-text>
            </b-tab>

            <b-tab title="Speeltips">
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

                    <h5>Melden verzaken</h5>
                    <p>
                        Melden verzaken kan alleen als de ronde nog niet is afgerond, dat wil zeggen wanneer de laatste slag van de ronde nog niet is genomen.<br>
                        Zorg er daarom voor dat verzaken wordt gemeld voordat de laatste slag wordt geregistreerd (slag wordt genomen).
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
                    <p>Hieronder staat een lijst met verbeteringen of aanvullingen die 
                        in de toekomst verder ontwikkeld kunnen worden.
                    </p>
                    <ul>
                        <li>Mogelijkheid om gezamelijk een correctie uit te voeren op geregistreerde score.</li>
                        <li>Uitgebereidere rapportages over gemaakte scores en het vergelijken van games</li>
                        <li>De mogelijkheid bieden aan spelers om de eigen gegevens aan te passen</li>
                    </ul>
                </b-card-text>
            </b-tab>

            <b-tab title="Credits">
                <b-card-text>
                    
                    <p>
                        Dit is spel is ontwikkeld door Ole Karlsen.
                        De drijver om dit spel op te zetten was drieledig. <br> <br>
                        <ul>
                            <li>Een tijdsverdrijf vinden gedurende de Corona lockdown periode</li>
                            <li>Kennis vergroting van website technologien</li>
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
                        kleine verbetering worden doorgevoerd. Mocht je suggesties of feedback hebben, maak dan 
                        een bericht via de hoofdpagina <a href="#" v-on:click="gotoRemarks()">'Berichten'</a>
                        
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
      } else {

          //Check that screen is mobile. If so, set full screen
          var isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
          if (isMobile) {
            // document.body.requestFullscreen()
            document.documentElement.requestFullscreen()
          }
      }

  },//END activated
  methods: {
    gotoHome: function () {
        this.$router.push({ name: 'Home' })
    }, //END gotoHome

    gotoRemarks: function () {
      this.$router.push({ name: 'Remarks' })
    },  //END gotoRemarks

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
