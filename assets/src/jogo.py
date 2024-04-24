import pygame
import time, random, colorsys, math
from pygame.math import Vector2
from bomba import Bomba
from dinheiro import Dinheiro
from explosao import Explosao
from fundo import Fundo
from jogador import Jogador
from botao import Botao
from funcoes import clip, checacolisoes, pegamaiorelemento, adicionanoarquivo


def run():
    pygame.init()
    window=pygame.display.set_mode((640,480))
    pygame.display.set_caption('Riqueza Geracional')
    font = pygame.font.Font(pygame.font.get_default_font(), 100)
    fonteprincipal = pygame.font.Font(pygame.font.get_default_font(), 30)
    fontepequena = pygame.font.Font(pygame.font.get_default_font(), 20)
    formatentenovamente = pygame.image.load('assets/img/botaoforma.png')
    trilhasonora = pygame.mixer.music.load('assets/snd/Puzzle Piece - Lorne Balfe copy.mp3')
    pygame.mixer.music.play()

    assets = {
       'dinheirosom': pygame.mixer.Sound('assets/snd/moneysound.mp3'),
       'explosaosom': pygame.mixer.Sound('assets/snd/explosao.mp3'),
    }

    rotacao = -4.2

    jogador = Jogador()
    dinheiros = []
    bombas = []
    botoes = []

    for i in range(3):
        botoes.append(Botao()) 

    botoes[0].preco = 5
    botoes[1].preco = 5
    botoes[2].preco = 30

    botaopulo =  fontepequena.render('+ 1.5 pulo', True, (255, 255, 255))
    botaovel = fontepequena.render('+ 1.5 vel', True, (255, 255, 255))
    botaodin = fontepequena.render('+ 1.5 din', True, (255, 255, 255))

    imagens_botoes = [
        botaopulo,
        botaovel,
        botaodin
    ]
    
    for i in range(12): 
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
    planodefundotit = pygame.image.load('assets/img/Screen Shot 2024-04-24 at 15.29.08.png')
    planodefundotit = pygame.transform.scale(planodefundotit, (window.get_width() - 40, window.get_height() - 30))
    botaotentenovamente = pygame.image.load('assets/img/botaoforma.png')

    recordearq = "records.txt"
    
    tentenovamente = fonte_menor.render('Pressione ENTER para recomeçar', True, (0, 0, 0))
    
    while True:
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
            break

        window.fill((255, 255, 255))
        window.blit(planodefundotit, (0, 0))
        comece = fonte_pequena.render('APERTE "ENTER" PARA COMEÇAR', True, (0, 0, 0))
        window.blit(comece, (window.get_width()/2 - comece.get_width()/2, window.get_height() - comece.get_height()))
         
        pygame.display.update()

    trilhasonora = pygame.mixer.music.load('assets/snd/Puzzle Piece - Lorne Balfe copy.mp3')
    pygame.mixer.music.play()
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
        
        cor = colorsys.hsv_to_rgb(((jogador.posicao.y/2) % 100) / 100,0.2,0.5)        
        window.fill((0, 0, 0))
        
        for x in pf:
            x.definefundo(((jogador.posicao.y/50) % 100) / 100)
            window.blit(x.sprite, (0, x.posicao))
        
        mostracontador = fonteprincipal.render('$' + str(contadordinheiro).zfill(5), True, (168, 168, 168))
        window.blit(mostracontador, (30, 400))

        for dinheiro in dinheiros:
            window.blit(dinheiro.spritedinheiro, (dinheiro.posicao.x, dinheiro.posicao.y + camerafora))

        for bomba in bombas:
            window.blit(bomba.spritebomba, (bomba.posicao.x, bomba.posicao.y + camerafora))
        
        for botao in botoes:
            teclas = pygame.key.get_pressed()
            if not morto:
                if teclas[pygame.K_1]:
                    if contadordinheiro >= botao.preco:
                        botao.nivel += 1
                        contadordinheiro -= botao.preco
                        botao.preco = round(botao.preco*2.5)
                        if botoes.index == 0:
                            alturapulo *= 1.5 

                if teclas[pygame.K_2]:
                    if contadordinheiro >= botao.preco:
                        botao.nivel += 1
                        contadordinheiro -= botao.preco
                        botao.preco = round(botao.preco*2.5)
                        jogador.velocidade.x *= 1.5


                if teclas[pygame.K_3]:
                    if contadordinheiro >= botao.preco:
                        botao.nivel += 1
                        contadordinheiro -= botao.preco
                        botao.preco = round(botao.preco*2.5)
                        multiplicadordinheiro *= 1.5

        cor = colorsys.hsv_to_rgb(((jogador.posicao.y/2) % 100) / 100,0.2,0.5)
        objetos_astronomicos = {
            (0, 10): 'Terra',
            (10, 15): 'Marte',
            (15, 25): 'Júpiter',
            (25, 40): 'Saturno',
            (40, 55): 'Urano',
            (55, 70): 'Netuno',
            (70, 100): 'Galáxia de Andrômeda',
            (100, float('inf')): 'Messier 31'  
        }

        for intervalo, objeto in objetos_astronomicos.items():
            if intervalo[0] <= altura < intervalo[1]:
                marcadoraltura = fonte_pequena.render(f'Distância: {altura} em:{objeto}', True, (168, 168, 168))
                break  

        window.blit(marcadoraltura, (window.get_width()/2 - marcadoraltura.get_width()/2, camerafora + round((jogador.posicao.y - alturainicial)/window.get_height())*window.get_height() + jogador.flipatual.get_height() - 40))
        novorecord = altura
        appendscore = adicionanoarquivo(recordearq, novorecord)

        maior = pegamaiorelemento(recordearq)

        i = 0
        for botao in botoes:
            window.blit(imagens_botoes[i], (210 + (botoes.index(botao)*125), 410)) 
            nivelbotao = fonte_menor.render('Nv' + str(botao.nivel), True, (200, 200, 200))
            window.blit(nivelbotao, (215 + (botoes.index(botao)*125), 445))
            mostrapreco = fonte_menor.render('$' + str(botao.preco), True, (255, 255, 255))
            window.blit(mostrapreco, (265 + (botoes.index(botao)*125), 445)) 
            i += 1

        maiorrecorde = fonte_pequena.render('Maior Distância: ' + str(maior), True, (168, 168, 168))
        window.blit(maiorrecorde, (window.get_width() / 2 - maiorrecorde.get_width() / 2 , 5))

        window.blit(pygame.transform.rotate (jogador.flipatual, clip(jogador.velocidade.y, -10, 5)*rotacao), (jogador.posicao.x,jogador.posicao.y + camerafora))
        pygame.draw.rect(window,(62, 125, 82),(21,437,150*(vida/100),25))
            

        vida -= 0.25*deltat
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

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    clicou = True

                if event.type == pygame.QUIT:
                    pygame.quit()
        
            if teclas[pygame.K_RETURN]:
                clicou = False
                morto = False        
            

            window.fill((0,0,0))
            planodefundofin = pygame.image.load('assets/img/Screen Shot 2024-04-24 at 15.31.10.png')
            planodefundofin = pygame.transform.scale(planodefundofin, (window.get_width() - 20, window.get_height() - 30))
            window.blit(planodefundofin, (0, 0)) 

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
                    multiplicadordinheiro = 1
                    pygame.mixer.Sound.play(assets['dinheirosom'])
                    contadordinheiro += 1*1
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
                window.blit(exp.image, (150, 0)) 

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
            jogador.flipatual = jogador.flipdireita
            bombas = []
            dinheiros = []
            botoes = []

            for i in range(3):
                botoes.append(Botao())

            botoes[0].preco = 5
            botoes[1].preco = 5
            botoes[2].preco = 30

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