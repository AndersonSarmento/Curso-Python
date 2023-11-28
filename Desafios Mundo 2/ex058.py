print('{:=^80}'.format('Exercício Python 058'))
print()
print('Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. \n Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.')
from random import randint
from time import sleep 
computador = randint(0,5)

number = int(input('Digite o seu número de 0 á 5: '))

tentativas = 1
while number != computador:
    print('Analizando o input.')
    sleep(0.5)
    print('Analizando o input..')
    sleep(0.5)
    print('Analizando o input...')
    if number < computador:
        print('Digite um numero maior')
    elif number > computador:
        print('Digite um numero menor')
    number = int(input('Digite novamente  seu número de 0 á 5: '))
    tentativas =tentativas+1
print()
print('{:=^40}'.format('Processando os resultados.'))
print('Processando os resultados.')
sleep(0.5)
print('Processando os resultados..')
sleep(0.5)
print('Processando os resultados...')
sleep(0.5)
print('O computador digitou {} e você {}'.format(computador,number))
print('Você prescisou de {} tentativas'.format(tentativas))
print('Fim')