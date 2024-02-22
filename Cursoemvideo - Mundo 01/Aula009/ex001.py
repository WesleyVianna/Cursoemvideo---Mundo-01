frase = 'Curso em Vídeo Python'

print(frase[3]) # retornará a 3ª letra da frase (lembrando que o C é o número 0)
print(frase[1:13]) # retornará "urso em Víde" (que é quando começa do caractere 1 até o caractere 13)
print(frase[:13]) # retornará "Curso em Víde" (que é do começo até a quantidade de caractere que foi pedido)
print(frase[1:15:2]) # retornará "us mVdo" (que é quando começa do caractere 1 e percorre de 2 em 2)
print(frase[::2]) # retornará "Croe íe yhn" (que é quando vai de 2 em 2)
print()

# usando apenas o objeto 'frase'
print(frase.count('o')) # retornará número 3 (que é a quantidade de "o" que tem na frase)
print(frase.upper().count('o')) # o upper é para ignorar se for maiúsculo ou minúsculo
print(len(frase)) # o len conta a quantidade de caracteres tem, incluindo os espaços
print(len(frase.strip())) # o strip remove os espaço indesejados
print(frase.replace('Python', 'Android')) # o replace irá trocar as palavras, sem o salvamento
frase = (frase.replace('Python', 'Android')) # nesse caso irá salvar 
print(frase)
print('Curso' in frase) # irá ver se a palavra 'Curso' está dentro da frase
print(frase.find('Vídeo')) # irá mostrar a posição da palavra na frase




#quando quer escrever algo na tela e seja muito grande utiliza
print()
print("""Escravos de Jó
Jogavam caxangá
Tira, bota, deixa ficar
Guerreiros com guerreiros fazem zigue-zigue-zá
Guerreiros com guerreiros fazem zigue-zigue-zá.""")