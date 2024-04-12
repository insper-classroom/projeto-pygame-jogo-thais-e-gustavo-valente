import pygame
import random
import time, sys, colorsys, math
from pygame.math import Vector2

class Jogador:
    posicao = pygame.Vector2()
    posicao.xy = 295, 100
    aceleracao = 0.25
    velocidade = pygame.Vector2()
    velocidade.xy = 4.3, 0
    viradodireita = pygame.image.load('player.png')
    viradodireita = pygame.transform.scale(viradodireita, (100, 100))
    viradoesquerda = pygame.transform.flip(viradodireita, True, False)
    flipatual = viradoesquerda


class Dinheiro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.posicao = pygame.Vector2()
        self.posicao.xy
        self.spritedinheiro = pygame.image.load('money.png')
        self.spritedinheiro = pygame.transform.scale(spritedinheiro, (50, 80))

class Fundo:
    def __init__(self):
        self.spritefundo = pygame.image.load('bandeirafundo.png')
        self.posicao = 0
        self.cornormal = pygame.image.load('bandeirafundo.png')

    def defineSprite(self, corf):
        copia = self.cornormal.copy()
        cor = colorsys.hsv_to_rgb(tint, 1, 1)
        copia.fill((cor[0]*80, cor[1]*20, color[2]*70), special_flags = pygame.BLEND_ADD)
        self.spritefundo = copia
    
class Botao:
    def __init__(self):
        self.preco = 3
        self.nivel = 1
    
    spritebotao = pygame.image.load('button.png')
    
def clamp(valor, min, max):
    if valor < min:
        return min 
    
    if valor > max:
        return max

    return valor

def checkcolisoes(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    return (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height)



def main():
    pygame.init()

    #comeca a tela
    window = pygame.display.set_mode((640, 480), 0, 32)
    font = pygame.font.Font(pygame.font.get_default_font(), 100)
    fonte_pequena = pygame.font.Font(pygame.font.get_default_font(), 32)
    fonte_menor = pygame.font.Font(pygame.font.get_default_font(), 20)

    #carrega as imagens
    sompulo = pygame.mixer.Sound('tiro.mp3')
    somdinheiro = pygame.mixer.Sound('moneysound.mp3')
    musica = pygame.mixer.music.load('musicaestadoislamico.mp3')
    BRANCO = (255, 255, 255)

    rotacao = -5

    jogador = Jogador()
    dinheiros = []
    botoes = []

    #adicionando dinheiros na tela
    for i in range(5):
        dinheiros.append(Dinheiro())

    for dinheiro in dinheiros:
        dinheiro.posicao.xy = random.randrange(0, window.get_width() - dinheiro.spritedinheiro.get_width()), dinheiros.index(dinheiro)*-150 - jogador.posicao.y

    #criando a lista de fundos q vai ficar descendo

    pf = [Fundo(), Fundo(), Fundo()]

    contadordinheiro = 0
    alturainicial = jogador.posicao.y
    altura = 0
    vida = 100
    forcapulo = 3
    multiplicadordinheiro = 5

    fps = 60
    last_updated = time.time()
    planodefundostart = pygame.image.load('planodefundostart.png')
    botaotentenovamente = pygame.font.Font(pygame.font.get_default_font(), 20)
    botaotentenovamente = botaotentenovamente.render('Tente novamente', True, (0, 0, 0))

    #loop da tela de titulo
    while True:
        pygame.mixer.music.play()
        mx, my = pygame.mouse.get_pos()

        deltat = time.time() - last_updated
        deltat *= 60
        last_updated = time.time()

        clicou = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicou = True

            if event.type == pygame.QUIT:
                pygame.quit()



        if (clicou and checkCollisions(mx, my, 3, 3, window.get_width() / 2 - botaotentenovamente.get_width() / 2, 288, botaotentenovamente.get_width(), botaotentenovamente.get_height())):
            clicou = False
            break

        window.fill(BRANCO)
        window.blit(planodefundostart, (0, 0))
        comecar = fonte_pequena.render('Clique aqui para começar', True, (0, 0, 0))
        window.blit(comecar, (window.get_width() / 2 - comecar.get_height() / 2, 290))

        pygame.display.update()

        pygame.time.delay()

    
    #loop do jogoo em si

    while True:

        deltat = time.time() - last_time
        deltat *= 60
        last_updated = time.time()

        mx, my = pygame.mouse.get_pos()

        pulando = False
        clicou = False
        morto = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == 1:
                pulando = True
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicou = True
            
            if clicou and my < window.get_height() - 90:
                pulando = True

            if event.type == QUIT:
                pygame.quit()

        
        camerafora = -jogador.position.y + window.get_height()/2 - jogador.flipatual.get_size()[1]/2

        window.fill(BRANCO)
        for x in pf:
            x.defineSprite(((jogaodr.posicao.y/50) % 100) / 100)
            window.blit(x.spritefundo, (0, x.posicao))

        cor = colorsys.hsv_to_rgb(((jogador.posicao.y / 2) % 100) / 100, 0.2, 0.5)
        marcadoraltura = font.render(str(altura), True, (0, 0, 255))
        window.blit(marcadoraltura, (window.get_width()/2 - marcadoraltura.get_width()/2, camerafora + round((jogador.position.y - alturainicial)/window.get_height())*window.get_height() + jogador.flipatual.get_height() - 40))

        for dinheiro in dinheiros:
            window.blit(dinheiro.spritedinheiro, (dinheiro.posicao.x, dinheiro.posicao.y + camerafora))

        window.blit(pygame.transform.rotate(player.flipatual, clamp(jogador.velocidade.y, -10, 5)*rotacao), (jogador.posicao.x, jogador.posicao.y + camerafora))
        pygame.draw.rect(window, (62, 125, 82), (20, 440, 150*(vida/100), 25))

        mostrarcontador = fonte_pequena.render('$' + str(contadordinheiro).zfill(5), True, (0, 0, 0))
        window.blit(mostrarcontador, (67, 394))

        if morto:
            window.blit(botaotentenovamente, (4, 4))
            mensagemmorto = fonte_pequena('Tente novamente', True, (0, 0, 0))
            window.blit(mensagemmorto, (24, 8))

        altura = round(-(jogador.posicao.y - alturainicial) / window.get_height())

        jogador.posicao.x += jogador.velocidade.x*delat 
        if jogador.flipatual.get_size()[0] + jogador.posicao.x > 640:
            jogador.velocidade.x = -abs(jogador.velocidade.x)
            jogaodr.flipatual = jogador.viradodireita
            rotacao = 5

        if jogador.posicao.x < 0:
            jogador.velocidade.x = abs(jogador.velocidade.x)
            jogador.flipatual = jogador.viradoesquerda
            rotacao = -5
        
        if pulando and not morto:
            jogador.velocidade.y = -forcapulo
            pygame.mixer.Sound(sompulo)

        jogador.posicao.y += jogador.velocidade.y*deltat
        jogador.velocidade.y = clamp(jogador.velocidade.y + jogador.aceleracao*dt, -100000000, 50)
            






