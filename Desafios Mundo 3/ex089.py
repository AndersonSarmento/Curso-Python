print()
print('{:=^80}'.format(' Exercício Python 84'))
print()
print('Faça um programa que leia nome e peso de várias pessoas,')
print('guardando tudo em uma lista e no final mostre')
print('\n A)Quantas pessoas foram cadastradas \n B)Uma listagem com as pessoas mais pesadas \n C) uma listagem com as pessoas mais leves')
print('')
print('-='*30)
#cadastra  as pessoas
dado = list()
pessoas = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso ')))
    pessoas.append(dado[:])
    dado.clear()
#faz a media de peso das pessoas
totpeso=list()
for p in pessoas:
    totpeso.append(p[1])

totpessoas=(int(len(pessoas)))

media = sum(totpeso)/totpessoas

leve = list()
pesado = list()

for p in pessoas:
    if p[1] > media:
        pesado.append(p[0])
    else:
        leve.append(p[0])

print(f'A) Temos',totpessoas,'cadastradas')
print(f' Temos uma média de peso  de {media} então')
print(f'B)Os leves são{leve}')
print(f'C)Os pesados são{pesado}')

