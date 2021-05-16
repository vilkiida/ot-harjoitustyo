# MIINAHARAVA-peli

Miinaharava-pelisovellus. Pelin ideana on siis avata tyhjiä ruutuja ja merkata miinoja lipulla, niin kauan kunnes kaikki ja tyhjät ruudut on avattu, jolloin peli päättyy voittoon. Peli hävitään jos pelaaja avaa ruudun jossa on miina.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/alustava_m%C3%A4%C3%A4rittelydokumentti/vaatimusmaarittely.md)


[Työaikakirjanpito](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)


[Kuvien lähteet](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/photosources.md)


[Arkkitehtuurikuvaus](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)


[Käytöohje](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)


[Testaus](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Miinaharava sovelluksen käyttöohjeet:

1. Ensin asenna riippuvuudet **poetry install** komennolla
2. Ennen pelin ensimmäistä käynnistämistä alustetaan SQL-tietokanta komennolla **poetry run invoke initialize**
3. Pelin saat käynnistettyä **poetry run invoke start** komennolla
4. Suorittaaksesi sovelluksen testit, käytä komentoa **poetry run invoke test**
5. Suorittaaksesi testikattavuusraportin, käytä komentoa **poetry run invoke coverage-report**
6. Suorittaaksesi pylint arvion, käytä komentoa **poetry run invoke lint**

### Ohjeita miinaharava pelin käyttöön:

Katso [Käyttöohje](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)


