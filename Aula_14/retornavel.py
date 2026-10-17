import os
os.system('cls' if os.name == 'nt' else 'clear')

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
resultado = calcular_media(8, 6)
print(resultado)

if resultado >= 7:
    print("Aprovado")
else:
    print("Reprovado")