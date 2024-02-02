print('')
print('{:=^80}'.format(' Exercício Python 79 '))
print('')
print('Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.')
print('Caso o número já exista lá dentro, ele não será adicionado.')
print('No final, serão exibidos todos os valores únicos digitados, em ordem crescente')
print('')
valores = []
numero = 0

while True:
    if numero not in valores:
        numero = int(input('Digite o seu número'))
        valores.append(numero)
    else:
        print('Digite outro valor este já está na lista')

    valores.append(numero)
   
    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N :')).upper().strip()[0]
    if resp == 'N':
        break
print(sorted(valores)[:1])



