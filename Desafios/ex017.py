print()
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.')
print('\n')
co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))

hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print("\n**************************\n")

print("O valor da hipotenusa é: {:.2f}".format(hipotenusa))

from math import hypot
hi = hypot(ca, co) 
print("Usando from math import hypot O valor da hipotenusa é: {:.2f}".format(hi))
