import os
os.system('cls' if os.name == 'nt' else 'clear')

alunos = ["Ana", "Bruno", "Carla", "Diego"]
busca = input("Digite o nome: ")
posicao = -1
for indice in range(len(alunos)):
    if alunos[indice] == busca:
        posicao = indice
if posicao != -1:
    print(f"Aluno encontrado no índice {posicao}")
else:
    print("Aluno não encontrado.")