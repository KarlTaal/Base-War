import os
import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 720, 480
BACKGROUND_COLOR = pygame.Color('black')
FPS = 60

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


mehikese_pildid = [pygame.image.load("images/mehike/mehike1.png"), pygame.image.load("images/mehike/mehike2.png"), pygame.image.load("images/mehike/mehike3.png"),\
pygame.image.load("images/mehike/mehike4.png"), pygame.image.load("images/mehike/mehike5.png"), pygame.image.load("images/mehike/mehike6.png"),\
pygame.image.load("images/mehike/mehike7.png"), pygame.image.load("images/mehike/mehike8.png")]
mehike_walkright = []
for mehike in mehikese_pildid:
    mehike_walkright.append(pygame.transform.scale(mehike, (int(200), int(300))))


class Player2(pygame.sprite.Sprite):

    def __init__(self, position, mehike_walkright):
        super(Player2, self).__init__()
        size = (32, 32)
        self.rect = pygame.Rect(position, size)
        self.images = mehike_walkright
        self.images_left = [pygame.transform.flip(image, True, False) for image in mehike_walkright]  # Flipping every image.
        self.index = 0
        self.image = mehike_walkright[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.images = self.images_left
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= 5

def main():

    player2 = Player2(position=(100, 100), mehike_walkright=mehike_walkright)
    all_sprites = pygame.sprite.Group(player2)  # Creates a sprite group and adds 'player' to it.

    running = True
    while running:

        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.velocity.x = 4
                elif event.key == pygame.K_LEFT:
                    player.velocity.x = -4

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity.x = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player.velocity.y = 0

        all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).

        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()