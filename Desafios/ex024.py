print()
print('Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"')
print('___________________________________________________________')

cidade = str(input('Digite sua cidade de origem!')).strip()

cidade_title = cidade.title()
cidade_split = cidade.split()
cidade_lista = cidade_split[0]
cidade_title = cidade_lista
cidade =('Santo' in cidade_lista)

print(cidade_title)
print(cidade_split)
print(cidade_split)
print(cidade_lista)
print(cidade)