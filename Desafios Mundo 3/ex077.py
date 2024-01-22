print('')
print('{:=^80}'.format(' Exercício Python 77'))
print('Crie um programa que tenha uma tupla com várias palavras (não usar acentos).')
print('Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais')
print()


lista =(
        'APREENDER','PROGRAMAR','LINGUAGEM',
        'PYTHON','CURSO','GRATIS',
        'ESTUDAR','PRATICAR','TRABALHAR',
        'MERCADO','PROGAMADOR','FUTURO')


for i in lista:
        if 'A' in i:
                print(i+'-A')
        elif 'E' in i:
               print(i+'-E')
        elif 'I' in i:
               print(i+'-I')
        elif 'O' in i:
               print(i+'-O') 
        elif 'U' in i:
               print(i+'-U') 

