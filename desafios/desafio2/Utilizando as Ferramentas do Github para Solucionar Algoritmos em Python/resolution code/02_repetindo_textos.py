"""
Desafio 2 - Repetindo Textos

Descrição:
Solicitar uma string e um número inteiro como entrada. 
Depois retornar a string repetida o número de vezes informado.
"""

def repetir_texto():
    # Solicitando os dados ao usuário
    texto = input("Digite um texto: ")
    
    # Tratando possíveis erros na entrada do número
    try:
        repeticoes = int(input("Digite quantas vezes o texto deve ser repetido: "))
        if repeticoes < 0:
            print("Por favor, digite um número não negativo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
    
    # Repetindo o texto
    resultado = texto * repeticoes
    
    # Exibindo o resultado
    print(f"Texto repetido: {resultado}")

if __name__ == "__main__":
    repetir_texto()
