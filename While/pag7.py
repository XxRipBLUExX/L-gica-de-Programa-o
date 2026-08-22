import os
os.system('cls' if os.name == 'nt' else 'clear')

opcao = 0

while opcao != 3:
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Cadastrar selecionado.")
    elif opcao == 2:
        print("Consultar selecionado.")
    elif opcao == 3:
        print("Sair selecionado.")
    else:
        print("Opção inválida!")