import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input ("Digite seu nome: ")

for letra in nome:
    print(letra)