print()
print('{:=^80}'.format('Exercício Python 068'))
print('')
print('Faça um programa que jogue par ou ímpar com o computador.\n O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. ')
print()

import random
jokepo = ['Papel','Tesoura','Pedra' ]

while True:
    perdeu = pontos = 0    
    usuario = input('Digite a sua escolha ').strip().capitalize()
    print(f'usuario{usuario}')
    pc =random.choice(jokepo)
    print(f'pc{pc}')
    if perdeu != 0:
        break
    if usuario == pc:
        print(f'Jogue novamente, pois ambos jogaran a mesma mão: {pc}')
    elif usuario == 'Papel' and pc == 'Pedra':
        pontos += 1
        print(pontos)
    elif usuario == 'Pedra' and pc == 'Tesoura':
        pontos += 1
        print(pontos)
    elif usuario == 'Tesoura' and pc == 'Papel':
        pontos += 1
        print(pontos)
    else:
        perdeu += 1
print(f'Pontos {pontos}')





#Papel vence Pedra
#Papel perde Tesoura #

#Tesoura vence Papel
#Tesoura perde Pedra
# 
#Pedra vence Tesoura  
#Pedra perde Papel