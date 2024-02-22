'''
Desafio 027
Faça um programa que leia o noem completo de uma pessoa, 
mostrando em seguinda o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

nome = str(input('Digite seu nome completo: ')).strip()

nome_completo = nome.split()

print('Muito prazer te conhecer!!')
print('Seu primeiro nome é {}.'.format(nome_completo[0]))
print('Seu último nome é {}.'.format(nome_completo[len(nome_completo) - 1]))