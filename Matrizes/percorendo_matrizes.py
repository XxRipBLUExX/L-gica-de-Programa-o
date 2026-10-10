import os
os.system('cls' if os.name == 'nt' else 'clear')

matriz = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
for linha in matriz:
    for valor in linha:
        print(valor)

print("\n")

for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()