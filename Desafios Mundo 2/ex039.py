print()
print('Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, \n se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.\n Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.')
print('___________________________________________________________ \n')
import datetime 

print('Qual é o seu sexo : \n [1]Masculino \n [2]Feminino.')
sexo = int(input('Digite o número correspondente ao seu sexo  '))
nascimento = int(input('Digite o ano de seu nascimento, no formato YYYY, ex: 1956 ').strip())



ano_alistamento = nascimento+18 
hoje = datetime.datetime.now()
hoje = int(hoje.strftime("%Y"))
idade = hoje-nascimento
faltam=ano_alistamento-hoje

if sexo == 2:
    print('De acordo com a legislação o seu comparecimento não é obrigatório ')
elif idade == 18:
    print('Quem nasceu em {} tem {} em {}!'.format(nascimento,idade,hoje))
    print('Seu alistamento deve ser IMEDIATAMENTE ')
elif idade < 18:
    print('Quem nasceu em {} tem {} em {}!'.format(nascimento,idade,hoje))
    print('Ainda faltam {} anos para o alistamento'.format(faltam))
    print('Seu alistamento será no ano de {}'.format(ano_alistamento))
elif idade >18:
    print('Quem nasceu em {} tem {} em {}!'.format(nascimento,idade,hoje))
    print('Você deveria ter se alistado há {} anos'.format(faltam))
    print('Seu alistamento foi em {}'.format(ano_alistamento))
else:
    print('Suas opções são inválidas')

print( '==============================================================')
