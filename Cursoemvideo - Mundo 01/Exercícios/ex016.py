'''
Desafio 016
Crie um programa que leia um número Real qualquer pelo teclado e 
mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte 6 inteira
'''

#Primeira forma de fazer com import math (trunc)
'''from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num))) '''

# Segunda forma de fazer

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))