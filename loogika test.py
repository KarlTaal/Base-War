import pygame
import random

pygame.init()

clock = pygame.time.Clock()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
white = (255, 255, 255)
black = (0, 0, 0)

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

    def reset_pos(self):
        self.rect.x = X_kordinaat_A
        self.rect.y = Y_kordinaat_A

    def update(self):
        if self.rect.x > display_width - 30:
            # self.reset_pos()
            self.rect.x += 0
        else:
            self.rect.x += 5


def blokk_a(x_kordinaat, y_kordinaat):
    block = Block_A(black, 30, 30)

    block.rect.x = x_kordinaat
    block.rect.y = y_kordinaat

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)


class Block_B(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.x = X_kordinaat_B
        self.rect.y = Y_kordinaat_B

    def update(self):
        if self.rect.x < 0:
            # self.reset_pos()
            self.rect.x += 0
        else:
            self.rect.x -= 5


def blokk_b(x_kordinaat, y_kordinaat):
    block = Block_B(black, 30, 30)

    block.rect.x = x_kordinaat
    block.rect.y = y_kordinaat

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)


# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

#blokk_a(X_kordinaat_A, Y_kordinaat_A)
#blokk_b(X_kordinaat_B,Y_kordinaat_B)


while not gameExit:
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
    all_sprites_list.update()
    all_sprites_list.draw(gameDisplay)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
