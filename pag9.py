import os
os.system('cls' if os.name == 'nt' else 'clear')

usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin":
    if senha == "1234":
        print("Acesso permitido.")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")