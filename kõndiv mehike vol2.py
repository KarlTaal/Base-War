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
images = []
for mehike in mehikese_pildid:
    images.append(pygame.transform.scale(mehike, (int(200), int(300))))


class Player(pygame.sprite.Sprite):

    def __init__(self, position, images):
        super(Player, self).__init__()
        size = (200, 300)
        self.rect = pygame.Rect(position, size)
        self.images = images
        self.index = 0
        self.image = images[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.2
        self.current_time = 0


    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update_frame_dependent(self):
        self.current_frame = 0
        self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)


player = Player(position=(100, 100), images=images)
all_sprites = pygame.sprite.Group(player)

running = True
while running:

    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)

    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    pygame.display.update()
