import os
os.system('cls' if os.name == 'nt' else 'clear')

opcao = 0

while opcao != 4:

    print("1 - Somar Dois números")
    print("2 - Verificar se o número é par ou ímpar")
    print("3 - Mostrar uma mensagem de boas-vindas")
    print("4 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao == 1:
        print("Somar Dois números selecionado.")
        print ("Digite dois números para somar:")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} é: {soma}")

    elif opcao == 2:
        print("Verificar se o número é par ou ímpar selecionado.")
        num = float(input("Digite um número: "))
        if num % 2 == 0:
            print(f"{num} é par.")
        else:
            print(f"{num} é ímpar.")

    elif opcao == 3:
        print("Mostrar uma mensagem de boas-vindas selecionado.")
        print("Bem-vindo ao SENAC!")

    elif opcao == 4:
        print("Sair selecionado.")
        print("Programa encerrado.")

    else:
        print("Opção inválida!")