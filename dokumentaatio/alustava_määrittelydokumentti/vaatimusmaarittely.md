# Vaatimusmäärittely

## Sovelluksen tarkoitus

Tarkoituksena on tehdä miinaharava-peli. Pelin ideana on siis avata tyhjiä
ruutuja ja merkata miinoja lipulla, niin kauan kunnes kaikki ja tyhjät ruudut
on avattu, jolloin peli päättyy voittoon. Peli hävitään jos pelaaja avaa
ruudun jossa on miina.

## Suunnitellut toiminnallisuudet

### Yleisesti:
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

### Vähän tarkemmin:

#### Toimnnallisuudet ennen varsinaisen pelin alkua (pelivalikko):
- pelaaja voi valita haluamansa vaikeustason ja käynnistää varsinaisen pelin
- pelaaja voi tarkastella highscore -listaa eri vaikeustasoilla
- pelaaja voi lukea pelin ohjeen

#### Toiminnallisuudet varsinaisen pelin aikana:
- suorituksen kestosta mitataan aikaa
- pelaaja voi klikata haluamaansa ruutua hiiren vasemalla näppäimellä
avatakseensa kyseisen ruudun
  - jos kyseisessä ruudussa oli miina peli päättyy
  - jos kyseinen ruutu oli tyhjä aukeaa sen ympäriltä myös muut tyhjät
ruudut ja osaan näistä ruuduista, ilmestyy numerot, jotka kertovat montako
miinaa kyseisen ruudun ympärillä on. 
- pelaaja voi klikata hiiren oikealla näppäillä ruutua, jonka se haluaa merkitä
lipulla
- jos pelaaja klikkaa oikealla näppäimellä ruutua, joka on jo merkitty lipulla
merkintä muuttuu kysymysmerkiksi, joka on merkitä mitä pelaaja voi itse käyttää
hyödyksi epäillessään kyseisessä ruudussa olevan miina.
- jos pelaaja klikkaa oikealla näppäimella ruutua, joka on merkitty
kysymysmerkillä, merkitä häviää.

#### Toiminnallisuudet pelisuorituksen jälkeen:
- pelaaja näkee suoritusaikansa
- pelaajalle näytetään, kyseisen vaikeustason highscore -lista
- jos pelaaja oma tulos on tarpeeksi hyvä päästäkseen highscore -listalle,
kysytään pelaajalta sen haluama nimimerkki
- pelaaja voi joko pelata pelin uudestaan tai palata ns. "pelivalikkoon"

## Jatkokehitysideoita
- saattaa mennä jo perusversioonkin, mutta mukautettu vaikeustaso, jossa
saa siis itse valita ruudukon koon ja miinojen määrän.
