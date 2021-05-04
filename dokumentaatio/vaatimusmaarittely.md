# Vaatimusmäärittely

## Sovelluksen tarkoitus

Tarkoituksena on tehdä miinaharava-peli. Pelin ideana on siis avata tyhjiä
ruutuja ja merkata miinoja lipulla, niin kauan kunnes kaikki ja tyhjät ruudut
on avattu, jolloin peli päättyy voittoon. Peli hävitään jos pelaaja avaa
ruudun jossa on miina.

## Suunnitellut toiminnallisuudet

### Lyhyesti:
- Peliä on tarkoitus pystyä pelaamaan eri vaikeustasoilla, joita olisi
ainakin seuraavat:
  - Helppo
  - Normaali
  - Vaikea
- Jokaisesta pelisuorituksesta mitataan siihen kulunut aika
- Suoritusaika näytetään ruudulla pelaajalle pelin päättymisen jälkeen
- Pelisuorituksista on tarkoitus muodostaa aina tiettyä vaikeustasoa kohden
oma Top 5 "High Score" -lista, johon merkitään pelaajan nimimerkki, pelin
suoritusaika
- Pelaajalta kysytään myös nimimerkki pelisuorituksen päätyttyä, jos pelaajan
suoritusaika on tarpeeksi hyvä päästäkseen Top 5 listalle.
- Pelaaja voi tarkastella high score taulukkoja eri vaikeustasoille

### Vähän tarkemmin (checklist toiminnallisuuksista):

#### Toiminnallisuudet ennen varsinaisen pelin alkua (pelivalikko):
- [x] sovelluksessa on pelivalikko
- [x] pelaaja voi valita haluamansa vaikeustason ja käynnistää varsinaisen pelin
- [ ] pelaaja voi tarkastella highscore -listaa eri vaikeustasoilla
- [x] pelaaja voi lukea pelin ohjeen

#### Toiminnallisuudet varsinaisen pelin aikana:
- [x] suorituksen kestosta mitataan aikaa
- [x] pelaaja voi klikata haluamaansa ruutua hiiren vasemalla näppäimellä
avatakseensa kyseisen ruudun
  - [x] jos kyseisessä ruudussa oli miina peli päättyy
  - [x] jos kyseinen ruutu oli tyhjä aukeaa sen ympäriltä myös muut tyhjät
ruudut ja osaan näistä ruuduista, ilmestyy numerot, jotka kertovat montako
miinaa kyseisen ruudun ympärillä on. 
- [x] pelaaja voi klikata hiiren oikealla näppäillä ruutua, jonka se haluaa merkitä
lipulla
- [x] jos pelaaja klikkaa oikealla näppäimellä ruutua, joka on jo merkitty lipulla
merkintä muuttuu kysymysmerkiksi, joka on merkitä mitä pelaaja voi itse käyttää
hyödyksi epäillessään kyseisessä ruudussa olevan miina.
- [x] jos pelaaja klikkaa oikealla näppäimella ruutua, joka on merkitty
kysymysmerkillä, merkintä häviää.

#### Toiminnallisuudet pelisuorituksen jälkeen:
- [x] pelaaja näkee ilmoituksen voittiko vai hävisikö pelin
- [x] pelaaja näkee suoritusaikansa
- [ ] jos pelaaja oma tulos on tarpeeksi hyvä päästäkseen highscore -listalle,
kysytään pelaajalta sen haluama nimimerkki
- [x] pelaaja voi pelin jälkeen palata ns. "pelivalikkoon" klikkaamalla ruutua.

#### Lisää:
- [ ] sovelluksen pelivalikon koodin jäsentelyn parantaminen (vähemmän toisteista koodia pelivalikoissa)

## Jatkokehitysideoita
- [ ] mukautettu vaikeustaso, jossa
saa siis itse valita ruudukon koon ja miinojen määrä
