import os
os.system('cls' if os.name == 'nt' else 'clear')

print("-" * 30)
print("CADASTRO DE PRODUTOS:")
print("-" * 30)

quantidade_produtos = int(input("\nQuantidade de produtos: "))
produtos = []
estoque_produto = []
opcao = 0

#cadastro de produtos

for _ in range(quantidade_produtos):
    produto = {
        "codigo": input(f"Código do produto {_ + 1}: "),
        "nome": input(f"Nome do produto {_ + 1}: "),
        "preço": float(input(f"Preço do produto {_ + 1}: ")),
        "quantidade": int(input(f"Quantidade do produto {_ + 1}: ")),
    }
    produtos.append(produto)
    estoque_produto.append(produto)

#menu de opções

while opcao != 6:

    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    print("-" * 30)
    print("MENU DE OPÇÕES:")
    print("-" * 30)

    print("1 - Deseja cadastrar mais produtos?")
    print("2 - Deseja alterar a estoque de algum produto?")
    print("3 - Deseja alterar o preço de algum produto?")
    print("4 - Deseja alterar o código de algum produto?")
    print("5 - Relatório de produtos cadastrados?")
    print("6 - Finalizar o programa?")

    opcao = int(input("\nDigite a opção desejada: "))

    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == 1:
        print("Cadastrar mais produtos selecionado.")
        produto = {
            "codigo": input(f"Código do produto {len(produtos) + 1}: "),
            "nome": input(f"Nome do produto {len(produtos) + 1}: "),
            "preço": float(input(f"Preço do produto {len(produtos) + 1}: ")),
            "quantidade": int(input(f"Quantidade do produto {len(produtos) + 1}: ")),
        }
        produtos.append(produto)
        estoque_produto.append(produto)

    elif opcao == 2:
        print("Alterar estoque de algum produto selecionado.")
        codigo_produto = input(f"Código do produto: ")
        for produto in produtos:
            if produto["codigo"] == codigo_produto:
                nova_quantidade = int(input(f"Nova quantidade do produto {produto['nome']}: "))
                produto["quantidade"] = nova_quantidade
                break
        else:
            print("Produto não encontrado.")

    elif opcao == 3:
        print("Alterar o preço de algum produto selecionado.")
        codigo_produto = input(f"Código do produto: ")
        for produto in produtos:
            if produto["codigo"] == codigo_produto:
                novo_preco = float(input(f"Novo preço do produto {produto['nome']}: "))
                produto["preço"] = novo_preco
                break
        else:
            print("Produto não encontrado.")

    elif opcao == 4:
        print("Alterar o código de algum produto selecionado.")
        codigo_produto = input(f"Código do produto: ")
        for produto in produtos:
            if produto["codigo"] == codigo_produto:
                novo_codigo = input(f"Novo código do produto {produto['nome']}: ")
                produto["codigo"] = novo_codigo
                break
        else:
            print("Produto não encontrado.")

    elif opcao == 5:
        print("Relatório de produtos cadastrados selecionado.")
        print("-" * 30)
        print("RELÁTORIO DE PRODUTOS:")
        print("-" * 30)
        
        for produto in produtos:
            print(f"Produto: {produto['nome']}")
            print(f"Código: {produto['codigo']}")
            print(f"Preço: {produto['preço']}")
            print(f"Quantidade: {produto['quantidade']}")
            print("\n")

        print("Deseja encerrar o programa? (S/N)")
        encerrar = input().strip().upper()
        if encerrar == "S":
            print("\nPrograma encerrado, até a próxima.")
            break

    elif opcao == 6:
        print("Finalizar o programa selecionado.")
        print("Programa encerrado, até a próxima.")

    else:
        print("Opção inválida!")