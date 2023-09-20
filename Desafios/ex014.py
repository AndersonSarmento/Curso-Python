print('=======================================================================')
print('Escreva um programa que converta uma temperatura digitando em graus \n Celsius e converta para graus Fahrenheit e Kelvin', end='\n')
print()
celsiu = float(input('Qual a temperaturaem Celsius?'))
Fahrenheit = (celsiu*1.8)+32
Kelvin = celsiu+273.15
print('A temperatura em Fahrenheit é {:.2f}F!'.format(Fahrenheit))
print('A temperatura em Kelvin é {:.2f}K!'.format(Kelvin))