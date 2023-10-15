print()
print('Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher\nqual será a base de conversão: \n [1]binário \n [2]octal \n [3]hexadecimal.')

print('___________________________________________________________ \n')

numero = int(input('Digite o seu numero:'))
print('Escolha a base de conversão: \n [1]binário \n [2]octal \n [3]hexadecimal.')
escolha = int(input('Base de conversão:'))

binario = (bin(numero)[2:])
octal = (oct(numero)[2:])
hexadecimal = (hex(numero)[2:])


if escolha == 1:
    print('O {} convertido para binário é {}:'.format(numero,binario))
elif escolha == 2:
    print('O {} convertido para octal  é {}:'.format(numero,octal))
elif escolha == 3:
    print('O {} convertido para hexadecimal é {}:'.format(numero,hexadecimal))
else:
    print('Opção não existente ')

print( '==============================================================')