import os
os.system('cls' if os.name == 'nt' else 'clear')

alunos = []
quantidade = int(input("Digite a quantidade de alunos: "))

for i in range(quantidade):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
print("Alunos cadastrados:", alunos)