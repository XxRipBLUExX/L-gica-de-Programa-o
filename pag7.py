import os
os.system('cls' if os.name == 'nt' else 'clear')

idade = 16
possui_autorizacao = True
nota = 6.5
frequencia = 80

print(idade >= 18)
print(idade < 18 and possui_autorizacao == True)
print(nota >= 7 and frequencia >= 75)
print(nota >= 7 or frequencia >= 75)
print(not possui_autorizacao)