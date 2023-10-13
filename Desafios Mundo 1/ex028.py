print()
print('Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. \n O programa deverá escrever na tela se o usuário venceu ou perdeu.')
print('___________________________________________________________ \n')
from random import randint
from time import sleep 
computador = randint(0,5)

number = int(input('Digite o seu número de 0 á 5: '))
print('PROCESSANDO...')
sleep(2)


if number == computador:
    print('Acertou Miserável!')
    print('Seu número é {} e o do computador foi {}'.format(number, computador))
else:
    print('Ai que burro da zero pra ele! ')
    print('Seu número é {} e o do computador foi {}!'.format(number, computador))

print('___________________________________________________________')


