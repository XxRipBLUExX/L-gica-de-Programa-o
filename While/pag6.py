import os
os.system('cls' if os.name == 'nt' else 'clear')

senha = input('Digite a senha: ')

while senha != '1234':
    print('Senha incorreta!')
    senha = input('Digite a senha novamente: ')
print('Senha correta! Acesso permitido.')