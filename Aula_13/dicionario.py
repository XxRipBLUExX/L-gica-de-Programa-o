import os
os.system('cls' if os.name == 'nt' else 'clear')

quantidade_alunos = int(input("Quantidade de alunos: "))
alunos = []

for _ in range(quantidade_alunos):
    aluno = {
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "matricula": input("Matrícula: "),
        "media": float(input("Média: ")),
        "ativo": bool(input("Ativo (True/False): "))
    }
    alunos.append(aluno)

print("\nAlunos:")
for aluno in alunos:
    print("\nAluno:")
    for chave, valor in aluno.items():
        print(f"{chave}: {valor}")