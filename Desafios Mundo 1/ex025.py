print()
print('Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.')
print('___________________________________________________________')

nome = str(input('Digite o seu nome.')).strip()

nome = nome.upper()
nome =('SILVA' in nome)

print(nome)