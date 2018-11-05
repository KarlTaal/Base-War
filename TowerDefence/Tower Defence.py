import pygame
import ctypes
import time

pygame.init()

FPS = 60
clock = pygame.time.Clock()


#VÕTAB ARVUTI EKRAANI MÕÕTME JA LOOB MÄNGU EKRAANI SUURUSE 
ctypes.windll.user32.SetProcessDPIAware()
true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
mängu_screen = pygame.display.set_mode(true_res,pygame.FULLSCREEN)

#Kogu ekraani suurused
x_global = int(true_res[0])  #1920
y_global = int(true_res[1])  #1080


#MÄNGU NIMI
pygame.display.set_caption("TOWER DEFENCE")

#LAEB PILDID JA MUUDAB NEED SOBIVAKS SUURUSEKS
taust = pygame.image.load("images/taust.png")
taust = pygame.transform.scale(taust, (x_global, y_global))

vasak_torn = pygame.image.load("images/vasak_torn.png")
vasak_torn = pygame.transform.scale(vasak_torn, (int(0.15 * y_global), int(0.15 * x_global)))

parem_torn = pygame.image.load("images/parem_torn.png")
parem_torn = pygame.transform.scale(parem_torn, (int(0.15 * y_global), int(0.15 * x_global)))

mehikese_pildid = [pygame.image.load("images/mehike/mehike1.png"), pygame.image.load("images/mehike/mehike2.png"), pygame.image.load("images/mehike/mehike3.png"),\
pygame.image.load("images/mehike/mehike4.png"), pygame.image.load("images/mehike/mehike5.png"), pygame.image.load("images/mehike/mehike6.png"),\
pygame.image.load("images/mehike/mehike7.png"), pygame.image.load("images/mehike/mehike8.png")]
mehike_walkRight = []
for mehike in mehikese_pildid:
    mehike_walkRight.append(pygame.transform.scale(mehike, (int(0.07 * x_global), int(0.13 * y_global))))
    
class Player(pygame.sprite.Sprite):
#EI SAA PÄRIS HÄSTI ARU MIS SIIN TOIMUB, AGA SEE TÖÖTAB :D
    def __init__(self, position, mehike_walkRight):
        super(Player, self).__init__()
        size = (int(0.15 * x_global), int(0.15 * y_global))
        self.rect = pygame.Rect(position, size)
        self.mehike_walkRight = mehike_walkRight
        self.index = 0
        self.image = mehike_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.001
        self.current_time = 0


    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.mehike_walkRight)
            self.image = self.mehike_walkRight[self.index]

    def update_frame_dependent(self):
        self.current_frame = 0
        self.index = (self.index + 1) % len(self.mehike_walkRight)
        self.image = self.mehike_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 20


def draw():
    mängu_screen.blit(taust, (0, 0))
    all_sprites.update(dt)
    all_sprites.draw(mängu_screen)
    mängu_screen.blit(vasak_torn, (0, 0.635 * y_global))
    mängu_screen.blit(parem_torn, (x_global - int(0.15 * y_global), 0.635 * y_global))
    pygame.display.update()


player = Player(position=(0, y_global * 0.76), mehike_walkRight=mehike_walkRight)
all_sprites = pygame.sprite.Group(player)

a = True
while a:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        a = False

    draw()

pygame.quit()