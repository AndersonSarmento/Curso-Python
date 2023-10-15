print()
print('Crie um programa que leia duas notas de um aluno e calcule sua média, \n mostrando uma mensagem no final, de acordo com a média atingida:')
print('- Média abaixo de 5.0: REPROVADO \n- Média entre 5.0 e 6.9: RECUPERAÇÃO \n- Média 7.0 ou superior: APROVADO')
print('___________________________________________________________ \n')
import math

n1 = float(input('Nota da primeira prova :'))
n2 = float(input('Nota da segunda prova : '))


media = (n1+n2)/2

print('Suas notas são na primeira prova {:.2f} e na segunda prova {:.2f}'.format(n1,n2))
print('Sua média é {:.2f},'.format(media))
print('O seu resultado é:')
if media < 5.0:
    print('você foi: REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('Sua média é {},'.format(media))
    print('você foi: RECUPERAÇÃO') 
else:
    print('Sua média é {},'.format(media))
    print('você foi: APROVADO')






print( '==============================================================')

