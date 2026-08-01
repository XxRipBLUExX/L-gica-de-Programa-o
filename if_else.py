import os
os.system('cls' if os.name == 'nt' else 'clear')

# Coleta das notas usando um laço de repetição
notas = []
extensos = ["primeira", "segunda"]

for i in range(2):
    nota = float(input(f"Digite a {extensos[i]} nota: "))
    notas.append(nota)

# Cálculo e exibição dos resultados
media = sum(notas) / len(notas)

print("\n" + "=" * 30)
print(f"Notas obtidas: {notas}")
print(f"Média Final: {media:.2f}")  # O :.2f limita para 2 casas decimais

if media >= 7:
    print("Parabéns! Você foi aprovado(a).")
else:
    print("Infelizmente, você não atingiu a média mínima para aprovação.")
print("=" * 30)