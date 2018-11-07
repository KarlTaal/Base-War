import pygame
import random

pygame.init()

clock = pygame.time.Clock()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
white = (255, 255, 255)
black = (0, 0, 0)

liikumis_kiirus = 2

X_kordinaat_A = 0
Y_kordinaat_A = 400

X_kordinaat_B = 800 - 30
Y_kordinaat_B = 400

gameExit = False


class Block_A(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


    def update(self):
        if self.rect.x > display_width - 30:
            self.rect.x += 0
        else:
            self.rect.x += liikumis_kiirus


def blokk_a(x_kordinaat, y_kordinaat):
    block = Block_A(black, 30, 30)

    block.rect.x = x_kordinaat
    block.rect.y = y_kordinaat

    # Add the block to the list of objects
    A_sprites.add(block)


class Block_B(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


    def update(self):
        if self.rect.x < 0:
            self.rect.x += 0
        else:
            self.rect.x -= liikumis_kiirus

def blokk_b(x_kordinaat, y_kordinaat):
    block = Block_B(black, 30, 30)

    block.rect.x = x_kordinaat
    block.rect.y = y_kordinaat

    # Add the block to the list of objects
    B_sprites.add(block)


# This is a list of every sprite.
A_sprites = pygame.sprite.Group()
B_sprites = pygame.sprite.Group()




def kokkupuude():
    # kustutab kokkupuutel
    blocks_hit_list = pygame.sprite.groupcollide(A_sprites, B_sprites, False, False, collided=None)
    #kustutab vabalt valitud blokki
    for i in blocks_hit_list:
        suvaline = random.randint(0,2)
        if suvaline == 0:
            A_sprites.remove(i)
        elif suvaline == 1:
            B_sprites.remove(blocks_hit_list[i])

while not gameExit:

    kokkupuude()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                blokk_a(X_kordinaat_A,Y_kordinaat_A)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                blokk_b(X_kordinaat_B,Y_kordinaat_B)

    gameDisplay.fill(white)
    # Calls update() method on every sprite in the list
    A_sprites.update()
    B_sprites.update()
    A_sprites.draw(gameDisplay)
    B_sprites.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
