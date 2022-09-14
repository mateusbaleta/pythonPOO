import pygame
import os
import random


# Constantes
TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_PASSARO = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
                  pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
                  pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Passaro:
    pass

class Chao:
    pass

class Cano:
    pass