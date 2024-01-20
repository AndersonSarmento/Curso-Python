print()
print('{:=^80}'.format('Exercício Python 74'))
print('')
print('Crie um programa que vai gerar cinco números aleatórios e colocar em uma numeros.')
print('Depois disso, mostre a listagem de números gerados e também indique\no menor e o maior valor que estão na numeros.')
print()
print('{:=^80}'.format('Resposta'))
print('')
import random
#y=random.randrange(100)

numeros = []
for lista in range(1,6):
    y=random.randrange(100)
    x = lista*y
    numeros.append(x)
tupla = tuple(numeros)

print(f'Lista com números aleatórios:{numeros,type(numeros)}')
print(f'Lista convertida para tupla com método tuple:{type(tupla)}')
print(f'Tupla ordenada com método sorted{sorted(tupla)}')
print(f'O maior número é {max(tupla)} e o menor é {min(tupla)}')
print('')