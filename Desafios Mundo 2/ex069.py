print()
print('{:=^80}'.format('Exercício Python 069:'))
print('Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:')
print('A) quantas pessoas tem mais de 18 anos.')
print('B) quantos homens foram cadastrados.')
print('C quantas mulheres tem menos de 20 anos.')
print()

print('-'*30)
print('{:-^30}'.format(' Cadadastre uma pessoa '))
print('-'*30)

cont_maior = cont_menor =  cont_mu20 = cont_h20 = 0
cont_homen = 0
cont_mulher = 0

while True:
    idade = int(input('Qual é a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('M/F :')).upper().strip()[0]  

    if idade >= 18:
        cont_maior += 1
    if idade <= 17:
        cont_menor += 1
    elif sexo == 'M':
        cont_homen += 1
    if sexo == 'F':
        cont_mulher += 1
    if sexo == 'F' and idade <= 20:
        cont_mu20 += 1
    if sexo == 'M' and idade <= 20:
        cont_h20 += 1
    
    resp=' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N :')).upper().strip()[0]
    if resp == 'N':
        break

print('-'*30)
print('{:-^30}'.format(' Cadadastros efetuados '))
print('-'*30)
print(f'Total de pessoas com mais de 18 anos:{cont_maior} e {cont_menor} com menos')
print(f'Ao todo temos {cont_homen} homen(s) cadastrados e {cont_mulher} mulheres')
print(f'E temos {cont_mu20} mulheres com menos de 20 anos')
print(f'E temos {cont_h20} homen(s) com menos de 20 anos')


