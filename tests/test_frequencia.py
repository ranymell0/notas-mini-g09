import unittest
from notas.frequencia import frequencia_ok

class TestFrequencia(unittest.TestCase):
    def test_exatamente_75_por_cento(self):
        self.assertTrue(frequencia_ok(24, 32))
    def test_abaixo_de_75(self):
        self.assertFalse(frequencia_ok(23, 32))
    def test_presenca_total(self):
        self.assertTrue(frequencia_ok(32, 32))
    def test_zero_presencas(self):
        self.assertFalse(frequencia_ok(0, 32))
    def test_sem_aulas_da_erro(self):
        with self.assertRaises(ValueError):
            frequencia_ok(5, 0)
