print()
print('Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:')
print('___________________________________________________________ \n')
n1=int(input('Digite o seu primeiro número:>'))
n2=int(input('Digite o seu segundo número:>'))

if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n1 < n2:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais')

print( '==============================================================')