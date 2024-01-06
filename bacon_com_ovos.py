"""
1 - Receber um número inteiro
2 - Saber se o número é múltiplo de 3 e 5:
    Bacon com ovos
3 - Saber se o número é múltiplo somente de 3:
    Bacon
4 - Saber se o número é múltiplo somente de 5:
    Ovos
5 - Saber se o número não é múltiplo de 3 e 5:
    Passa fome
"""
import unittest
from test_bacon_com_ovos import bacon_com_ovos

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)  # Multiplos de 3 e 5
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                        bacon_com_ovos(entrada),
                        saida,
                        msg=f'"{entrada}" não retornou "{saida}"'
                    )
                
    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)  # Multiplos de 3 e 5
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                        bacon_com_ovos(entrada), 
                        saida,
                        msg=f'"{entrada}" não retornou "{saida}"'
                    )
                
    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)  # Multiplos de 3
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                        bacon_com_ovos(entrada), 
                        saida,
                        msg=f'"{entrada}" não retornou "{saida}"'
                    )
                
    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)  # Multiplos de 5
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                        bacon_com_ovos(entrada), 
                        saida,
                        msg=f'"{entrada}" não retornou "{saida}"'
                    )


unittest.main(verbosity=2)