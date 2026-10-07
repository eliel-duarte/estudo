import pygame

pygame.init()
tela = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Meu jogo")
relogio = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((30, 40, 50))
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()