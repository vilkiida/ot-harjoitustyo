import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
        self.maksukortti=Maksukortti(1000)

    #kassapääte luotu oikein:
    def test_luodun_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    def test_luodun_kassapaatteen_myydyt_edulliset_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    def test_luodun_kassapaatteen_myydyt_maukkaat_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #Käteisosto toimii edullisten lounaiden osalta:
    def test_vaihtoraha_oikein_kun_edullisen_lounaan_kateisosto_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250),10)
    def test_kassan_rahamaara_kasvaa_oikein_kun_ostetaan_kateisella_edullinen_lounas(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    def test_myytyjen_edullisten_lounaiden_maara_oikein_kun_kateisosto_onnistuu(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset,1)
    def test_kassan_rahamaara_oikein_kun_edullisen_lounaan_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    def test_vaihtorahan_maara_oikein_kun_edullisen_lounaan_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(150),150)
    def test_myytyjen_edullisten_lounaiden_maara_oikein_kun_kateisosto_ei_mene_lapi(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    #Käteisosto toimii maksullisten lounaiden osalta:
    def test_vaihtoraha_oikein_kun_maukkaan_lounaan_kateisosto_onnistuu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(420),20)
    def test_kassan_rahamaara_kasvaa_oikein_kun_ostetaan_kateisella_maukas_lounas(self):
        self.kassapaate.syo_maukkaasti_kateisella(420)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    def test_myytyjen_maukkaiden_lounaiden_maara_oikein_kun_kateisosto_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kateisella(420)
        self.assertEqual(self.kassapaate.maukkaat,1)
    def test_kassan_rahamaara_oikein_kun_maukkaan_lounaan_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    def test_vaihtorahan_maara_oikein_kun_maukkaan_lounaan_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(350),350)
    def test_myytyjen_maukkaiden_lounaiden_maara_oikein_kun_kateisosto_ei_mene_lapi(self):
        self.kassapaate.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    #Korttiostot edullisten lounaiden osalta:
    def test_kortilta_veloitetaan_oikein_kun_edullisen_lounaan_korttiosto_onnistuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo,760)
    def test_palauttaa_True_kun_ostetaan_edullinen_lounas_kortilla_onnistuneesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
    def test_myytyjen_edullisten_lounaiden_maara_oikein_kun_korttiosto_onnistuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,1)
    def test_kortilta_ei_veloiteta_jos_edullisen_lounaan_korttimaksu_ei_onnistu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo,200)
    def test_myytyjen_edullisten_lounaiden_maara_ei_muutu_kun_korttiosto_epaonnistuu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    def test_palauttaa_False_kun_ostetaan_edullinen_lounas_kortilla_epaonnistuneesti(self):
        self.maksukortti.ota_rahaa(800)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
    def test_kassassa_oleva_rahamaara_ei_muutu_kun_kortilla_ostetaan_edullinen_lounas(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    
    #Korttiostot maukkaan lounaan osalta:
    def test_kortilta_veloitetaan_oikein_kun_maukkaan_lounaan_korttiosto_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo,600)
    def test_palauttaa_True_kun_ostetaan_maukas_lounas_kortilla_onnistuneesti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True)
    def test_myytyjen_maukkaiden_lounaiden_maara_oikein_kun_korttiosto_onnistuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,1)
    def test_kortilta_ei_veloiteta_jos_maukkaan_lounaan_korttimaksu_ei_onnistu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo,200)
    def test_myytyjen_maukkaiden_lounaiden_maara_ei_muutu_kun_korttiosto_epaonnistuu(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    def test_palauttaa_False_kun_ostetaan_maukas_lounas_kortilla_epaonnistuneesti(self):
        self.maksukortti.ota_rahaa(800)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
    def test_kassassa_oleva_rahamaara_ei_muutu_kun_kortilla_ostetaan_maukas_lounas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    
    #Rahan lataus:
    def test_kortin_saldo_muuttuu_oikein_kun_ladataan_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
        self.assertEqual(self.maksukortti.saldo,1500)
    def test_kassan_rahamaara_kasvaa_oikein_kun_ladataan_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)