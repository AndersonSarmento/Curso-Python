print()
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
number = float(input('Entre com o valor do cateto oposto: '))
print('___________________________________________________________')

from math import radians, sin, cos, tan
number = radians(number)
tangente = tan(number)
cosseno = cos(number)
seno = sin(number)

print('O angulo escolhido foi {:.2f} então temos: '.format(number))
print('O valor do seno é: {:.2f}'.format(seno))
print('O valor do cosseno é: {:.2f}'.format(cosseno))
print('O valor do tangente é: {:.2f}'.format(tangente))
print('___________________________________________________________')
