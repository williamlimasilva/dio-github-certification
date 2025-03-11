"""
Desafio 3 - Operações Matemáticas Simples

Descrição:
Solicitar como entrada dois números e depois realizar operações simples entre eles.
"""

def realizar_operacoes():
    # Solicitando os números ao usuário
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        return
    
    # Realizando as operações básicas
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    
    # Tratando divisão por zero
    if num2 != 0:
        divisao = num1 / num2
        divisao_str = str(divisao)
    else:
        divisao_str = "Erro: divisão por zero"
    
    # Exibindo os resultados
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao_str}")

if __name__ == "__main__":
    realizar_operacoes()
