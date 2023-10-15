print()
print('Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. \n Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.')
print('___________________________________________________________ \n')

casa = float(input('Qual é o valor da casa desejada ?'))
renda = float(input('Qual o valor da renda do comprador?'))
prazo =  float(input('Quantos anos ela vai pagar?'))
prestacao = casa / (prazo * 12)
limite = renda * 0.30


if prestacao <= limite:
    print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa,prazo), end='')
    print(' o valor da prestação é de R$ {:.1f}'.format(prestacao))
    print('O empréstimo pode ser CONCEDIDO')
else:
    print('O empréstimo foi NEGADO')
    print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa,prazo), end='')
    print(' o valor da prestação é de R$ {:.1f} \n e supera os 30% de renda  que pode ser comprometida'.format(prestacao))

print('___________________________________________________________ \n')

print( '==============================================================')