nome = str(input('Qual é o seu nome? '))

if nome == 'Wesley': # if é o Se (se isso for verdadeiro, faça isso)
  print('Que nome lindo que você tem!')
else: # else é o senão (caso o if não for verdadeiro, ele fará isso)
  print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))