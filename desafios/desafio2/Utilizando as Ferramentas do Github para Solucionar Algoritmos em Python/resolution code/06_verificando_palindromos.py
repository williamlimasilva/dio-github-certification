"""
Desafio 6 - Verificando Palíndromos

Descrição:
Testar se uma palavra é um palíndromo.
Um palíndromo é uma palavra, frase ou sequência que se lê da mesma forma 
de trás para frente (ignorando espaços, pontuação e capitalização).
"""

def verificar_palindromo():
    # Solicitando a palavra ao usuário
    palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    
    # Removendo espaços e convertendo para minúsculas para uma comparação mais precisa
    palavra_processada = ''.join(palavra.lower().split())
    
    # Invertendo a palavra
    palavra_invertida = palavra_processada[::-1]
    
    # Verificando se é um palíndromo
    if palavra_processada == palavra_invertida:
        print(f"'{palavra}' É um palíndromo!")
    else:
        print(f"'{palavra}' NÃO é um palíndromo!")
        print(f"Original (sem espaços): {palavra_processada}")
        print(f"Invertida: {palavra_invertida}")

if __name__ == "__main__":
    verificar_palindromo()
