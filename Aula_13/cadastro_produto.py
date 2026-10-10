import os
os.system('cls' if os.name == 'nt' else 'clear')

quantidade_produtos = int(input("Quantidade de produtos: "))
produtos = []

for _ in range(quantidade_produtos):
    produto = {
        "nome": input("Nome do Produtoe: "),
        "preço": float(input("Preço: ")),
        "quantidade": int(input("Quantidade: ")),
        "valor Total": 0,
    }
    produto["valor Total"] = produto["preço"] * produto["quantidade"]
    produtos.append(produto)

print("\nProdutos:")
for produto in produtos:
    print(f"\nProduto: {produto['nome']}")
    for chave, valor in produto.items():
        print(f"{chave}: {valor}")
    encontrado = True
if not encontrado:
    print("Produto não encontrado")
