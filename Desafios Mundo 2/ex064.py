print('{:=^80}'.format('Exercício Python 064:'))
print()
print('Crie um programa que leia vários números inteiros pelo teclado. \n O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).')
print()
numero = cont= soma = 0
numero =int(input('Digite um número ou [999 para parar]:'))
while numero != 999:
    soma += numero
    cont += 1
    numero =int(input('Digite um número ou [999 para parar]:'))
print('O valor da soma {} foi e foram {} tentativas'.format(soma,cont))
print('fim')
