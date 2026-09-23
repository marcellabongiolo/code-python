"""
Módulo: CS50 Problem Set - Validador de Cartão de Crédito (Algoritmo de Luhn)
Autor: Marcella Bongiolo
Descrição: Implementação em Python do famoso desafio do CS50 para validar
           números de cartões de crédito usando o Algoritmo de Luhn.
"""

def validar_cartao(numero_str: str) -> str:
    """Valida um número de cartão de crédito usando o Algoritmo de Luhn."""
    # Remove espaços ou hifens se houver
    cartao = "".join(filter(str.isdigit, numero_str))
    
    if not cartao:
        return "Inválido"

    soma = 0
    tamanho = len(cartao)
    alternar = False

    # Percorre o cartão de trás para frente (Algoritmo de Luhn)
    for i in range(tamanho - 1, -1, -1):
        digito = int(cartao[i])
        
        if alternar:
            digito *= 2
            if digito > 9:
                digito -= 9
                
        soma += digito
        alternar = not alternar

    # Se a soma for divisível por 10, o cartão é válido matematicamente
    if soma % 10 == 0:
        # Identifica a bandeira com base no prefixo e tamanho
        if cartao.startswith(("34", "37")) and tamanho == 15:
            return "AMEX"
        elif 51 <= int(cartao[:2]) <= 55 and tamanho == 16:
            return "MASTERCARD"
        elif cartao.startswith("4") and (tamanho == 13 or tamanho == 16):
            return "VISA"
        else:
            return "Válido (Bandeira desconhecida)"
    
    return "INVÁLIDO"

def main():
    print("=" * 50)
    print(" 🎓 HARVARD CS50: VALIDADOR DE CARTÃO (LUHN) 💳")
    print("=" * 50)
    
    entrada = input("Digite o número do cartão para testar: ")
    resultado = validar_cartao(entrada)
    
    print(f"Resultado da validação: {resultado}")
    print("=" * 50)

if __name__ == "__main__":
    main()
