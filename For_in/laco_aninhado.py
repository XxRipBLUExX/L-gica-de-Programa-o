import os
os.system('cls' if os.name == 'nt' else 'clear')

quantidade_alunos = int(input("Quantos alunos deseja registrar? "))
contador = 0

for contador in range(quantidade_alunos):
    nota = float(input("Digite a nota: "))
while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Digite novamente: "))
