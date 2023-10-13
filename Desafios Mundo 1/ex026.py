print()
print('Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", \n em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.')
print('__________________________________________________________________')

frase = str(input("Digite sua frase >>>> :")).strip()
frase = frase.upper()
frase_contador = frase.count('A')
frase_find = frase.find('A')+1
frase_rfind = frase.rfind('A')+1

print('A letra A parece {} vezes na frase'.format(frase_contador))
print('A sua primeira aparição é na posição {}'.format(frase_find))
print('A sua ultima aparição é na posição {}'.format(frase_rfind))
