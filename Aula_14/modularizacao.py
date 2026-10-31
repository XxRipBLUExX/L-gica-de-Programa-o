import os
os.system('cls' if os.name == 'nt' else 'clear')

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def mostrar_menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = int(input("Opção: "))

        if opcao == 0:
            break

        a = float(input("A: "))
        b = float(input("B: "))

        if opcao == 1:
            print(somar(a, b))
        elif opcao == 2:
            print(subtrair(a, b))
        else:
            print("Opção inválida")


main()