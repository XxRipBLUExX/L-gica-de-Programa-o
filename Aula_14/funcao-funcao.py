import os
os.system('cls' if os.name == 'nt' else 'clear')

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def situacao(media):
    if media >= 7:
        return "Aprovado"
    return "Reprovado"

media = calcular_media(8, 6)
print(situacao(media))