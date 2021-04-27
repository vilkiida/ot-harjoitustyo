# MIINAHARAVA-peli

Miinaharava-pelisovellus. Pelin ideana on siis avata tyhjiä ruutuja ja merkata miinoja lipulla, niin kauan kunnes kaikki ja tyhjät ruudut on avattu, jolloin peli päättyy voittoon. Peli hävitään jos pelaaja avaa ruudun jossa on miina.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/alustava_m%C3%A4%C3%A4rittelydokumentti/vaatimusmaarittely.md)


[Työaikakirjanpito](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)


[Kuvien lähteet](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/photosources.md)


[Arkkitehtuurikuvaus](https://github.com/vilkiida/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)


## Miinaharava sovelluksen käyttöohjeet:

1. Ensin asenna riippuvuudet "poetry install" komennolla
2. Pelin saat käynnistettyä "poetry run invoke start" komennolla
3. Jos haluat suorittaa sovelluksen testit, voit suorittaa ne komennolla "poetry run invoke test"

### Ohjeita miinaharava pelin käyttöön:
- Kun olet voittanut tai hävinnyt miinaharavapelin klikkaamalla mihin tahansa kohtaan ruutua, pääset takaisin pelivalikkoon (kohtaan jossa valitaan vaikeustaso).
- Pelivalikon highscores sivulla olevat easy, mediumhard ja expert näppäimien painaminen ei vielä tee muuta kuin printtaa tekstin "highscores for the level [klikattu vaikeustaso] coming soon...", sillä highscores osio on vielä kesken.


