import pygame
import time, random, colorsys, math
from pygame.math import Vector2
from bomba import Bomba
from dinheiro import Dinheiro
from explosao import Explosao
from fundo import Fundo
from jogador import Jogador
from funcoes import clip, checacolisoes

class TelaJogo:
    def __init__(self):
        self.window = pygame.display.set_mode((640, 480))
        self.fonte = pygame.fontFont(pygame.font.get_default_font(), 100)
        self.fonteprincipal = pygame.font.Font(pygame.font.get_default_font(), 30)
        self.fontepequena = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.formatentenovamente = pygame.image.load('assets/img/botaoforma.png')

        self.assets = {
            'dinheirosom': pygame.mixer.Sound('assets/snd/moneysound.mp3'),
            'explosaosom': pygame.mixer.Sound('assets/snd/explosao.mp3'),
        }

        self.rotacao = -4.2


        self.jogador = Jogador()
        self.dinheiros = []
        self.bombas = []

    def process_event(self, event)
        for i in range(15):
            self.dinheiros.append(Dinheiro())

        for i in range(6):
            self.bombas.append(Bomba())

        for dinheiro in self.dineiros:
            dinheiro.posicao.xy = random.randrange(0, self.window.get_width() - self.jogador.flipatual.get_width()), self.dinheiros.index(dinheiro)*-200 - self.jogador.posicao.y

        for bomba in self.bombas:
            bomba.posicao.xy = random.randrange(0, self.window.get_width() - self.jogador.flipatual.get_width()), self.bombas.index(bomba)*-200 - self.jogador.posicao.y

        self.pf = [Fundo(), Fundo(), Fundo()]

        self.contadordinheiro = 0
        self.alturainicial = self.jogador.posicao.y
        self.altura = 0
        self.vida = 100
        self.alturapulo = 3
        self.multiplicador = 5
        self.morto = False
        self.inverte = False

