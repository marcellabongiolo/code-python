"""Validador educacional de números de cartão usando o Algoritmo de Luhn.

O projeto é inspirado no exercício Credit do CS50. A validação é apenas
matemática e de formato; não consulta emissores, bancos ou redes de pagamento.
"""

import re


def _normalizar_numero(numero: str) -> str | None:
    """Aceita apenas dígitos, espaços e hífens como separadores."""
    valor = numero.strip()

    if not valor or not re.fullmatch(r"[0-9 -]+", valor):
        return None

    return valor.replace(" ", "").replace("-", "")


def validar_cartao(numero: str) -> str:
    """Valida um número pelo Algoritmo de Luhn e identifica a bandeira.

    Retorna AMEX, MASTERCARD, VISA ou uma mensagem genérica quando o número
    passa no Luhn, mas não corresponde às regras de bandeira implementadas.
    """
    cartao = _normalizar_numero(numero)

    if cartao is None:
        return "INVÁLIDO"

    tamanho = len(cartao)

    if tamanho < 2:
        return "INVÁLIDO"

    soma = 0
    dobrar = False

    for caractere in reversed(cartao):
        digito = int(caractere)

        if dobrar:
            digito *= 2
            if digito > 9:
                digito -= 9

        soma += digito
        dobrar = not dobrar

    if soma % 10 != 0:
        return "INVÁLIDO"

    if cartao.startswith(("34", "37")) and tamanho == 15:
        return "AMEX"

    if 51 <= int(cartao[:2]) <= 55 and tamanho == 16:
        return "MASTERCARD"

    if cartao.startswith("4") and tamanho in (13, 16):
        return "VISA"

    return "Válido (Bandeira desconhecida)"


def main() -> None:
    """Executa a interface de linha de comando do exercício."""
    print("=" * 50)
    print("CS50 — VALIDADOR DE CARTÃO (LUHN)")
    print("=" * 50)

    entrada = input("Digite o número do cartão para testar: ")
    resultado = validar_cartao(entrada)

    print(f"Resultado da validação: {resultado}")
    print("=" * 50)


if __name__ == "__main__":
    main()
