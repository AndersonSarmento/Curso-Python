print()
print('{:=^80}'.format('Exercício Python 071:'))
print('')
print('Crie um programa que simule o funcionamento de um caixa eletrônico.\nNo início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)')
print('e o programa vai informar quantas cédulas de cada valor serão entregues.')
print('OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.')
print('')


print('{:-^40}'.format(' Banco Ander '))
valor = float(input('Qual o valor a ser sacado '))
total = valor
cédula = 50
totcéd = 0
while True:
    if total >= cédula:
        total -= cédula
        totcéd +=1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} células de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula =  1
        totcéd = 0
        if total ==0:
            break 
print('{:-^40}'.format('Gaste com sabedoria '))
print()



    