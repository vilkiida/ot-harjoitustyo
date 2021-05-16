# Käyttöohje:
## Ohjelman käynnistäminen ja muut toiminnot
Kun tarvittavat riippuvuudet on asennettu "poetry install" -komennolla:

- Ennen ensimmäistä pelin käynnistystä alustetaan tietokanta komennolla **poetry run invoke initialize** (Tämä komento tyhjentää highscoretietokannan ja alustaa sen uudestaan, joten komennon voi halutessaan tehdä myös myöhemminkin esim. tyhjentääkseen kaikki highscore tiedot.)
- Peli käynnistetään komennolla **poetry run invoke start**.
- Pelin testit suoritetaan komennolla **poetry run invoke test**.
- Pelin pylint arvio suoritetaan komennolla **poetry run invoke lint**.
- Pelistä laaditaan coverage raportti komennolla **poetry run invoke coverage-report**.
  -  Coverage raportti löytyy edellisen komennon jälkeen **htmlcov** kansion **index.html** tiedoston avaamalla selaimessa.

## SOVELLUKSEN KÄYTTÄMINEN:
### Päävalikko:
Sovellus aukeaa käynnistyttyään päävalikkoon:

Päävalikon painikkeet voi valita painamalla niitä hiiren vasemmalla painikkeella.
- **PLAY** painike ohjaa sinut pelivalikkoon.
- **HIGHSCORES** painike ohjaa sinut highscores-valikkoon.
- **HELP** painike ohjaa sinut peliohje sivulle.

### Pelivalikko:
Pelivalikossa voi valita haluamansa vaikeustason.

Pelivalikon painikkeet voi valita painamalla niitä hiiren vasemmalla painikkeella.
- **EASY** painike käynnistää helppotasoisen miinaharavapelin.
- **MEDIUMHARD** painike käynnistää keskivaikeatasoisen miinaharavapelin.
- **EXPERT** painike käynnistää erittäin vaikeatasoisen miinaharavapelin.
- **BACK** painike ohjaa sinut takaisin päävalikkoon.

### Highscores-valikko:
Highscores -valikossa voi valita minkä tason top5 - highscore-listan haluaa nähdä.

Highscorevalikon painikkeet voi valita painamalla niitä hiiren vasemmalla painikkeella.
- **EASY** painike avaa helppotasoisen miinaharavapelin top5 - highscore-listan.
- **MEDIUMHARD** painike avaa keskivaikeatasoisen miinaharavapelin top5 - highscore-listan.
- **EXPERT** painike avaa vaikeatasoisen miinaharavapelin top5 - highscore-listan.
- **BACK** painike ohjaa sinut takaisin päävalikkoon.

### Highscore-sivut:
Highscore-sivulla pystyy näkemään valitun tason top5 - highscore-listan.

- Listaan on merkittu sijoittain 1-5 parhaat tulokset sekä päiväys+kellonaika, jolloin tulos on tehty.
- Jos Listassa ei ole kyseiselle sijalle olevaa tulosta, lukee sijan kohdalla "NO SCORE".
- **ERACE SCORES** painiketta painamalla hiiren vasemmalla painikkeella tyhjennetään kyseisen vaikeustason highscore lista.
- **BACK** painiketta painamalla hiiren vasemalla painikkeella pääsee takaisin highscores-valikkoon.

### How to play-sivu / Ohje-sivu:
Ohje sivulla voi lukea lyhyen englanninkielisen peliohjeen. 

Takaisin päävalikkoon pääsee klikkaamalla **BACK** painiketta.

### Peli
- Pelissä ruutuja avataan vasemmalla hiiren painikkeella.
- Merkkaukset tehdään hiiren oikeaa painiketta käyttäen. Avaamaton ruutu muuttuu oikealla klikattaessa liputetuksi, liputettu ruutu kysymysmerkiksi ja kysymysmerkillä merkattu takaisin merkkaamattomaksi aavaamattomaksi ruuduksi.
- Lipulla tai kysymysmerkillä merkittyä ruutua, ei voi avata vasemmalla hiiren klikkauksella. Merkinnät tulee poistaa ennen kuin tämä on mahdollista.
- Lipulla merkityt eli ns. "löydetyt miinat" näkyvät peliruudun alalaidassa olevassa laskurissa, jossa näkyy löydettyjen miinojen osuus pelikentällä yhteensä olevien miinojen määrästä. Viimeiseksi avaamatta jäänyt miina ruutu lasketaan myös löydetyksi ja tällöin peli voitetaan.
- Avattu ruutu on joko tyhjä eli sen ympärillä ei ole miinoja tai siinä on lukuarvo, joka kertoo ruutua ympäröivien miinojen määrän. 
- Peli voitetaan, kun kaikki miinattomat ruudut ovat avattu.
- Peli hävitään, jos avataan ruutu, jossa on miina.
- Kun peli päättyy, ruudulla näkyy peliin mennyt aika (lasketaan esimmäisestä siirrosta lähtien).
- Pääset takaisin pelivalikkoon pelin päätyttyä klikkaamalla mihin tahansa ruudulla.
- Peli ruudun alalaidassa on myös **back** näppäin, jota klikkaamalla nykyinen peli loppuu ja pääsee takaisin pelivalikkoon.
