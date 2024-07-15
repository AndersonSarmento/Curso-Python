print('')
print('{:=^80}'.format(' Exercício Python 85'))
print('Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que')
print('mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente. ')
print('')

print('-='*30)
lista = list()

num = [[],[]]
valor = 0

for c in range(1,8):
    valor=int(input(f'Digite um o {c}. valor:'))
    if valor %2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(f'Os valores pares são{sorted(num[0])}')
print(f'Os valores inpares são{sorted(num[1])}')
print('-='*30)
