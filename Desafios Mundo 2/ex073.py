print('')
print('{:=^105}'.format('Exercício Python 073'))
print('')

print('Crie uma tupla preenchida com os 20 primeiros colocados da times do Campeonato Brasileiro de Futebol,\nna ordem de colocação. Depois mostre:')
print(' a) Os 5 primeiros times.')
print(' b) Os últimos 4 colocados.')
print(' c) Times em ordem alfabética.') 
print(' d) Em que posição está o time da Chapecoense.') 
print('')

times =('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'Sao Paulo',
         'Atletico-MG', 'Athletico-PR','Cruzeiro','Botafogo','Santos',
         'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceara', 'Vasco',
         'América-MG', 'Sport', 'Vitória', 'Parana')


    
#resp=str(input('Digite a resposta que você deseja ter?')).strip().upper()[0]
    
    
print(f'Resposta A:\n{times[0:6]}\n')
  
print(f'Resposta B:\n{times[-5:-1]}\n')

print(f'Resposta C:\n{sorted(times)}\n')

print(f'Resposta C:')
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
print()

