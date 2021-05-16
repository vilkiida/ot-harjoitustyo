# Testausdokumentti

## Testaus:
Luokille löytyy niitä testaavat luokat src hakemiston tests hakemiston sisällä olevista *_test.py* päätteisistä moduuleista. Esimerkiksi luokkaa Cell testaa luokka TestCell. Testit suoritetaan **poetry run invoke test** komennolla.

## Testauskattavuus:
Koska käyttöliittymään liittyvää koodia ei ole eriytetty pois testauskattavuusraportista on testauskattavuus prosentti 54%

![Coverage-report](./kuvat/coverage-report.png)

## Sovellukseen jääneet laatuongelmat:
Käyttöliittymään liittyvää koodia ei ole tarpeeksi hyvin erityitetty koodista erilleen, joten sitä ei ole myöskään jätetty huomioimatta testauskattavuusraportissa. Käyttöliittymään liittyvään koodin ei ole tehty testejä (niinkuin ei tarkoituskaan) ja koska se on muun koodin kanssa sekaisin, se laskee testauskattavuus prosenttia.
