print('{:=^80}'.format('Exercício Python 054'))
print()
print('Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. \n Caso esteja errado, peça a digitação novamente até ter um valor correto.')

S = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    S = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
    print(S)

print('Fim')