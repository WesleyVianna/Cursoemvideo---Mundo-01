'''
Desafio 006
Crie um algoritmo que leia um número e mostre 
o seu dobro, triplo e raiz quadrada.
'''

numero = int(input('Digite um número inteiro: '))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)

print('O dobro de {} é de {}.'.format(numero, dobro))
print('O triplo de {} é de {}.'.format(numero, triplo))
print('A raiz quadrada de {} é {:.2f}.'.format(numero, raiz_quadrada))