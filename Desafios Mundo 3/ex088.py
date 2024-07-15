print()
print('{:=^80}'.format('Exercício Python 88'))
print('Faça um programa que ajude um jogador da MEGA SENA a criar palpites.')
print('O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre')
print('1 e 60 para cada jogo, cadastrando tudo em uma lista composta.')
print()
import random
from time import sleep
print('-='*15)
print('{:^30}'.format(' PALPITES DA MEGA SENNA'))
print('-='*15)
print()

# Pergunta quantos jogos o usuário quer gerar
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
matrizes = []

# Gera os palpites para cada jogo
for jogo in range(1, jogos + 1):
    matriz = []
    for numero in range(6):
        numero = random.randint(1, 60)
        matriz.append(numero)
    matrizes.append(matriz)

# Exibe os palpites gerados
for i, matriz in enumerate(matrizes, start=1):
    print(f'Jogo {i}: {matriz}')
    sleep(1)
print('{:^30}'.format(' BOA SORTE NA MEGA SENNA!'))