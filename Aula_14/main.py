import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_cabecalho():
    print("-" * 30)
    print("CADASTRO DE PRODUTOS:")
    print("-" * 30)

def cadastrar_produto(produtos):
    numero = len(produtos) + 1
    produto = {
        "codigo": input(f"Código do produto {numero}: "),
        "nome": input(f"Nome do produto {numero}: "),
        "preço": float(input(f"Preço do produto {numero}: ")),
        "quantidade": int(input(f"Quantidade do produto {numero}: ")),
    }
    produtos.append(produto)

def cadastrar_produtos_iniciais(produtos):
    quantidade = int(input("\nQuantidade de produtos: "))
    for _ in range(quantidade):
        cadastrar_produto(produtos)

def mostrar_menu():
    print("-" * 30)
    print("MENU DE OPÇÕES:")
    print("-" * 30)
    print("1 - Cadastrar mais produtos")
    print("2 - Alterar o estoque de um produto")
    print("3 - Alterar o preço de um produto")
    print("4 - Alterar o código de um produto")
    print("5 - Relatório de produtos cadastrados")
    print("6 - Finalizar o programa")
    return int(input("\nDigite a opção desejada: "))

def buscar_produto_por_codigo(produtos):
    codigo = input("Código do produto: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    print("Produto não encontrado.")
    return None

def alterar_estoque(produtos):
    produto = buscar_produto_por_codigo(produtos)
    if produto:
        produto["quantidade"] = int(
            input(f"Nova quantidade do produto {produto['nome']}: ")
        )

def alterar_preco(produtos):
    produto = buscar_produto_por_codigo(produtos)
    if produto:
        produto["preço"] = float(
            input(f"Novo preço do produto {produto['nome']}: ")
        )

def alterar_codigo(produtos):
    produto = buscar_produto_por_codigo(produtos)
    if produto:
        produto["codigo"] = input(f"Novo código do produto {produto['nome']}: ")

def mostrar_relatorio(produtos):
    print("Relatório de produtos cadastrados:")
    print("-" * 30)

    for produto in produtos:
        print(f"Produto: {produto['nome']}")
        print(f"Código: {produto['codigo']}")
        print(f"Preço: {produto['preço']}")
        print(f"Quantidade: {produto['quantidade']}")
        print()

def executar_opcao(opcao, produtos):
    if opcao == 1:
        print("Cadastrar mais produtos selecionado.")
        cadastrar_produto(produtos)
    elif opcao == 2:
        print("Alterar estoque de algum produto selecionado.")
        alterar_estoque(produtos)
    elif opcao == 3:
        print("Alterar o preço de algum produto selecionado.")
        alterar_preco(produtos)
    elif opcao == 4:
        print("Alterar o código de algum produto selecionado.")
        alterar_codigo(produtos)
    elif opcao == 5:
        print("Relatório de produtos cadastrados selecionado.")
        mostrar_relatorio(produtos)
        encerrar = input("Deseja encerrar o programa? (S/N) ").strip().upper()
        if encerrar == "S":
            print("\nPrograma encerrado, até a próxima.")
            return False
    elif opcao == 6:
        print("Finalizar o programa selecionado.")
        print("Programa encerrado, até a próxima.")
        return False
    else:
        print("Opção inválida!")

    return True

def main():
    limpar_tela()
    mostrar_cabecalho()

    produtos = []
    cadastrar_produtos_iniciais(produtos)

    continuar = True
    while continuar:
        limpar_tela()
        opcao = mostrar_menu()
        limpar_tela()
        continuar = executar_opcao(opcao, produtos)

if __name__ == "__main__":
    main()
