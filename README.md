# Riqueza Geracional

Este é um projeto de um jogo desenvolvido por Gustavo Valente e Thais Silveira na disciplina Developer Life do semestre do curso de Ciência da Computação do Insper. O jogo foi desenvolvido em Python, utilizando a biblioteca [PyGame]([https://docs.python.org/3/library/curses.html](https://www.pygame.org/news)).

## Descrição do jogo

O roguelike desenvolvido consiste em um jogo de exploração de um calabouço, onde o jogador controla um personagem e deve derrotar os monstros e coletar tesouros.

O jogo apresenta alguns elementos característicos de roguelikes, como morte permanente (permadeath) e combates baseados em turnos.

O jogo desenvolvido consiste em um estilo flappy bird, em que o jogador inverte sua direção quando bate em uma das paredes, e também pode inverter a direção manualmente.

O objetivo é passar o máximo de tempo possível vivo, desviando de obstáculos, e coletando sacos de dinheiro para manter a barra de stamina enquanto pode usar esse dinheiro para fazer upgrades.

## Como jogar

Para jogar, é necessário ter o Python 3 instalado na máquina. Além disso, se você estiver no Windows, consulte o [guia abaixo](#jogando-no-windows) para mais informações.

Após instalar a biblioteca, clone este repositório e execute o arquivo `jogo.py`, dentro da pasta `src`, que está dentro da pasta `assets`. O jogo será aberto em uma janela e pode ser jogado com as seguintes teclas:

- **Pulo**: tecla "espaço"
- **Mudar a direção**: tecla "Q"
- **Fazer upgrades**: teclas "1", "2" e "3"

### Jogando no Windows

Para jogar, precisamos instalar a biblioteca `pygame`, utilizando o gerenciador de pacotes pip. Para isso, abra o terminal e execute o seguinte comando:

```bash
pip install pygame
```

Pronto! Agora você pode seguir os passos da seção ["Como jogar"](#como-jogar) para executar o jogo.

