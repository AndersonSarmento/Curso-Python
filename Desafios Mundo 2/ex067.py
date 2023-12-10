from types import MemberDescriptorType


print()
print('{:=^80}'.format('Exercício Python 067'))
print()
print('Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.\nO programa será interrompido quando o número solicitado for negativo.')
print()
print('{:=^40}'.format(' Resultados: '))
print()

while True:
    n=int(input('Quer digitar a sua tabuada favorita?'))
    if n<0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{n}x{c}={n*c}')
    print('-'*30)
print(f'Programa encerrado o {n} é negativo')
    

  
