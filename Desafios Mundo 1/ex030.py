print()
print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')
print('___________________________________________________________ \n')

numero = int(input('Digite o seu número: '))
result = numero%2

if result == 0:
    print('PAR')
else:
    print('INPAR')
print('_______________________________________________________________')
