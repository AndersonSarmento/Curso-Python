print("{:=^80}".format("Exercícios Python 82"))
print('Crie um programa que vai ler vários números e colocar em uma lista')
print('Depois separe em duas listas sendo uma par e outra impar')
print('Ao finalmostre as 3 listas geradas no programa')
print('')

lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor :')))
    resp=str(input('Quer continuar?[S/N]')).upper()
    if resp in 'N':
        break

for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('-='*30)
print(f'Aqui temos a lista cpmpleta:',lista)
print(f'Aqui temos a lista dos pares',pares)
print(f'Aqui temos as lista de ímpares ',impares)