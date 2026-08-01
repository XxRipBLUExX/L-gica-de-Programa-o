import os
os.system('cls' if os.name == 'nt' else 'clear')

senha = input("Digite a senha: ")
if senha == "Senac1234":
    print("Acesso permitido! Seja bem-vindo(a)!")
else:
    print("Acesso negado!")