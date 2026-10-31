import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    return "Reprovado"

media = calcular_media(n1, n2, n3)

def mostrar_resultado(nome, media, situacao):
    print("\nResultado do Aluno:")
    print(f"Aluno: {nome}")
    print(f"Situação: {situacao}")
    print(f"Média: {media:.2f}")

mostrar_resultado(nome, media, definir_situacao(media))

