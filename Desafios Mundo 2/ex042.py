print()
print('efaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.')
print('- EQUILÁTERO: todos os lados iguais')
print('- ISÓSCELES: dois lados iguais, um diferente')
print('- ESCALENO: todos os lados diferentes')
print('___________________________________________________________ \n')

r1 =  int(input('Digite a reta número 1:'))
r2 =  int(input('Digite a reta número 2:'))
r3 =  int(input('Digite a reta número 3:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Sim pode formarm um triângulo', end='')
    if r1== r2 ==r3:
        print('e aqui temos um EQUILÁTERO onde todos os lados são iguais')
    elif r1 != r2 != r3 != r1:
        print('e aqui temos um ESCALENO onde todos os lados são diferentes')
    else:
        print('e aqui temos um ISÓSCELES onde dois lados iguais, um diferente')
else:
    print('Não formam triangulo')  




#

print('_______________________________________________________________')