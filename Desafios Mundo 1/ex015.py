print()
print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e \n a quantidade de dias pelos quais ele foi alugado.\n Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
print('\n')
rodou = float(input('Rodou quantos Kms?'))
dias = int(input('Você alugou o carro por quantos dias?'))
aluguel = dias* 60.00
tarifa_km = rodou * 0.15
total= aluguel+tarifa_km
print(' ============== Extrato ================= ')
print(' Total de dias com o carro {} dias'.format(dias)) 
print(' Valor total das diarias R$ {:.2f} reais'.format(aluguel))
print(' Valor total da tarifa por km R${:.2f} reais'.format(tarifa_km))
print(' Valor total a pagar R$ {:.2f} reais'.format(total))
print(' ========================================= ')