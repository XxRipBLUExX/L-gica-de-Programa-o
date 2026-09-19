import os
os.system('cls' if os.name == 'nt' else 'clear')

produtos = ["computador", "notebook", "smartphone", "tablet"]
busca = input("Digite o nome do produto: ")
posicao = -1
indice = 0

while indice < len(produtos):
    if produtos[indice] == busca:
        posicao = indice
        break
    indice += 1

if posicao != -1:
    print(f"Produto encontrado no índice {posicao}")
else:
    print("Produto não encontrado.")