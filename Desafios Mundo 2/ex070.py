print()
print('{:=^80}'.format('Exercício Python 070:'))
print('')
print('Crie um programa que leia o nome e o preço de vários produtos.\nO programa deverá perguntar se o usuário vai continuar ou não. \nNo final, mostre:')
print(' A) qual é o total gasto na compra.')
print(' B) quantos produtos custam mais de R$1000.')
print(' C) qual é o nome do produto mais barato.')
print('')

cont = total = maior_que_mil = menor = 0
barato = ''

while True:
    produto = str(input('Qual o nome do produto: '))
    preco = float(input('Qual o valor do produto R$:'))
    cont+=1
    total += preco
    if preco >= 1000:
        maior_que_mil +=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto    
    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N :')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total da compra foi R$ {total}')
print(f'Temos {maior_que_mil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi que {barato} custa R$ {menor:.2f}')
print('')

#if cont == 1:
#       menor = preco
#       barato = produto
#   else:
#       if preco < menor:
#           menor = preco
#           barato = produto