import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Digite um número para ver a tabuada dele até o 100: "))
i = 1

while numero < 0:
    print("Número inválido! Digite um número positivo.")
    numero = int(input("Digite um número para ver a tabuada dele até o 100: "))

while i <= 100:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1

'''
Também pode ser utilizado:
for i in range(1, 101):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
'''