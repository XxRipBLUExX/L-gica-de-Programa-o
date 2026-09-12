import os
os.system('cls' if os.name == 'nt' else 'clear')

notas = [8, 6, 9, 7]

maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota
print(f"Maior nota: {maior}")

print(f"Menor nota: {menor}")