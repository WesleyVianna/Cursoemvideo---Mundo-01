'''
Desafio 005
Faça um programa que leia um número inteiro e mostre 
na tela o seu sucessor e seu antecessor.
'''
# Utilizando 3 variáveis (numero, antecessor e sucessor)
numero = int(input('Digite um número inteiro: '))

antecessor = numero - 1
sucessor = numero + 1

print('Analisando o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(numero, antecessor, sucessor))

# Utilizando 1 variável (numero)
'''
numero = int(input('Digite um número inteiro'))

print('Analisando o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(numero, (numero - 1), (numero + 1)))
'''