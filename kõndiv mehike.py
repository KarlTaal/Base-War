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
    images.append(pygame.transform.scale(mehike, (int(200), int(350))))


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images):
        """
        Animated sprite object.

        Args:
            position: x, y coordinate on the screen to place the AnimatedSprite.
            images: Images to use in the animation.
        """
        super(AnimatedSprite, self).__init__()

        size = (32, 32)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        """
        Updates the image of Sprite every 6 frame (approximately every 0.1 second if frame rate is 60).
        """
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update(self, dt):
        """This is the method that's being called when 'all_sprites.update(dt)' is called."""
        # Switch between the two update methods by commenting/uncommenting.
        self.update_time_dependent(dt)
        # self.update_frame_dependent()


def main():

    player = AnimatedSprite(position=(100, 100), images=images)
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.

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
                #elif event.key == pygame.K_DOWN:
                    #player.velocity.y = 4
                #elif event.key == pygame.K_UP:
                    #player.velocity.y = -4
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