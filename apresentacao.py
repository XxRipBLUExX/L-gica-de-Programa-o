import os
os.system('cls' if os.name == 'nt' else 'clear')

nome = input("Bem-vindo! Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
curso = input("Digite o curso que você está cursando: ")
area = input("Digite a área de atuação: ")

print("\n" + "=" * 30)
print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}.")
print(f"Você está cursando {curso} na área de {area}.")
print("Desejamos muito sucesso em sua jornada de aprendizado!")
print("=" * 30)