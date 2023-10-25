print('{:=^80}'.format('='))
print('')
print('Faça um programa que calcule a soma entre todos os números que são múltiplos \n de três e que se encontram no intervalo de 1 até 500.')

soma=0
contador = 0
for n in range(1,500+1,2):
    if n % 3 == 0:
        soma =soma+n
        contador = contador+1
print('A soma de todos os múltiplos de 3 é {} e a contagem deles é de {} números '.format(soma,contador))
print('')
print('{:=^80}'.format('='))
