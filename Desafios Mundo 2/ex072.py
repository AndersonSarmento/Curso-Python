print('')
print('{:=^105}'.format('Exercício Python 072'))
print('')
print('Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.\nSeu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.\n')



lista = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove', 
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezesete', 'dezoito',
         'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número a sua escolha de 0 até 20.\nNúmero digitado: '))
    if 0 <= numero <= 20:
        break 
    print(f'Tente novamente. ', end= '')
print(f'Você digitou o número: {lista[numero]}')
print()

