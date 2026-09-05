import os
os.system('cls' if os.name == 'nt' else 'clear')

nomes = ["Ana", "Bruno", "Carla"]
for indice in range(len(nomes)):
 print(indice, nomes[indice])