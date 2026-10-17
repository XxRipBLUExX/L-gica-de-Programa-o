import os
os.system('cls' if os.name == 'nt' else 'clear')

numeros = []

def calculadora(numeros):
    soma = sum(numeros)
    subtracao = len(numeros) > 1 and numeros[0] - numeros[1] or numeros[0]
    multiplicacao = len(numeros) > 1 and numeros[0] * numeros[1] or numeros[0]
    divisao = len(numeros) > 1 and numeros[0] / numeros[1] or None
    return soma, subtracao, multiplicacao, divisao

while True:
    try:
        numero = float(input("Digite um número (ou 'sair' para encerrar): "))
        numeros.append(numero)
    except ValueError:
        break

soma, subtracao, multiplicacao, divisao = calculadora(numeros)
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")