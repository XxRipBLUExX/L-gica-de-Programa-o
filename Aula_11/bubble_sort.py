import os
os.system('cls' if os.name == 'nt' else 'clear')

numeros = [5, 3, 8, 2, 1, 4, 7, 6]
print(f"Lista original: {numeros}")

for i in range(len(numeros)):
 for j in range(len(numeros) - 1):
    if numeros[j] > numeros[j + 1]:
        numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print(f"Lista ordenada: {numeros}")