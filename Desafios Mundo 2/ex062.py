print('')
print('{:=^80}'.format('Exercício Python 062'))
print('')
print('Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.')
print('')


primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo),end='')
    termo += razão
    cont += 1
  
 

print()


