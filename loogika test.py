import pygame

pygame.init()

clock = pygame.time.Clock()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
white = (255, 255, 255)
black = (0, 0, 0)

X_kordinaat = 0
Y_kordinaat = 400

gameExit = False

while not gameExit:
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    X_kordinaat += 1

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [X_kordinaat, Y_kordinaat, 30, 30])
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
