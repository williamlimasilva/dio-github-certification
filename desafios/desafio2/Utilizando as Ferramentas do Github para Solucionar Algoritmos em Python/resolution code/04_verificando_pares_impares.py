"""
Desafio 4 - Verificando Números Pares e Ímpares

Descrição:
Receber um número inteiro e verificar se ele é par ou ímpar.
"""

def verificar_par_impar():
    # Solicitando o número ao usuário
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
    
    # Verificando se é par ou ímpar usando o operador de módulo (%)
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

if __name__ == "__main__":
    verificar_par_impar()
