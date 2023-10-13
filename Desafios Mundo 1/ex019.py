print()
print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro.\nFaça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.')
print('___________________________________________________________')
from random import choices

alunos = ['o Mario', 'o Luigui', 'o Kopa', 'a Peach', 'o Toad']

escolhido = choices(alunos)
sem_colchetes =str(escolhido)[1:-1]
sem_aspas = sem_colchetes.replace("'","")
print('Imprimindo a lista:>>>>',alunos)
print('Usando o metodo choice para selecionar o aluno:>>>>',escolhido)
print('Retirando os colchetes do escolhido:>>>>', sem_colchetes)
print('Retirando as aspas do escolhido:>>>>', sem_colchetes)
print('O escolhido foi,{}'.format(sem_aspas))
print('___________________________________________________________')