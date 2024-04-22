import pygame

class Bomba(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posicao = pygame.Vector2()
        self.posicao.xy
        self.spritebomba = pygame.image.load('assets/img/bomba.png')
        self.spritebomba = pygame.transform.scale(self.spritebomba, (30, 100))