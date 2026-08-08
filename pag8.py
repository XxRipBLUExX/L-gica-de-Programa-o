import os
os.system('cls' if os.name == 'nt' else 'clear')

#Idade

idade=int(input("Digite sua idade: "))
if idade <= 12:
    print("Você é uma criança.")
elif idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é um adolescente.")

#Bateria

bateria = int(input("Digite a porcentagem da bateria do seu celular: "))
if bateria >= 80:
    print("Bateria cheia.")
elif bateria >= 50:
    print("Bateria moderada.")
else:
    print("Bateria baixa.")

#Atendimento

nota_atendimento = float(input("Digite a nota do atendimento (0 a 10): "))
if nota_atendimento >= 9:
    print("Atendimento excelente.")
elif nota_atendimento >= 7:
    print("Atendimento bom.")
else:
    print("Atendimento ruim.")

#Prioridade

prioridade = input("Digite a prioridade (alta, média, baixa): ")
if prioridade == "alta":
    print("Prioridade alta, delocamento em cod. 3.")
elif prioridade == "média":
    print("Prioridade média, delocamento em cod. 2.")
else:
    print("Prioridade baixa, delocamento em cod. 1.")

#Desconto em Loja

desconto = float(input("Digite o valor da compra: "))
if desconto >= 1000:
    print("Desconto de 10%")
elif desconto >= 500:
    print("Desconto de 5%")
else:
    print("Sem desconto.")

print("-" * 30)

#Dinheiro

dinheiro = float(input("Digite quantos reais (R$) você tem: "))
if dinheiro >= 1000:
    print("Você é pobre.")
elif dinheiro >= 500:
    print("Você é classe média.")
else:
    print("Você é rico.")

print("-" * 30)
print("Fim do programa.")
