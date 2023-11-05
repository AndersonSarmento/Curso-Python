print('')
print('{:=^80}'.format('Exercício Python 054'))
print('')
print('Crie um programa que leia o ano de nascimento de sete pessoas. \n No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.')

from datetime import date
ano_atual = date.today().year
totmaior= 0
totmenor= 0


for pess in range(1,8):
    nasc = int(input('Qual ano a {} nasceu'.format(pess)))
    idade =  ano_atual-nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('e também tivemos {} pessoas menores de idade'.format(totmenor))

