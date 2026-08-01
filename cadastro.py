import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input("Digite o nome do Produto: ")
categoria = (input("Digite a categoria do Produto: "))
preco = float(input("Digite o preço do Produto: "))
quantidade = (input("Digite a quantidade do Produto no estoque: "))

print("\n" + "=" * 30 + " Relatório de Cadastro de Produto " + "=" * 30)
print(f"Produto: {nome}")
print(f"Categoria: {categoria}")
print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade em estoque: {quantidade}")
print("=" * 30)