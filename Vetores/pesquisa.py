import os
os.system('cls' if os.name == 'nt' else 'clear')

alunos = ["Ana", "Bruno", "Carla", "Diego"]
busca = input("Digite o nome: ")
encontrado = False

for aluno in alunos:
    if aluno == busca:
        encontrado = True
if encontrado:
    print("Aluno encontrado.")
else:
    print("Aluno não encontrado.")