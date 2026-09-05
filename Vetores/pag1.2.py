import os
os.system('cls' if os.name == 'nt' else 'clear')

nomes = []
for contador in range(5):
 nome = input("Digite um nome: ")
 nomes.append(nome)
print(nomes)