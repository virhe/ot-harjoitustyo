import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 12)

    def test_saldo_vahenee(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 8)
    
    def test_saldo_ei_negatiivinen(self):
        self.maksukortti.ota_rahaa(1200)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_ota_rahaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)

    def test_ota_rahaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)