print('{:=^80}'.format('Exercício Python 057'))
print()
print('Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. \n Caso esteja errado, peça a digitação novamente até ter um valor correto.')

sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        print('Sexo masculino registrador com sucesso')
    elif sexo == 'F':
        print('Sexo feminino registrador com sucesso')   
print('Muito obrigado!')
print('Fim')


