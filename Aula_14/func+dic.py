import os
os.system('cls' if os.name == 'nt' else 'clear')

produto = {
 "codigo": 1,
 "nome": "Mouse",
 "preco": 80.0
}

def mostrar_produto(produto):
 print(f"Código: {produto['codigo']}")
 print(f"Nome: {produto['nome']}")
 print(f"Preço: R$ {produto['preco']:.2f}")

mostrar_produto(produto)