import os
os.system('cls' if os.name == 'nt' else 'clear')

nomes = ["Kaka", "Ana", "Pedro", "Gustavo", "Heitor", "Felipe", "Dieimes"]
nomes.remove("Ana")
nomes.pop(4)

nome = input("Digite o nome do aluno: ")
if nome in nomes:
 print("Aluno encontrado.")
else:
 print("Aluno não encontrado.")

for indice in range(len(nomes)):
 print(indice, nomes[indice])
