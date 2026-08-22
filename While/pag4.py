import os
os.system('cls' if os.name == 'nt' else 'clear')

contador = 1
total = 0

while contador <= 5:
    total = total + contador
    contador = contador + 1

print(f'O total é: {total}') 