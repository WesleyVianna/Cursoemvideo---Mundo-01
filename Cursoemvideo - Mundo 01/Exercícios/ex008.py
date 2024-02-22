'''
Desafio 008
Escreva um programa que leia um valor em metros e 
o exiba convertido em centímetro e milímetros.
'''

metros = float(input('Digite um valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(metros, centimetros, milimetros))
