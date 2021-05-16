# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on miinaharava-peli. Pelin ideana on siis avata tyhjiä
ruutuja ja merkata miinoja lipulla, niin kauan kunnes kaikki ja tyhjät ruudut
on avattu, jolloin peli päättyy voittoon. Peli hävitään jos pelaaja avaa
ruudun jossa on miina.

## Suunnitellut toiminnallisuudet

### Lyhyesti:
- Peliä pystyy pelaamaan eri vaikeustasoilla, joita ovat
seuraavat:
  - Helppo
  - Keskivaikea
  - Vaikea
- Jokaisesta pelisuorituksesta mitataan siihen kulunut aika
- Suoritusaika näytetään ruudulla pelaajalle pelin päättymisen jälkeen (oli kyseessä voitto tai häviö)
- Pelisuorituksista on tarkoitus muodostaa aina tiettyä vaikeustasoa kohden
oma Top 5 "High Score" -lista, johon merkitään päiväys ja kellonaika jolloin peli pelattiin sekä pelin suoritusaika
- Pelin suoritus aika lisätään highscores - tietokantaan jos peli on voitettu.
- Pelaaja voi tarkastella high score taulukkoja eri vaikeustasoille

### Vähän tarkemmin (checklist toiminnallisuuksista):

#### Toiminnallisuudet ennen varsinaisen pelin alkua (pelivalikko):
- [x] sovelluksessa on pelivalikko
- [x] pelaaja voi valita haluamansa vaikeustason ja käynnistää varsinaisen pelin
- [x] pelaaja voi tarkastella highscore -listaa eri vaikeustasoilla
- [x] pelaaja voi lukea pelin ohjeen

#### Toiminnallisuudet varsinaisen pelin aikana:
- [x] suorituksen kestosta mitataan aikaa
- [x] pelaaja voi klikata haluamaansa ruutua hiiren vasemalla näppäimellä
avatakseensa kyseisen ruudun
  - [x] jos kyseisessä ruudussa oli miina peli päättyy
  - [x] jos kyseinen ruutu oli tyhjä aukeaa sen ympäriltä myös muut tyhjät
ruudut ja osaan näistä ruuduista, ilmestyy numerot, jotka kertovat montako
miinaa kyseisen ruudun ympärillä on. Jos ruudussa ei ole numeroa, sen ympärillä ei ole miinaa.
- [x] pelaaja voi klikata hiiren oikealla näppäillä ruutua, jonka se haluaa merkitä
lipulla
- [x] jos pelaaja klikkaa oikealla näppäimellä ruutua, joka on jo merkitty lipulla
merkintä muuttuu kysymysmerkiksi, joka on merkitä mitä pelaaja voi itse käyttää
hyödyksi epäillessään kyseisessä ruudussa olevan miina.
- [x] jos pelaaja klikkaa oikealla näppäimella ruutua, joka on merkitty
kysymysmerkillä, merkintä häviää.
- [x] ruudun alalaidassa on laskuri, joka laskee montako piilossa olevista miinoista on ns. "löydetty" eli tarkoittaa siis merkittyjen miinojen määrää. Myös viimeiseksi avaamattomaksi ruuduksi jäänyt miina lasketaan löydetyksi.
- [x] ruudun alalaidassa on takaisin näppäin, jolla peli loppuu ja päädytään takaisin pelivalikkoon.

#### Toiminnallisuudet pelisuorituksen jälkeen:
- [x] pelaaja näkee ilmoituksen voittiko vai hävisikö pelin
- [x] pelaaja näkee suoritusaikansa
- [x] pelaaja voi pelin jälkeen palata ns. "pelivalikkoon" klikkaamalla ruutua.


## Jatkokehitysideoita
- mukautettu vaikeustaso, jossa
saa siis itse valita ruudukon koon ja miinojen määrä
