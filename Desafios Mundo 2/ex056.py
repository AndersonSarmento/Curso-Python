from typing import Dict


print(':=^80'.format('Exercício Python 056: '))
print()
print('Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. \n No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.')
print()
#variaveis
somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho= ''
tormulher20 =0


for p in range(1,5):
    print('----- {}ª  PESSOA ----- '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        tormulher20 +=1


mediaidade = somaidade /4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}.'.format(maioridadehomen, nomevelho))
print('Ao todo temos são {} mulheres com menos de 20 anos'.format(tormulher20))

print('')