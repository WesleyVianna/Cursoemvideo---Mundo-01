'''
Desafio 024
Crie um programa que leia o noem de uma cidade e diga se ela começa com o nome "SANTO".
'''

cidade = str(input('Em que cidade você nasceu: ')).strip()

print(cidade[:5].upper() == 'Santo')