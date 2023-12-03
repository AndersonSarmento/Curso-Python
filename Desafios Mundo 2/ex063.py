print('')
print('{:=^80}'.format(' Exercício Python 063 '))
print('Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.') 
print('')
print('')


print('{:=^30}'.format(' Sequência de Fibonacci'))
print()
termos = int(input('Quantos termos você quer mostar? '))
stop = termos
Termo1= 0
Termo2 = 1
print('~'*30)
print('{} - {}'.format(Termo1,Termo2), end='-')
cont = 3
while cont <= termos:
    Termo3 = Termo1+Termo2
    print(' {}'.format(Termo3), end='-')
    Termo1= Termo2
    Termo2 =Termo3
    cont +=1
print('FIM')