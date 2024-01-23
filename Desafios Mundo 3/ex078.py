print('')
print('{:=^80}'.format(' Exercício Python 78'))
print('')
print('Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,') 
print('mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.')
print('')

cont= 1
pos = 0
lista = []
while cont <=5:
    numero = (int(input(f'Digite um valor para posição {pos}:')))
    cont +=1
    pos  +=1
    lista.append(numero)
print('')
maior = sorted(lista)[-1]
menor = sorted(lista)[0]
#elemento que retira a repetição do for
contm = contme = 0 

print(f'Você digitou os valores {lista}')
for i in lista:
    if i == maior and contm == 0: 
        contm += 1        
        print(f' O maior valor digitado foi {maior} nas posições', end='')
        for p,i in enumerate(lista):
            if i == maior:
                print(f' {p}...',end='')
print()
for i in lista:        
    if i == menor and contme == 0: 
        contme += 1        
        print(f' O menor valor digitado foi {menor} nas posições', end='')
        for p,i in enumerate(lista):
            if i == menor:
                print(f' {p}...',end='')
 
   
print('\n')
print('{:=^80}'.format(' Solução Guanabara'))

listanum=[]
mai = men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posicões ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print('')
print(f'O menor valor digitado foi {men} nas posicões ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print('')








