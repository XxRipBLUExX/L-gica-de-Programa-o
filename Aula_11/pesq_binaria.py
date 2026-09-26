import os
os.system('cls' if os.name == 'nt' else 'clear')

numeros = [3, 7, 10, 15, 18, 22, 30]
procurado = int(input("Valor procurado: "))
inicio = 0
fim = len(numeros) - 1
encontrado = False
while inicio <= fim:
    meio = (inicio + fim) // 2

    if numeros[meio] == procurado:
        encontrado = True
        print(f"Encontrado na posição {meio}")
    else:
        print("Número não encontrado")
        elif procurado < numeros[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    break