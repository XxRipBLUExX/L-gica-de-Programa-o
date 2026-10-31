import os
os.system('cls' if os.name == 'nt' else 'clear')

def calcular_media_lista(notas):
    soma = 0

    for nota in notas:
        soma += nota
    return soma / len(notas)
                   
notas = [8, 7, 9]
media = calcular_media_lista(notas)
print(media)
