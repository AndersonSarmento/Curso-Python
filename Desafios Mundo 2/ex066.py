print()
print('{:=^80}'.format('Exercício Python 066:'))
print()
print(' Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.\n No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).')
print()
print('{:=^40}'.format(' Resultados: '))
print()
número = soma = tentativas = 0
while número != 999:
    número = int(input(' Digite um valor: '))
    if número == 999:
        break
    soma += número
    tentativas += 1
print(f'\nA soma total foi {soma} em {tentativas} tentativas!\n')
