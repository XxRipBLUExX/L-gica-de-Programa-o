import os
os.system('cls' if os.name == 'nt' else 'clear')

nomes = []
notas = []
media = []
situacao = []
quantidade = int(input("Quantidade de alunos: "))
quantidade_notas = int(input("Digite quantas notas: "))

for contador in range(quantidade):
    name = input("Nome: ")
    nota_aluno = []
    for i in range(quantidade_notas):
        nota = float(input("Nota: "))
        nota_aluno.append(nota)

    nomes.append(name)
    notas.append(nota_aluno)

for indice in range(len(nomes)):
 total = sum(notas[indice])
 media_aluno = total / len(notas[indice])
 media.append(media_aluno)
 situacao.append("Aprovado" if media_aluno >= 7 else "Reprovado")

print("\nRelatório de alunos:")
for indice in range(len(nomes)):
 print(f"{nomes[indice]} - Notas: {notas[indice]} - Média do aluno: {media[indice]} - Situação: {situacao[indice]}")