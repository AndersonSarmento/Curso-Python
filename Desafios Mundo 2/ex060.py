from os import pidfd_open


print('{:=^80}'.format('Exercício Python 060'))
print('Faça um programa que leia um número qualquer e mostre o seu fatorial.')
print()

fatorial = int(input('Digite um número e descubra o seu fatorial '))
print('Calculando {}! = '.format(fatorial), end='')
x = fatorial
f = 1
while x > 0:
    print('{} '.format(x), end='')
    print(' x ' if x > 1 else ' = ',end='')
    f *= x
    x-=1

print('{}'.format(f))
