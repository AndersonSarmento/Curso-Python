print('')
print('{:=^80}'.format('Exercício Python 061'))
print('')
print('Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.')
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

while 