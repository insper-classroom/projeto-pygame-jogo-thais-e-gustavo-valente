import pygame


class Jogador(pygame.sprite.Sprite):
        posicao = pygame.Vector2()
        posicao.xy = 295, 100
        velocidade = pygame.Vector2()
        velocidade.xy = 3, 0
        acceleration = 0.1
        flipdireita = pygame.image.load('assets/img/cr3-removebg-preview.png')
        flipdireita = pygame.transform.scale(flipdireita, (100, 100))
        flipdireita = pygame.transform.flip(flipdireita, True, False)
        flipesquerda = pygame.transform.flip(flipdireita, True, False)
        flipatual = flipdireita