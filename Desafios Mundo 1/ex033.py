print()
print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
print('___________________________________________________________ \n')

n1 =  int(input('Digite o número 1:'))
n2 =  int(input('Digite o número 2:'))
n3 =  int(input('Digite o número 3:'))


menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n1 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n1 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))





print('_______________________________________________________________')