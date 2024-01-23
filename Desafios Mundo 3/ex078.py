print('')
print('{:=^80}'.format(' Exercício Python 78'))
print('')
print('Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,') 
print('mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.')
print('')

cont= 1
pos = 0
lista = []
while cont <=5:
    numero = (int(input(f'Digite um valor para posição {pos}:')))
    cont +=1
    pos  +=1
    lista.append(numero)
print('')
maior = sorted(lista)[-1]
menor = sorted(lista)[0]


print(f'Você digitou os valores {lista}')
for pos,i in enumerate(lista):
    if maior == i:
        print(f'O maior valor digitado foi {maior} nas posições {pos}')
    elif menor == i:
        print(f'O menor valor digitado foi {menor} nas posições {pos}')









