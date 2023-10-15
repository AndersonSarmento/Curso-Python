print()
print('A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:')
print('- Até 9 anos: MIRIM')
print('- Até 14 anos: INFANTIL')
print('- Até 19 anos: JÚNIOR')
print('- Até 25 anos: SÊNIOR')
print('- Acima de 25 anos: MASTER')
print('___________________________________________________________ \n')

from datetime import date

ano = int(input('Qual é o seu ano de nascimento?'))
hoje = date.today().year
idade = hoje-ano

print('Sua idade é {}'.format(idade))
if idade <= 9:
    print('Categoria:MIRIM')
elif idade <=14: 
    print('Categoria:INFANTIL')
elif idade <=19:
    print('Categoria:JÚNIOR')
elif idade <=25:
    print('Categoria:SÊNIOR')
elif idade >25:
    print('Categoria:MASTER')
else:
    print('Algo está errado')

print( '==============================================================')