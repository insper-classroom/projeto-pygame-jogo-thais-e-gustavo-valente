import pygame

class Botao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.preco = 3
        self.nivel = 1

    botaoforma = pygame.image.load('assets/img/botaoforma.png')
    botaoforma = pygame.transform.scale(botaoforma, (80, 50)) 