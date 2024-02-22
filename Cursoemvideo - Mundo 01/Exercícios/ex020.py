'''
Desafio 020
O mesmo professor do desafio anterior quer sortear a ordem de apresentação
de trabalhos dos alunos. Faça um programa que leia o nome 
dos quatros alunos e mostre a ordem sorteada.
'''

from random import shuffle

nome1 = str(input('Digite o nome do 1º aluno: '))
nome2 = str(input('Digite o nome do 2º aluno: '))
nome3 = str(input('Digite o nome do 3º aluno: '))
nome4 = str(input('Digite o nome do 4º aluno: '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem de apresentação será ')
print(lista)