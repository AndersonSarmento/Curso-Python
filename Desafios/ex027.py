print()
print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.')
print('___________________________________________________________')

nome = str(input('Digite um nome com sobrenome completo :')).capitalize().strip()
nome_fatiado = nome.split()



print('Seu primeiro nome é:',nome_fatiado[0])
print('Seu último nome é:',nome_fatiado[-1])
print('\n ___________________________________________________________')