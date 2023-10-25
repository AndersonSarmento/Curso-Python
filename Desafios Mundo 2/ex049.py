print('{:=^80}'.format(''))
print('Crie um programa  que receba um número e faça a sua tabuada? ')
tabuada = int(input('Digite o seu número:'))
print('O seu número é:', tabuada)

for n in range(1,tabuada+1,1):
    print('{}x{}={}'.format(tabuada,n,tabuada*n))
print('===========================================================')