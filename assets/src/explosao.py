import pygame

class Explosao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagens = []
        for n in range(9):
            img = pygame.image.load(f'assets/img/regularExplosion0{str (n)}.png')
            img = pygame.transform.scale(img, (320, 480))
            self.imagens.append(img)

        self.indice = 0
        self.image = self.imagens[self.indice]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.contador = 0
    
    def update(self):
        velocidade_explosao = 4

        self.contador += 1

        if self.contador >= velocidade_explosao:
            self.contador = 0
            self.indice = 1
            self.image = self.imagens[self.indice]

        if self.indice >= len(self.imagens) and self.contador >= velocidade_explosao:
            self.kill()