import pygame
import time, random, colorsys, math
from pygame.math import Vector2
from bomba import Bomba
from dinheiro import Dinheiro
from explosao import Explosao
from fundo import Fundo
from jogador import Jogador
from funcoes import clip, checacolisoes


def run():
    pygame.init()
    window=pygame.display.set_mode((640,480))
    font = pygame.font.Font(pygame.font.get_default_font(), 100)
    fonteprincipal = pygame.font.Font(pygame.font.get_default_font(), 30)
    fontepequena = pygame.font.Font(pygame.font.get_default_font(), 20)
    formatentenovamente = pygame.image.load('assets/img/botaoforma.png')
    # musicaestadoislamico = pygame.mixer.music.load('musicaestadoislamico.mp3')

    assets = {
       'dinheirosom': pygame.mixer.Sound('assets/snd/moneysound.mp3'),
       'explosaosom': pygame.mixer.Sound('assets/snd/explosao.mp3'),
    }

    rotacao = -4.2

    jogador = Jogador()
    dinheiros = []
    bombas = []
    
    for i in range(15): 
        dinheiros.append(Dinheiro())

    
    for i in range(6):
        bombas.append(Bomba())

    for dinheiro in dinheiros:
        dinheiro.posicao.xy = random.randrange(0, window.get_width() - jogador.flipatual.get_width()), dinheiros.index(dinheiro)*-200 - jogador.posicao.y
    
    for bomba in bombas:
        bomba.posicao.xy = random.randrange(0, window.get_width() - jogador.flipatual.get_width()), bombas.index(bomba)*-200 - jogador.posicao.y

    pf = [Fundo(), Fundo(), Fundo()]
   
    contadordinheiro = 0
    alturainicial = jogador.posicao.y
    altura = 0
    vida = 100
    alturapulo = 3
    multiplicador = 5
    morto = False
    inverte = False
    
    fps = 60
    last_updated = time.time()
    fonte = pygame.font.Font(pygame.font.get_default_font(), 100)
    fonte_pequena = pygame.font.Font(pygame.font.get_default_font(), 30)
    fonte_menor = pygame.font.Font(pygame.font.get_default_font(), 20)

    moneysound = pygame.mixer.Sound('assets/snd/moneysound.mp3')
    planodefundotit = pygame.image.load('assets/img/planodefundostart.png')
    botaotentenovamente = pygame.image.load('assets/img/botaoforma.png')
    tentenovamente = fonte_menor.render('Recomeçar', True, (0, 0, 0))
    
    while True:
        # pygame.mixer.music.play()
        deltat = time.time() - last_updated
        deltat *= 60
        last_updated = time.time()

        mx, my = pygame.mouse.get_pos()
        clicou = False
        teclas = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicou = True

            if event.type == pygame.QUIT:
                pygame.quit()
        
        if (clicou and checacolisoes(mx, my, 3, 3, window.get_width() / 2 - botaotentenovamente.get_width() / 2, 288, botaotentenovamente.get_width(), botaotentenovamente.get_height())):
            clicou = False
            break
        window.fill((255, 255, 255))
        window.blit(planodefundotit, (0, 0))
        comece = fonte_pequena.render('CLIQUE AQUI PARA COMEÇAR', True, (0, 0, 0))
        window.blit(comece, (window.get_width()/2 - comece.get_width()/2, 290))
         
        pygame.display.update()


    while True:
        
        deltat = time.time() - last_updated
        deltat *= 60
        last_updated = time.time()
        mx,my = pygame.mouse.get_pos()

        pulando = False
        clicou = False
        inverte = False
        camerafora = -jogador.posicao.y + window.get_height()/2 - jogador.flipatual.get_size()[1]/2
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                pulando = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicou = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                inverte = True
  
            if clicou and my < window.get_height() - 90:
                pulando = True
            

            if event.type == pygame.QUIT:
                pygame.quit()
        
        window.fill((255, 255, 255))
        
        for x in pf:
            x.definefundo(((jogador.posicao.y/50) % 100) / 100)
            window.blit(x.sprite, (0, x.posicao))
        
        mostracontador = fonteprincipal.render('$' + str(contadordinheiro).zfill(5), True, (0, 0, 0))
        window.blit(mostracontador, (30, 400))

        for dinheiro in dinheiros:
            window.blit(dinheiro.spritedinheiro, (dinheiro.posicao.x, dinheiro.posicao.y + camerafora))

        for bomba in bombas:
            window.blit(bomba.spritebomba, (bomba.posicao.x, bomba.posicao.y + camerafora))


        cor = colorsys.hsv_to_rgb(((jogador.posicao.y/2) % 100) / 100,0.2,0.5)
        marcadoraltura = font.render(str(altura), True, (168, 168, 168))
        window.blit(marcadoraltura, (window.get_width()/2 - marcadoraltura.get_width()/2, camerafora + round((jogador.posicao.y - alturainicial)/window.get_height())*window.get_height() + jogador.flipatual.get_height() - 40))
        
        window.blit(pygame.transform.rotate (jogador.flipatual, clip(jogador.velocidade.y, -10, 5)*rotacao), (jogador.posicao.x,jogador.posicao.y + camerafora))
        pygame.draw.rect(window,(62, 125, 82),(21,437,150*(vida/100),25))
            

        vida -= 0.5*deltat
        if vida <= 0 and not morto:
            morto = True

        if morto:
            deltat = time.time() - last_updated
            deltat *= 60
            last_updated = time.time()

            mx, my = pygame.mouse.get_pos()
            clicou = False
            teclas = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clicou = True

                if event.type == pygame.QUIT:
                    pygame.quit()
        
            if teclas[pygame.K_RETURN]:
                clicou = False
                morto = False
        
            

            window.fill((0,0,0))
            textotentenovamente = fonte_menor.render('Recomeçar', True, (255, 255, 255))
            window.blit(textotentenovamente, (270, 240))

            pygame.display.update()


        altura = round(-(jogador.posicao.y - alturainicial)/window.get_height())
 
        jogador.posicao.x += jogador.velocidade.x*deltat
        if inverte and jogador.velocidade.x > 0:
            jogador.velocidade.x = -abs(jogador.velocidade.x)
            jogador.flipatual = jogador.flipesquerda
            rotacao = 4.2
        elif inverte and jogador.velocidade.x < 0:
            jogador.velocidade.x = abs(jogador.velocidade.x)
            jogador.flipatual = jogador.flipdireita
            rotacao = -4.2

        if jogador.posicao.x + jogador.flipatual.get_size()[0] > 640:
            jogador.velocidade.x = -abs(jogador.velocidade.x)
            jogador.flipatual = jogador.flipesquerda
            rotacao = 4.2

        if jogador.posicao.x < 0:
            jogador.velocidade.x = abs(jogador.velocidade.x)
            jogador.flipatual = jogador.flipdireita
            rotacao = -4.2  

        if pulando and not morto:
            jogador.velocidade.y = -alturapulo

        jogador.posicao.y += jogador.velocidade.y*deltat
        jogador.velocidade.y = clip(jogador.velocidade.y + jogador.acceleration*deltat, -99999999999, 50)
        
        pf[0].posicao = camerafora + round(jogador.posicao.y/window.get_height())*window.get_height()
        pf[1].posicao = pf[0].posicao + window.get_height() 
        pf[2].posicao = pf[0].posicao - window.get_height()

        for dinheiro in dinheiros:
            if camerafora + dinheiro.posicao.y + 90 > window.get_height():
                dinheiro.posicao.y -= window.get_height()*2
                dinheiro.posicao.x = random.randrange(0, window.get_width() - dinheiro.spritedinheiro.get_width())
            
            if not morto:
                if (checacolisoes(jogador.posicao.x, jogador.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height(), dinheiro.posicao.x, dinheiro.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height())):
                    morto = False
                    pygame.mixer.Sound.play(assets['dinheirosom'])
                    contadordinheiro += 1
                    vida +=20
                    if vida > 100:
                        vida = 100
                    dinheiro.posicao.y -= window.get_height() - random.randrange(0, 200)
                    dinheiro.posicao.x = random.randrange(0, window.get_width() - jogador.flipatual.get_width())


        for bomba in bombas:
            if camerafora + bomba.posicao.y + 60 > window.get_height():
                bomba.posicao.y -= window.get_height()*2
                bomba.posicao.x = random.randrange(0, window.get_width() - bomba.spritebomba.get_width())
            if (checacolisoes(jogador.posicao.x, jogador.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height(), bomba.posicao.x, bomba.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height())):
                vida -= 20
                pygame.mixer.Sound.play(assets['explosaosom'])
                exp = Explosao(bomba.posicao.x, bomba.posicao.y)
                window.blit(exp.image, (0, 0)) 

                bomba.posicao.y -= window.get_height() - random.randrange(0, 200)
                bomba.posicao.x = random.randrange(0, window.get_width() - jogador.flipatual.get_width())
            if bomba.posicao.y > window.get_height() or bomba.posicao.x > window.get_width():
                bomba.posicao.y -= window.get_height() - random.randrange(0, 200)
                bomba.posicao.x = random.randrange(0, window.get_width() - jogador.flipatual.get_width())
        
        tecla = pygame.key.get_pressed()
        if morto and tecla[pygame.K_RETURN]:
            deltat = time.time() - last_updated
            deltat *= 60
            last_updated = time.time()

            vida = 100
            contadordinheiro = 0
            altura = 0
            alturapulo = 2.5
            multiplicadordinheiro = 3
            jogador.velocidade.xy = 2.5, 0
            jogador.posicao.xy = 300, 100
            jogador.flipatual = jogador.flipesquerda
            bombas = []
            dinheiros = []


            for i in range(5): 
                dinheiros.append(Dinheiro())

            for i in range(9):
                bombas.append(Bomba())

            for dinheiro in dinheiros:
                dinheiro.posicao.xy = random.randrange(0, window.get_width() - jogador.flipatual.get_width()), dinheiros.index(dinheiro)*-200 - jogador.posicao.y
            
            for bomba in bombas:
                 bomba.posicao.y = random.randrange(0, window.get_width() - jogador.flipatual.get_width())
                 bomba.posicao.x = bombas.index(bomba)*-200 - jogador.posicao.y

            for bomba in bombas:
                if (checacolisoes(jogador.posicao.x, jogador.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height(), bomba.posicao.x, bomba.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height())):
                    vida -= 20
                    pygame.mixer.Sound.play(assets['explosaosom'])
                    bomba.posicao.y -= window.get_height() - random.randrange(0, 200)
                    bomba.posicao.x = random.randrange(0, window.get_width() - jogador.flipatual.get_width())
                elif bomba.posicao.y > window.get_height() or bomba.posicao.x > window.get_width():
                    bomba.posicao.y -= window.get_height() - random.randrange(0, 200)
                    bomba.posicao.x = random.randrange(0, window.get_width() - jogador.flipatual.get_width())
            


            morto = False         

        

        
        pygame.display.update()


if __name__ == "__main__":
    run()
