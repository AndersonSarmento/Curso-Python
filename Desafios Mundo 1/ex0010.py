print('=========================================================================')
print('Crie um programa que leia quanto dinheiro uma pessoa \n tem na carteira e  mostre quantos Dólares ela pode comprar')
real = float(input('Quanto você tem na carteira!'))
dolar = 3.27
compra = real/dolar
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, compra))

