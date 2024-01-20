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

x=0
y=1
print('{:=^40}'.format(' LISTAGEM DE PREÇOS '))

for i in range(0,len(lista)):
    print(f'{lista[x]:.<30} R$ {lista[y]}')
    x +=2
    y +=2

print('')

