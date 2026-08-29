import os
os.system('cls' if os.name == 'nt' else 'clear')

notas = []

for i in range(3):
    while True:
        nota = int(input(f"Digite a nota do aluno no {i + 1}º trimestre: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("Nota inválida! Digite uma nota entre 0 e 10.")

media = sum(notas) / len(notas)

print(f"A média do aluno é: {media:.2f}")

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")