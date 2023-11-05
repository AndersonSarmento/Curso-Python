print('')
print('{:=^80}'.format('Exercício Python 052'))
print('')
print('Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.')
from re import M
from time import sleep
from typing import MutableMapping 


numero=int(input('Digite o seu número : '))
tot =0

for c in range(1,numero+1,1):
    if numero % c == 0:
        print('\033[33m', end = '')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{}'.format(c), end ='-')
print('\n\033[mO O número {} foi divisivel  {} vezes'.format(numero,tot))
if tot ==2:
    print('É por isso ele É PRIMO!')
else:
    print('É por isso ele NÃO PRIMO!')
print()


   