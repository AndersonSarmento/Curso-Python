print('{:=^80}'.format('Exercício Python 064:'))
print()
print('Crie um programa que leia vários números inteiros pelo teclado. \n O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).')
print()

op =int(input('Digite um número ou [999 para parar]:'))
tentativas=0
total = (op+0)-999
while op != 999:
    op =int(input('Digite um número ou [999 para parar]:'))
    total += op 
    tentativas +=1

print('O valor da soma {} foi e foram {} tantas tentativas'.format(total,tentativas))
print('fim')
