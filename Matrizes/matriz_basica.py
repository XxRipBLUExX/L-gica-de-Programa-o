import os
os.system('cls' if os.name == 'nt' else 'clear')

matriz = [
 [8, 7, 9, 2],
 [6, 8, 7, 5],
 [9, 9, 10, 3]
]
print(f"matriz: {matriz}")
print(f"Número de linhas: {len(matriz)}")
print(f"Número de colunas: {len(matriz[0])}")
print(f"Primeiro elemento: {matriz[0][0]}")