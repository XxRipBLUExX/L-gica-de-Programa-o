import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Digite um número inteiro: "))

for calculadora in range(0, numero * 11, numero):
    print(f"Tabuada do {numero} X {calculadora // numero}: {calculadora}")