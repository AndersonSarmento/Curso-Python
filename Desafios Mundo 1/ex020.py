print()
print('O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. \n Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
print('___________________________________________________________')
print()
from random import sample
alunos = ['o Mario', 'o Luigui', 'o Kopa', 'a Peach', 'o Toad']
escolhido = sample(alunos, k=5)
print('Imprimindo a lista na ordem da apresentação:>>>>',alunos,'.')
print('___________________________________________________________')