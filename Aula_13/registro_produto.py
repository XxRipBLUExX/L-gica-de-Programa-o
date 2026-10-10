import os
os.system('cls' if os.name == 'nt' else 'clear')

quantidade_produtos = int(input("Quantidade de produtos: "))
produtos = []

for _ in range(quantidade_produtos):
    produto = {
        "codigo": input("Código: "),
        "nome": input("Nome: "),
        "preço": float(input("Preço: ")),
        "quantidade": int(input("Quantidade: ")),
        "categoria": input("Categoria: "),
    }
    produtos.append(produto)

print("\nProdutos:")
for produto in produtos:
    print(f"\nProduto: {produto['nome']}")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")

quantidade_adicionados = sum(produto["quantidade"] for produto in produtos) + 10

print("\nProdutos:")
for produto in produtos:
    print(f"\nProduto: {produto['nome']}")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")