import pygame 
import colorsys


class Fundo:
    def __init__(self):
        self.sprite = pygame.image.load('assets/img/fundo.png')
        self.sprite = pygame.transform.scale(self.sprite, (640, 480))
        self.posicao = 0
        self.cornormal = pygame.image.load('assets/img/fundo.png') 
        self.cornormal = pygame.transform.scale(self.cornormal, (640, 480))
    def definefundo(self, tint):  
        copia = self.cornormal.copy()
        cor = colorsys.hsv_to_rgb(tint,1,1)
        copia.fill((cor[0]*40, cor[1]*90, cor[2]*200), special_flags=pygame.BLEND_ADD)
        self.sprite = copia