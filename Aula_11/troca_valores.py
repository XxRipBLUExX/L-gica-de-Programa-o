import os
os.system('cls' if os.name == 'nt' else 'clear')

numeros = [5, 3]
numeros[0], numeros[1] = numeros[1], numeros[0]
print(numeros)