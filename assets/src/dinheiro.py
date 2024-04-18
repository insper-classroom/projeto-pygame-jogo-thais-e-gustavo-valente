import pygame

class Dinheiro(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.spritedinheiro = pygame.image.load('assets/img/money.png')
        self.spritedinheiro = pygame.transform.scale(self.spritedinheiro, (50, 80))
        self.posicao = pygame.Vector2()
        self.posicao.xy