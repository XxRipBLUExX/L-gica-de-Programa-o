import os
os.system('cls' if os.name == 'nt' else 'clear')

numeros = [10, 25, 3, 18, 40]
procurado = int(input("Digite o número que deseja procurar: "))
for i in range(len(numeros)):
    if numeros[i] == procurado:
        print(f"Encontrado na posição {i}")
    else:   
        print("Número não encontrado")
    break