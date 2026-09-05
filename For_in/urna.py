import os
os.system('cls' if os.name == 'nt' else 'clear')

total_votos = 6

for contador in range(total_votos):
    print(f"Voto {contador + 1} de {total_votos}")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Candidato C")
    print("4 - Candidato D")
    print("5 - Nulo")
    print("6 - Branco")

    voto = int(input("Digite o número do candidato que deseja votar: "))

    if voto == 1:
        print("Você votou no Candidato A.")
    elif voto == 2:
        print("Você votou no Candidato B.")
    elif voto == 3:
        print("Você votou no Candidato C.")
    elif voto == 4:
        print("Você votou no Candidato D.")
    elif voto == 5:
        print("Você votou Nulo.")
    elif voto == 6:
        print("Você votou em Branco.")
    else:
        print("Opção inválida. Voto não registrado.")