print()
print('{:=^80}'.format('Exercício Python 087'))
print('Aprimore o desafio anterior, mostrando no final:')
print('A) A soma de todos os valores pares digitados.')
print('B) A soma dos valores da terceira coluna.')
print('C) O maior valor da segunda linha.')
print()
print('-='*30)

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'Aqui temos a nossa matriz') 




print('---'*20)
pares =[]
terceira_coluna = []
maior = []
n = 0



for linha in matriz:
    for numero in linha:
        print(matriz[1][n])
        if numero == matriz[1]:
            maior.append(numero)
        if numero == matriz[n][2]:
            terceira_coluna.append(numero)
        if numero %2 == 0:
            pares.append(numero)
        
    n += 1
    
   
print(maior)
print(f'A)A soma de todos os valores pares digitados é:',sum(pares))
print(f'B) A soma dos valores da terceira coluna é:',sum(terceira_coluna))
print(f'C) O maior valor da segunda linha.',maior)
