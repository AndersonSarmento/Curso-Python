print()
print('{:=^80}'.format('Exercício Python 066:'))
print(' Crie um programa que leia vários números inteiros pelo teclado. \n No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. \n O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.')
print()


resp = 'S'
média = quant = soma= maior = menor =0

while resp in 'Ss':
    num =  int(input('Digite um número: '))
    soma +=num
    quant +=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp=input('Você deseja digitar um novo número? S/N ').upper().strip()[0]
média= soma /quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
print()