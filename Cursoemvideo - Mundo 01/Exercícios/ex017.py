'''
Desafio 017
Faça um programae que leia o comprimento do cateto oposto e do cateto adjacente de
um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

# Forma tradicional de achar hipotenusa
'''
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))'''


# Forma usando import
from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))