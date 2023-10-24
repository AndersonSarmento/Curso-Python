print('{:-^60}'.format('-------'))
print('Faça um programa que mostre na tela uma contagem regressiva para o estouro de  \n fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.\n')
print('{:-^60}'.format('CONTADOR'))
from time import sleep 

for contador in range(10,-1,-1):
    print('É',contador,'!' )
    sleep(1)
print('BUMM! BUMM POOOW!')
print('\U0001f4a3'*4)
print('{:-^60}'.format('-------'))


