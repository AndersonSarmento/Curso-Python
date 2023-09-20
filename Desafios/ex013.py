print('====================================================================')
print('Faça um algoritmo que leia o salário de um funcionário  \n e mostre seu novo salário, com % de aumento escolhido por ele.')
print('-----------------------------------------------------------------------')

valor = float(input('Digite o seu sálario!'))
margem = int(input('Digite o percentual de ganho que gostaria no rejuste '))
valor_final = (((margem/100)*valor)+valor)
ganho = valor_final-valor
print('O valor base do seu sálario é R${:.2f} reais, depois do reajute será de R${:.2f} reais'.format(valor,valor_final))
print('você teve um aumento de R${:.2f} reais, que equivale a {}%'.format(ganho, margem))