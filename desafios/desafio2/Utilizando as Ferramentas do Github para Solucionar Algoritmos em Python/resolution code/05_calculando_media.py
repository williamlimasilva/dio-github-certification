"""
Desafio 5 - Calculando Média de Notas

Descrição:
Calcular a média de três notas fornecidas na entrada do usuário.
"""

def calcular_media():
    try:
        # Solicitando as três notas ao usuário
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        # Calculando a média
        media = (nota1 + nota2 + nota3) / 3
        
        # Exibindo o resultado com duas casas decimais
        print(f"A média das notas é: {media:.2f}")
        
        # Opcional: Verificar se o aluno foi aprovado (média >= 7)
        if media >= 7:
            print("O aluno foi APROVADO!")
        else:
            print("O aluno foi REPROVADO!")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos para as notas.")

if __name__ == "__main__":
    calcular_media()
