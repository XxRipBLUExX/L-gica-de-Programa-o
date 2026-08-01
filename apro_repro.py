import os
os.system('cls' if os.name == 'nt' else 'clear')

# Coleta das notas usando um laço de repetição
nome = input("Digite o nome do aluno: ")
notas = []
extensos = ["primeira", "segunda", "terceira", "quarta"]
frequencia = int(input("Digite a frequência do aluno (em %): "))

for i in range(4):
    nota = float(input(f"Digite a {extensos[i]} nota: "))
    notas.append(nota)

# Cálculo e exibição dos resultados
media = sum(notas) / len(notas)

print("\n" + "=" * 30 + " RELATÓRIO DO ALUNO " + "=" * 30)
print(f"Aluno(a): {nome}")
print(f"Notas obtidas: {notas}")
print(f"Frequência: {frequencia}%")
print(f"Média Final: {media:.2f}")  # O :.2f limita para 2 casas decimais

if media >= 7 and frequencia >= 75:
    print("Parabéns! Você foi aprovado(a).")
else:
    print("Infelizmente, você não atingiu os critérios para aprovação.")
print("=" * 80)