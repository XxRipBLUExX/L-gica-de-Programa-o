import os
os.system('cls' if os.name == 'nt' else 'clear')

comprar = int(input("Digite quantos produtos deseja comprar: "))
total = 0.0

for i in range(comprar):
    produto = input(f"Digite o nome do {i + 1}º produto: ")
    quantidade = int(input(f"Digite a quantidade do {i + 1}º produto: "))
    valor = float(input(f"Digite o valor unitário do {i + 1}º produto: "))
    total += quantidade * valor

print(f"O total a pagar é: R${total:.2f}")