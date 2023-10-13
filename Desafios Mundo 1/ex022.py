print()
print(''' Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.''')
print('___________________________________________________________')
nome = str(input('Digite o seu nome:>>>'))

print(nome.upper())  
print(nome.lower())
print(len(nome.strip())-nome.count(' '))
print(nome.split())
posica=nome.find(' ')
print(nome[:posica])
print(len(nome[:posica]))


