print('')
print('{:=^80}'.format('Exercício Python 061'))
print('')
print('Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.')
print('')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
while contador != 10:
    print(primeiro + (contador)* razão,end='-')
    contador =contador+1
print('Acabou')
print(40*'=')