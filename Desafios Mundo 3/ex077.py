print('')
print('{:=^80}'.format(' Exercício Python 77'))
print('Crie um programa que tenha uma tupla com várias palavras (não usar acentos).')
print('Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais')
print()


palavras =(
        'APREENDER','PROGRAMAR','LINGUAGEM',
        'PYTHON','CURSO','GRATIS',
        'ESTUDAR','PRATICAR','TRABALHAR',
        'MERCADO','PROGAMADOR','FUTURO')

for p in palavras:
        print(f'\nNa palavra {p} temos:', end='')
        for letra in p:
                if letra in 'AEIOU':
                        print(letra, end=' ')
print(' ')
