print()
print('Desenvolva um programa que pergunte a distância de uma viagem em Km.\nCalcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')
print('___________________________________________________________ \n')

distancia = float(input('Qual é a distância da sua viagen em KM ?'))

if distancia <= 200.00:
    print('Valor da sua viagen é de R$',(distancia*0.50),'reais')
else:
    print('Valor da sua viagen é de R$',(distancia*0.45),'reais')


print('_______________________________________________________________')