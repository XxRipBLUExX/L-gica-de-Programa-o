import os
os.system('cls' if os.name == 'nt' else 'clear')

contador = 1
total = 0
extensos = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]

# Solicita cinco números usando while
while contador <= 5:
    numero = float(input(f"Digite o {extensos[contador - 1]} número: "))
    total = total + numero
    contador = contador + 1

# Exibe o resultado final
print(f"\n--- RESULTADO FINAL ---")
print(f"Soma dos 5 números: {total}")
print(f"Média dos 5 números: {total / 5:.2f}")