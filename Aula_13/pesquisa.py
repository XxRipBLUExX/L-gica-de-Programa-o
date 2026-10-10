import os
os.system('cls' if os.name == 'nt' else 'clear')

quantidade_alunos = int(input("Quantidade de alunos: "))
alunos = []

for _ in range(quantidade_alunos):
    aluno = {
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "matricula": input("Matrícula: "),
    }
    alunos.append(aluno)

matricula_busca = input("Matrícula: ")
encontrado = False

for aluno in alunos:
    if aluno["matricula"] == matricula_busca:
        print("\nAluno:")
        for aluno in alunos:
            print(f"\nAluno: {aluno['nome']}")
        for chave, valor in aluno.items():
            print(f"{chave}: {valor}")
        encontrado = True
    break
if not encontrado:
    print("Aluno não encontrado")

