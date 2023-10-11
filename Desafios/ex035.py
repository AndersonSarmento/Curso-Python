print()
print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.')
print('___________________________________________________________ \n')

r1 =  int(input('Digite a reta número 1:'))
r2 =  int(input('Digite a reta número 2:'))
r3 =  int(input('Digite a reta número 3:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Sim pode formarm um triângulo ')
else:
    print('Essa três retas não forman um triângulo')

print('_______________________________________________________________')