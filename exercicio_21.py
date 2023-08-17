# Aprendendo trabalhar com a biblioteca pygame
# Reproduzindo uma musica!

import pygame

pygame.mixer.init()
pygame.mixer.music.load('PPD.mp3')
pygame.mixer.music.play()

input()