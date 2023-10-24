print('{:=^80}'.format(''))
print('Crie um programa que mostre na tela todos os números pares \n que estão no intervalo entre 1 e 50.')

intervalo = 50
inicio = 2
par = 2

for lista_pares in range(inicio, intervalo+1,par):
    print(lista_pares, end='-')
print('FIM')

print('{:=^80}'.format(''))

