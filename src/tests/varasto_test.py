import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

        varasto2 = Varasto(10, alku_saldo=-5.0)
        self.assertAlmostEqual(varasto2.saldo, 0.0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

        varasto2 = Varasto(-5)
        self.assertAlmostEqual(varasto2.tilavuus, 0.0)

    def test_lisays(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

        self.varasto.lisaa_varastoon(9999)
        self.assertAlmostEqual(self.varasto.saldo, 10)


    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liikaa_ottaminen(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(15)
        self.assertAlmostEqual(otettu, 5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)
    
    def test_liian_vahan_ottaminen(self):
        self.varasto.lisaa_varastoon(3)
        a = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(a, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 3)
    
    def test_str(self):
        self.varasto.lisaa_varastoon(3)
        self.assertEqual("saldo = 3, vielä tilaa 7", str(self.varasto))