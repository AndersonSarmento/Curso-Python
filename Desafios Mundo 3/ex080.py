print('')
print('{:=^80}'.format(' Exercício Python 80'))
print('')
print('Crie um  programa onde o usuário possa digitar cinco valores numéricos inteiros e cadastre-os em uma lista.')
print('Já na posição correta de inserção sem usar o sort().No final, mostrer a lista ordenada na tela')
print('')

lista =  []
for numero in range(0,5):
    valor = int(input('Digite um valor: '))
    if numero == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos,valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')

# Crie um programa onde o usuário possa digitar cinco valores numéricos inteiros e cadastre-os em uma lista.
# Já na posição correta de inserção sem usar o sort(). No final, mostre a lista ordenada na tela.

# Inicialize uma lista vazia para armazenar os valores
lista_valores = []

# Solicite ao usuário que insira cinco valores
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    
    # Encontre a posição correta para inserção
    posicao = 0
    while posicao < len(lista_valores) and valor > lista_valores[posicao]:
        posicao += 1
    
    # Insira o valor na posição correta
    lista_valores.insert(posicao, valor)

# Mostre a lista ordenada
print("Lista ordenada:")
for valor in lista_valores:
    print(valor)
