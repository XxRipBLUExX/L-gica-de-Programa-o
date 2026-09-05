import os
os.system('cls' if os.name == 'nt' else 'clear')

quantidade_vendas = int(input("Quantas vendas deseja registrar? "))

total_vendas = 0
for contador in range(quantidade_vendas):
 valor = float(input("Digite o valor da venda: "))
 total_vendas = total_vendas + valor
print(f"Total vendido: R$ {total_vendas:.2f}")