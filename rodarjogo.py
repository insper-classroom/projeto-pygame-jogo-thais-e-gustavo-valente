from jogo import *

def main():
    pygame.init()

    #comeca a tela
    window = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(pygame.font.get_default_font(), 100)
    fonte_pequena = pygame.font.Font(pygame.font.get_default_font(), 32)
    fonte_menor = pygame.font.Font(pygame.font.get_default_font(), 20) 

    #carrega as imagens
    sompulo = pygame.mixer.Sound('tiro.mp3')
    somdinheiro = pygame.mixer.Sound('moneysound.mp3')
    explodindo = pygame.mixer.Sound('explosao.mp3')
    musica = pygame.mixer.music.load('musicaestadoislamico.mp3')
    BRANCO = (255, 255, 255)

    rotacao = -3.5

    jogador = Jogador()
    dinheiros = []
    bombas = []
    botoes = []

    #adicionando dinheiros na tela
    for i in range(5):
        dinheiros.append(Dinheiro())

    for i in range(7):
        bombas.append(Bomba())

    for dinheiro in dinheiros:
        dinheiro.posicao.xy = random.randrange(0, window.get_width() - dinheiro.spritedinheiro.get_width()), dinheiros.index(dinheiro)*-150 - jogador.posicao.y

    for bomba in bombas:
        bomba.posicao.xy = random.randrange(0, window.get_width() - bomba.spritebomba.get_width()), bombas.index(bomba)*-150 - jogador.posicao.y
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
    retrybutton = pygame.transform.scale(pygame.image.load('retry_button.png'), (215,40)) 
    botaotentenovamente = fonte_pequena.render('Recomeçar', True, (0, 0, 0))

    #loop da tela de titulo
    while True:
        # pygame.mixer.music.play()
        mx, my = pygame.mouse.get_pos()

        deltat = time.time() - last_updated
        deltat *= 60
        last_updated = time.time()

        clicou = False
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicou = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                clicou = True

            if event.type == pygame.QUIT:
                pygame.quit() 


        if (clicou and checkcolisoes(mx, my, 2, 2, window.get_width() / 2 - botaotentenovamente.get_width() / 2, 280, botaotentenovamente.get_width(), botaotentenovamente.get_height())):
            clicou = False
            break

        window.fill(BRANCO)
        window.blit(planodefundostart, (0, 0))
        comecar = fonte_pequena.render('Clique aqui para começar', True, (0, 0, 0))
        window.blit(comecar, (window.get_width() / 2 - comecar.get_height() / 2, 290))

        pygame.display.update()

        pygame.time.delay(10)

    
    #loop do jogoo em si

    while True:

        deltat = time.time() - last_updated
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

            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                clicou = True
            
            if clicou and my < window.get_height() - 90:
                pulando = True

            if event.type == pygame.QUIT:
                pygame.quit()

        
        camerafora = -jogador.posicao.y + window.get_height()/2 - jogador.flipatual.get_size()[1]/2

        window.fill(BRANCO)
        for x in pf:
            x.defineSprite(((jogador.posicao.y/50) % 100) / 100)
            window.blit(x.spritefundo, (0, x.posicao))

        cor = colorsys.hsv_to_rgb(((jogador.posicao.y / 2) % 100) / 100, 0.2, 0.5)
        marcadoraltura = font.render(str(altura), True, (0, 255, 190))
        window.blit(marcadoraltura, (window.get_width()/2 - marcadoraltura.get_width()/2, camerafora + round((jogador.posicao.y - alturainicial)/window.get_height())*window.get_height() + jogador.flipatual.get_height() - 40))

        mostrarcontador = fonte_pequena.render('$' + str(contadordinheiro).zfill(5), True, (0, 0, 0))
        window.blit(mostrarcontador, (67, 394))
        
        for dinheiro in dinheiros:
            window.blit(dinheiro.spritedinheiro, (dinheiro.posicao.x, dinheiro.posicao.y + camerafora))

        for bomba in bombas:
            window.blit(bomba.spritebomba, (bomba.posicao.x, bomba.posicao.y + camerafora))

        window.blit(pygame.transform.rotate(jogador.flipatual, clamp(jogador.velocidade.y, -10, 5)*rotacao), (jogador.posicao.x, jogador.posicao.y + camerafora))
        pygame.draw.rect(window, (62, 125, 82), (20, 440, 200*(vida/100), 25))

    
        vida -= 0.3*deltat
        if vida <= 0 and not morto:
            morto = True
            
        if morto:
            window.blit(retrybutton, (4, 4))
            morreu = fonte_pequena.render('Recomeçar', True, (0, 0, 0))
            window.blit(morreu, (24, 8)) 

        altura = round(-(jogador.posicao.y - alturainicial) / window.get_height())

        jogador.posicao.x += jogador.velocidade.x*deltat 
        if jogador.flipatual.get_size()[0] + jogador.posicao.x > 640:
            jogador.velocidade.x = -abs(jogador.velocidade.x)
            jogador.flipatual = jogador.viradodireita
            rotacao = 3.5

        if jogador.posicao.x < 0:
            jogador.velocidade.x = abs(jogador.velocidade.x)
            jogador.flipatual = jogador.viradoesquerda
            rotacao = -3.5
        
        if pulando and not morto:
            jogador.velocidade.y = -forcapulo
            pygame.mixer.Sound(sompulo)

        jogador.posicao.y += jogador.velocidade.y*deltat
        jogador.velocidade.y = clamp(jogador.velocidade.y + jogador.aceleracao*deltat, -100000000, 50)

        
        for dinheiro in dinheiros:
            if camerafora + dinheiro.posicao.y + 60 > window.get_height():
                dinheiro.posicao.y -= window.get_height()*2
                dinheiro.posicao.x = random.randrange(0, window.get_width() - dinheiro.spritedinheiro.get_width())
            if (checkcolisoes(jogador.posicao.x, jogador.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height(), dinheiro.posicao.x, dinheiro.posicao.y, dinheiro.spritedinheiro.get_width(), dinheiro.spritedinheiro.get_height())):
                morto = False
                contadordinheiro += 1
                vida = 100
                dinheiro.posicao.y -= window.get_height() - random.randrange(0, 200)
                dinheiro.posicao.x = random.randrange(0, window.get_width() - dinheiro.spritedinheiro.get_width())
                pygame.mixer.Sound.play(somdinheiro)

        for bomba in bombas:
            if camerafora + bomba.posicao.y + 60 > window.get_height():
                bomba.posicao.y =- window.get_height()*2
                bomba.posicao.x = random.randrange(0, window.get_width() - bomba.spritebomba.get_width())
            if (checkcolisoes(jogador.posicao.x, jogador.posicao.y, jogador.flipatual.get_width(), jogador.flipatual.get_height(), bomba.posicao.x, bomba.posicao.y, bomba.spritebomba.get_width(), bomba.spritebomba.get_height())):
                vida -= 20
                bomba.posicao.y -= window.get_height() - random.randrange(0, 200)
                bomba.posicao.x = random.randrange(0, window.get_width() - bomba.spritebomba.get_width())
                pygame.mixer.Sound.play(explodindo)


        if morto and clicou and checkcolisoes(mx, my, 3, 3, 4, 4, botaotentenovamente.get_width(), botaotentenovamente.get_height()):
            vida = 100
            contadordinheiro = 0
            altura = 0
            forcapulo = 3
            multiplicadordinheiro = 3
            jogador.velocidade.xy = 3, 0
            jogador.posicao.xy = 300, 100
            jogador.flipatual = jogador.viradoesquerda

            dinheiros = []

            for i in range(5):
                dinheiros.append(Dinheiro())
            for dinheiro in dinheiros:
                dinheiro.posicao.xy = random.randrange(0, window.get_width() - dinheiro.spritedinheiro.get_width()), dinheiros.index(dinheiro)*-200 - jogador.posicao.y
            
            morto = False

        
        pf[0].posicao = camerafora + round(jogador.posicao.y / window.get_height())*window.get_height()
        pf[1].posicao = pf[0].posicao + window.get_height()
        pf[2].posicao = pf[1].posicao - window.get_height()

        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    main()