'''
Desafio 021
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

#Com o uso do ChatGPT

import pygame
import os
import sys

# Inicializa o Pygame
pygame.init()

# Inicializa o mixer
pygame.mixer.init()

# Imprime o diretório de trabalho atual
print("Diretório de trabalho atual:", os.getcwd())

# Tenta carregar o arquivo de música
try:
    pygame.mixer.music.load('C:\\Users\\Usuario\\Desktop\\Cursoemvideo - Mundo 01\\Exercícios\\LoverWhy.mp3')
    print("Arquivo de música carregado com sucesso.")
except pygame.error as e:
    print("Erro ao carregar o arquivo de música:", e)
    sys.exit()

# Tenta reproduzir a música
try:
    pygame.mixer.music.play()

    # Aguarda até que a música termine
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # ajuste conforme necessário

    print("A música terminou de tocar.")

except pygame.error as e:
    print("Erro ao reproduzir a música:", e)
finally:
    pygame.quit()

'''
import pygame

pygame.init()
pygame.mixer.music.load('C:\\Users\\Usuario\\Desktop\\Cursoemvideo - Mundo 01\\Exercícios\\ex021.mp3')
# pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''























