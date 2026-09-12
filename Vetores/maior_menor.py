import os
os.system('cls' if os.name == 'nt' else 'clear')

alunos = []
quantidade = int(input("Digite a quantidade de alunos: "))

for i in range(quantidade):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {alunos[i]}: "))
    notas.append(nota)

maior = notas[0]
for nota in notas:
    if nota > maior:
        maior = nota

menor = notas[0]
for nota in notas:
    if nota < menor:
        menor = nota

media = sum(notas) / len(notas)

print("Alunos cadastrados:", alunos)
print(f"Menor nota do aluno {alunos[notas.index(menor)]}: {menor}")
print(f"Maior nota do aluno {alunos[notas.index(maior)]}: {maior}")
print("Notas:", notas)
print(f" Média das notas: {media:.2f}")