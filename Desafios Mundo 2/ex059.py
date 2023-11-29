print('{:=^80}'.format('Exercício Python 059'))
print()
print('Crie um programa que leia dois valores e mostre um menu na tela:')
print('[ 1 ] somar')
print('[ 2 ] multiplicar')
print('[ 3 ] maior')
print('[ 4 ] novos números')
print('[ 5 ] sair do programa')
print('Seu programa deverá realizar a operação solicitada em cada caso.')
print()
from time import sleep

print('{:=^20}'.format('Programa'))
valor1=int(input('Digite o primeiro valor. '))
valor2=int(input('Digite o segundo valor. '))
op=int(input('>>>>> Digite sua opção '))
operacoes =0

while op != 5:
    if op == 1:
        resultado =valor1+valor2
        print('O resultado desta operação:{}+{}={}'.format(valor1,valor2,resultado))
    elif op == 2:
        resultado =valor1*valor2
        print('O resultado desta operação:{}x{}={}'.format(valor1,valor2,resultado))
    elif op == 3:
        if valor1 > valor2:
            print('O número maior é:',valor1)
        elif valor1 == valor2:
            print('Os números são iguais:',valor1)
        else:
            print('O número maior é:',valor2)            
    elif op == 4:
        valor1=int(input('Digite o primeiro valor. '))
        valor2=int(input('Digite o segundo valor. '))
    else:
        print('opção inválida')
    print()
    print('{:=^20}'.format('Operações'))
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')           
    operacoes = operacoes+1
    op=int(input('Digite uma nova opção: '))
sleep(2)
print('=-='*20)
print('Você usou {} operações diferentes'.format(operacoes))
print('Obrigado e até breve!')
print('')


