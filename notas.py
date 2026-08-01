import os
# Configurações Iniciais
curso = "Lógica de Programação"
nome = input("Bem-vindo! Digite seu nome: ")

print(f"\n--- {curso} ---")
print(f"Olá, {nome}. Vamos calcular a sua média final.")

# Coleta das notas usando um laço de repetição
notas = []
extensos = ["primeira", "segunda", "terceira", "quarta"]

for i in range(4):
    nota = float(input(f"Digite a {extensos[i]} nota: "))
    notas.append(nota)

# Cálculo e exibição dos resultados
media = sum(notas) / len(notas)

print("\n" + "=" * 30)
print(f"Aluno(a): {nome}")
print(f"Notas obtidas: {notas}")
print(f"Média Final: {media:.2f}")  # O :.2f limita para 2 casas decimais
print("=" * 30)