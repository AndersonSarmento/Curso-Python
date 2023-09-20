print('=====================================================================')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo \n preço, com 5% de desconto.')
print('-----------------------------------------------------------------------')

valor = float(input('Digite o valor do produto!'))
margem = int(input('Digite o percentual de ganho que gostaria neste produto!'))
valor_final = (valor-((margem/100)*valor))
print('O valor base deste produto é r${:.2f} reais, se vc colocar a margem de desconto de {}% no \n preço inicial seu valor final será de R${:.2f} reais'.format(valor,margem,valor_final))
print()