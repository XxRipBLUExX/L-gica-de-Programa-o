import os
os.system('cls' if os.name == 'nt' else 'clear')

matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f"Valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz:")
for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()