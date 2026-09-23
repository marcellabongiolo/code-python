import unittest

from cs50_credit import validar_cartao


class TestValidadorCartao(unittest.TestCase):
    def test_detecta_visa(self):
        self.assertEqual(validar_cartao("4111111111111111"), "VISA")

    def test_detecta_mastercard(self):
        self.assertEqual(validar_cartao("5555555555554444"), "MASTERCARD")

    def test_detecta_amex(self):
        self.assertEqual(validar_cartao("378282246310005"), "AMEX")

    def test_aceita_espacos_e_hifens(self):
        self.assertEqual(validar_cartao("4111 1111 1111 1111"), "VISA")
        self.assertEqual(validar_cartao("4111-1111-1111-1111"), "VISA")

    def test_rejeita_numero_invalido(self):
        self.assertEqual(validar_cartao("4111111111111112"), "INVÁLIDO")

    def test_rejeita_caracteres_nao_permitidos(self):
        self.assertEqual(validar_cartao("4111ABCD11111111"), "INVÁLIDO")

    def test_rejeita_entrada_vazia(self):
        self.assertEqual(validar_cartao(""), "INVÁLIDO")

    def test_retorna_bandeira_desconhecida_para_luhn_valido(self):
        self.assertEqual(
            validar_cartao("6011111111111117"),
            "Válido (Bandeira desconhecida)",
        )


if __name__ == "__main__":
    unittest.main()
