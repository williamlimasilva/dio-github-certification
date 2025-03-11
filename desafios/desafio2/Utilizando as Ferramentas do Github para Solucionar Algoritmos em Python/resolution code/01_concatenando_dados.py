"""
Desafio 1 - Concatenando Dados

Descrição:
Receber dois dados diferentes do usuário e concatená-los em uma única string.
"""

def concatenar_dados():
    # Solicitando os dados ao usuário
    primeiro_dado = input("Digite o primeiro dado: ")
    segundo_dado = input("Digite o segundo dado: ")
    
    # Concatenando os dados
    resultado = primeiro_dado + segundo_dado
    
    # Exibindo o resultado
    print(f"Dados concatenados: {resultado}")

if __name__ == "__main__":
    concatenar_dados()
