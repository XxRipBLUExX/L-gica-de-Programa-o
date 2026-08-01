import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Bem-vindo ao jogo de adivinhação de números!")
numero = int(input("Digite um número entre 1 e 100: "))
numero2 = numero * 2
numero3 = numero2 + 100
numero4 = numero3 / 2
numero5 = numero4 - numero



print("Agora, multiplique esse número por 2")
print("Some 100 ao resultado")
print("Divida o resultado por 2")
print("Subtraia o número original do resultado final")

input("Está pronto para ver o resultado? Pressione Enter para continuar...")
print(f"O resultado final é: {numero5}")