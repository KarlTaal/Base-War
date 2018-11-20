import pygame
import ctypes
import random
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
game_over = pygame.image.load("images/game_over.png")
game_over = pygame.transform.scale(game_over, (x_global,y_global))

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
mehike_walkLeft = []
for mehike in mehikese_pildid:
    mehike_walkRight.append(pygame.transform.scale(mehike, (int(0.07 * x_global), int(0.13 * y_global))))
for mehike in mehike_walkRight:
    mehike_walkLeft.append(pygame.transform.flip(mehike, True, False))


#vasaku torni sprite
class vasaktorn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x_global * 0.06, y_global * 0.1))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, 0.9 * y_global)
vasak_torn_sprite = pygame.sprite.Group()
vasaktorn = vasaktorn()
vasak_torn_sprite.add(vasaktorn)


#parema torni sprite
class paremtorn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x_global * 0.06, y_global * 0.1))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomright = (x_global, 0.9 * y_global)
parem_torn_sprite = pygame.sprite.Group()
paremtorn = paremtorn()
parem_torn_sprite.add(paremtorn)


class Player2(pygame.sprite.Sprite):
    def __init__(self, position, mehike_walkLeft):
        super(Player2, self).__init__()
        size = (int(0.07 * x_global), int(0.13 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = mehike_walkLeft
        self.index = 0
        self.image = mehike_walkLeft[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= 5

def player2():
    player2 = Player2(position=(x_global - int(0.07 * x_global) , y_global * 0.76), mehike_walkLeft=mehike_walkLeft)
    player_list2.add(player2)


class Player1(pygame.sprite.Sprite):
    def __init__(self, position, mehike_walkRight):
        super(Player1, self).__init__()
        size = (int(0.07 * x_global), int(0.13 * y_global))
        self.rect = pygame.Rect(position, size)
        self.mehike_walkRight = mehike_walkRight
        self.index = 0
        self.image = mehike_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.mehike_walkRight)
            self.image = self.mehike_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 5
def player1():
    player1 = Player1(position=(0, y_global * 0.76), mehike_walkRight=mehike_walkRight)
    player_list1.add(player1)


def kokkupuude():
    player_hit_list = pygame.sprite.groupcollide(player_list1, player_list2, False, False, collided=None)
    for i in player_hit_list:
        suvaline = random.randint(0,2)
        if suvaline == 0:
            player_list1.remove(i)
        elif suvaline == 1:
            player_list2.remove(player_hit_list[i])




def draw():
    kokkupuude()
    mängu_screen.blit(taust, (0, 0))
    player_list1.update(dt)
    player_list2.update(dt)
    player_list1.draw(mängu_screen)
    player_list2.draw(mängu_screen)
    vasak_torn_sprite.update()
    vasak_torn_sprite.draw(mängu_screen)
    mängu_screen.blit(vasak_torn, (0, 0.635 * y_global))
    parem_torn_sprite.update()
    parem_torn_sprite.draw(mängu_screen)
    mängu_screen.blit(parem_torn, (x_global - int(0.15 * y_global), 0.635 * y_global))
    pygame.display.update()

def draw_game_over():
    mängu_screen.blit(game_over, (0, 0))

    pygame.display.update()



player_list2 = pygame.sprite.Group()
player_list1 = pygame.sprite.Group()
a = True
b = 0
while a:
    dt = clock.tick(FPS) / 1000

    k = pygame.sprite.groupcollide(player_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k:
        player_list2.remove(i)
        b = 1
    k2 = pygame.sprite.groupcollide(player_list1, parem_torn_sprite, False, False, collided=None)
    for i in k2:
        player_list1.remove(i)
        b = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1()
            if event.key == pygame.K_s:
                player2()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                a = False
    if b == 0:
        draw()
    if b == 1:
        draw_game_over()

pygame.quit()