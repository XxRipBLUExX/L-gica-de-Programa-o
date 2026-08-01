import os # Lib para limpar a tela do terminal
import random
import time
import keyboard  # Biblioteca simples para ler o teclado

# Configurações do jogo
LARGURA_PISTA = 10
ALTURA_PISTA = 15

# Posição inicial do jogador (X começa no meio da pista)
jogador_x = LARGURA_PISTA // 2

# Obstáculo (carro inimigo)
obs_x = random.randint(0, LARGURA_PISTA - 1)
obs_y = 0

pontos = 0

print("Jogo Iniciado! Use as setas ESQUERDA e DIREITA para mover.")
time.sleep(2)

while True:
    # 1. Movimentação do jogador
    if keyboard.is_pressed("left") and jogador_x > 0:
        jogador_x -= 1
    elif keyboard.is_pressed("right") and jogador_x < LARGURA_PISTA - 1:
        jogador_x += 1

    # 2. Movimentação do obstáculo
    obs_y += 1

    # Se o obstáculo passou do final da tela, reseta ele no topo
    if obs_y >= ALTURA_PISTA:
        obs_y = 0
        obs_x = random.randint(0, LARGURA_PISTA - 1)
        pontos += 1

    # 3. Verifica colisão
    if obs_x == jogador_x and obs_y == ALTURA_PISTA - 1:
        print(f"\n💥 BATIDA! Fim de jogo. Pontuação final: {pontos}")
        break

    # 4. Desenha a tela no terminal
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    print(f"Pontos: {pontos} | Siga desviando!")
    print("-" * (LARGURA_PISTA + 2))  # Teto da pista

    for y in range(ALTURA_PISTA):
        linha = "|"  # Parede esquerda
        for x in range(LARGURA_PISTA):
            if x == jogador_x and y == ALTURA_PISTA - 1:
                linha += "A"  # Seu carro
            elif x == obs_x and y == obs_y:
                linha += "X"  # Carro inimigo
            else:
                linha += " "  # Espaço vazio
        linha += "|"  # Parede direita
        print(linha)

    print("-" * (LARGURA_PISTA + 2))  # Chão da pista

    # Controla a velocidade do jogo (quanto menor o número, mais rápido)
    time.sleep(0.1)