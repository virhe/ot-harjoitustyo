import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_kassapaate_alkuarvot(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_kassapaate_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
    
    def test_kateisosto_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)

    def test_kateisosto_edullinen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_kateisosto_lounaiden_maara_nousee(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_vaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_kateisosto_vaara_palautus(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_kateisosto_vaara_palautus_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateisosto_vaara_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_veloitus(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo_euroina(), 6)

    def test_korttiosto_edullinen_veloitus(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo_euroina(), 7.6)

    def test_korttiosto_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        


    def test_korttiosto_lounaiden_maara_nousee(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_vaara_rahamaara_ei_muuto(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kortti.saldo_euroina(), 1)

    def test_korttiosto_vaara_rahamaara_false(self):
        self.kortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)

    def test_korttiosto_edullinen_vaara_rahamaara_false(self):
        self.kortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)

    def test_korttiosto_vaara_rahamaara_maara_ei_muutu(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kassa_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_rahan_lataaminen_rahamaara(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001)
        self.assertEqual(self.kortti.saldo_euroina(), 11)
    
    def test_negatiivinen_rahan_lataaminen_rahamaara(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.kortti, -100), None)