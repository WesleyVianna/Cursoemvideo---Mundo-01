'''
Desafio 028
Escreva um programa que faça um computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolheido pelo computador. 
O programa deverá escrever na tela se o usuário vendeu ou perdeu.
'''

from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)

if jogador == computador:
  print('PARABÉNS! Você conseguiu me vencer!')
else:
  print('GANHEI! Eu pensei um número {} e não no número {}'.format(computador, jogador))