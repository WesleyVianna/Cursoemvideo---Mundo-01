nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print('A sua média foi {:.1f}'.format(media))

'''
# forma mais tradicional/complexa
if media >= 6.0:
  print('Sua média foi boa! PARABÉNS!')
else:
  print('Sua média foi ruim! ESTUDE MAIS!') '''


# forma mais simplificada
print('PARABÉNS!' if media >= 6 else 'ESTUDE MAIS')