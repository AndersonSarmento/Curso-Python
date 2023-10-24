print()
print('Crie um programa que faça o computador jogar Jokenpô com você.')
print('___________________________________________________________ \n')
from time import sleep 
import emoji
import random
computador= numero=random.randrange(1,3,1)

print('[1]Pedra')
print('[2]Papel')
print('[3]Tesoura ')
escolha = int(input('Sua opção:'))
print( '==============================================================')
print('PROCESSANDO...')
sleep(1)

if escolha == 1:
    print('Você escolheu Pedra')
elif escolha == 2:
    print('Sua escolha foi Papel')
elif escolha == 3:
        print('Sua escolha foi Tesoura')
else:
    print('Sua escolha não existe')

if computador == 1:
    print('O computador escolheu Pedra')
elif computador == 2:
    print('O computador escolheu Papel')
elif computador == 3:
    print('O computador escolheu Tesoura') 

if escolha == computador:
    print('ISSO DEU EMPATE')
elif escolha ==1 and computador == 3:
    print('Eu venci já que Pedra vence Tesoura')
elif escolha ==2 and computador == 1:
    print('Eu venci já que Papel vence Pedra')
elif escolha ==3 and computador == 2:
   print('Eu venci já que Tesoura vence Papel')
else:
    print('O Computador ganhou!!')

 

print( '==============================================================')