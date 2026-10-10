import os
os.system('cls' if os.name == 'nt' else 'clear')

alunos = [
 {"nome": "Ana", "media": 8.0},
 {"nome": "Bruno", "media": 6.5},
 {"nome": "Carla", "media": 9.0}
]

print(alunos[0])
print(alunos[0]["nome"])