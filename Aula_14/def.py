import os
os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_produto(nome, preco, quantidade):
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Quantidade: {quantidade}")

mostrar_produto("Teclado", 120.0, 5)
