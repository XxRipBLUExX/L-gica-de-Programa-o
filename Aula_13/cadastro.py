import os
os.system('cls' if os.name == 'nt' else 'clear')

alunos = []

for i in range(3):
 aluno = {}
 aluno["nome"] = input("Nome: ")
 aluno["media"] = float(input("Média: "))
 alunos.append(aluno)

print("\nAlunos:")
for aluno in alunos:
 print(f"\nAluno: {aluno['nome']}")
 for chave, valor in aluno.items():
  print(f"{chave}: {valor}")
