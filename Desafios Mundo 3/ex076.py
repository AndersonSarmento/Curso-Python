print('')
print('{:=^80}'.format(' Exercício Python 76 '))
print('Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos')
print('preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.')
print('')

lista =('Lápis',1.75,
        'Borracha',2.00,
        'Caderno',15.90,
        'Estojo',25.00,
        'Transferidor', 4.20,
        'Compasso',9.99,
        'Mochila',120.32,
        'Canetas',22.30,
        'Livros',34.90)

print('-'*40)
print('{:=^40}'.format(' LISTAGEM DE PREÇOS '))
print('-'*40)
for i in range(0,len(lista)):
    if i %2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>7.2f}')
print('-'*40)