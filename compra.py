import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input("Olá! Digite seu nome: ")
produto1 = input("Digite o nome do primeiro produto que você comprou: ")
preco1 = float(input(f"Digite o preço do produto {produto1}: "))
produto2 = input("Digite o nome do segundo produto que você comprou: ")
preco2 = float(input(f"Digite o preço do produto {produto2}: "))
produto3 = input("Digite o nome do terceiro produto que você comprou: ")
preco3 = float(input(f"Digite o preço do produto {produto3}: "))

total = preco1 + preco2 + preco3

print("=" * 30 + " Relatório de Compra " + "=" * 30)
print(f"Cliente, {nome}! Você comprou os seguintes produtos: {produto1}, {produto2} e {produto3}")
print(f"O total da sua compra foi de R$ {total:.2f}.")
print(f"Com 10% de desconto, o valor final da sua compra será de R$ {total * 0.9:.2f}.")
print("=" * 81)
