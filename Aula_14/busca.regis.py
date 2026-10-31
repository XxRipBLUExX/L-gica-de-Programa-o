import os
os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_produto(produto):
    print(f"Código: {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")

produtos = [
    {"codigo": 1, "nome": "Mouse", "preco": 80.0},
    {"codigo": 2, "nome": "Teclado", "preco": 120.0},
    {"codigo": 3, "nome": "Monitor", "preco": 600.0}
]

def buscar_produto(produtos, codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None

resultado = buscar_produto(produtos, 2)
if resultado is not None:
    mostrar_produto(resultado)
else:
    print("Produto não encontrado")