print('=====================================================================')
print('Faça um programa que leia a largura e a altura de uma parede em metros, \n calcule a sua área e a quantidade de tinta necessária para \n pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.')
print('-----------------------------------------------------------------------')

largura = float(input('Qual a largura da parede?:'))
altura = float(input('Qual a altura da  parede ?:'))
area = largura*altura
tinta =  area/2
print('Você deve comprar {} litros de tinta para pintar os {}m2 da sua aprede '.format(tinta, area))