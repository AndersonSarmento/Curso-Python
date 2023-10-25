print('')
print('{:=^80}'.format('Exercício Python 051'))
print('')
print('Desenvolva um programa que leia o primeiro termo e a razão de uma PA.\n No final, mostre os 10 primeiros termos dessa progressão.')
print('')



primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10-1)* razão
print('Primeiro Termo:',0)
print('Razão:',2)
for c in range(primeiro,décimo+razão,razão):
    print(c, end='-')   

print('Acabou')
print(40*'=')