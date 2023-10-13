print()
print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.')
print('___________________________________________________________')
numero = int(input("Digite um numero de 0 a 9999 :>>>"))

print('Analisando o número:{}'.format(numero))
print('Unidade:',numero//1 %10)
print('Dezena:' ,numero//10 %10)
print('Centena:',numero//100 %10)
print('Milhar:' ,numero//1000 %10)




