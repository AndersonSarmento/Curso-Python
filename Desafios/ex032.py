print()
print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
print('___________________________________________________________ \n')
from datetime import date
ano = int(input('Digite o ano que você deseja saber se é bissexto. \n Para analisar o ano atual digite 0 '))

if ano == 0:
    ano = date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else: 
     print('O ano de {} NÃO é bissexto'.format(ano))   

print('_______________________________________________________________')