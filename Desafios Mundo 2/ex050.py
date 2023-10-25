print('')
print('{:=^80}'.format('Exercício Python 050'))
print('')
print('Desenvolva um programa que leia seis números inteiros e mostre a soma apenas\n daqueles que forem pares.Se o valor digitado for ímpar, desconsidere-o.')
print('')

numero =int(input('Digite o número que deseja: '))

soma = 0
contador = 0
if numero %2 ==0:
    for c in range(0,numero+1,2):
        print(c)
        soma += c
        contador = contador+1 
else:
    print('O número {} não é PAR \n'.format(numero))

print('A soma dos {} números pares dentro do range de 0 até {} é {} \n'.format(contador,numero,soma))
print('=-='*40)
