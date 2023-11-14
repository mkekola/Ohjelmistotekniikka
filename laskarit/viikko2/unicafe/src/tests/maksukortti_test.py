import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)

    #kortin saldon tarkastus
    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
    
    #rahan lataaminen oikein
    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)
        self.assertEqual(self.kortti.saldo_euroina(), 35.0)

    #rahan ottaminen oikein
    def test_kortilta_voi_ottaa_rahaa(self):
        self.kortti.ota_rahaa(500)
        self.assertEqual(self.kortti.saldo_euroina(), 5.0)

    #saldo ei muutu jos rahaa ei ole tarpeeksi
    def test_kortilta_ei_voi_ottaa_liikaa_rahaa(self):
        self.kortti.ota_rahaa(1500)
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)


