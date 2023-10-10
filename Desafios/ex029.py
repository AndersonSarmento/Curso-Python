print()
print('Escreva um programa que leia a velocidade de um carro.\n Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. \n A multa vai custar R$7,00 por cada Km acima do limite.')
print('___________________________________________________________ \n')

vel = int(input('Qual velocidade o carro está? ')) 
limite = 80.00
multa = float((vel-limite)*7.00)
acima = float(vel-limite)

if vel > 80:
    print('Você ultrapassou o limite de velocidade de 80km/h')
    print('Sua velocidade registrou {:.2f}km/h ACIMA do permitido!!!'.format(acima))
    print('Parabéns você ganhou uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! E dirija com segurança!')



print('_______________________________________________________________')