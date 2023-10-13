print()
print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. \n Para salários superiores a R$1250,00, calcule um aumento de 10%.\n Para os inferiores ou iguais, o aumento é de 15%.')
print('___________________________________________________________ \n')

salario = float(input('Quanto é o seu salário?'))
aumento_10 = salario * 0.10
aumento_15 = salario * 0.15

if salario >= 1250:
    print('O seu aumento foi de R$ {} reais'.format(aumento_15))
    print('O seu total recebido será de R$',(salario+aumento_15),'reais')
else:
    print('O seu aumento foi de R$ {} reais'.format(aumento_10))
    print('O seu total recebido será de R$',(salario+aumento_10),'reais')
print('_______________________________________________________________')