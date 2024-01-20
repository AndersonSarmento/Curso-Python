print()
print('{:=^80}'.format(' Exercício Python 75 '))
print('Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.')
print('No final, mostre:')
print('A) Quantas vezes apareceu o valor 9.')
print('B) Em que posição foi digitado o primeiro valor 3.')
print('C) Quais foram os números pares.')
print()

tupla=(int(input('Digite o valor: ')),
       int(input('Digite o valor: ')),
       int(input('Digite o valor: ')),  
       int(input('Digite o valor: ')))
print(f'Os números digitados são {tupla}')


print(f'O número nove apareceu na Tupla:{9 in tupla}')

x=0
for i in tupla:
    if i == 9:
        x += 1
print(f'O número nove apareceu {x} vezes!')
print('Outra forma de aparecer o 9')
print(f'O número 9 apareceu {tupla.count(9)} vezes- USANDO COUNT')
if 3 in tupla:
    print(f'O número 3 apareceu na primeira vez na posicão: {tupla.index(3)}')
else:
    print(f'O múmero 3 não foi encontrado')

for i in tupla:
    if i%2 == 0:
        print(i, end='')

print()




