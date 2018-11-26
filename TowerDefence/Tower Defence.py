import pygame
import ctypes
import random
import time

pygame.init()

FPS = 60
clock = pygame.time.Clock()
tegelane_lisamis_delay = 20
vasaku_torni_elud = 5
parema_torni_elud = 5
vasakud_coinid = 0
paremad_coinid = 0


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

coin1 = pygame.image.load("images/coins/coin1.png")
coin1 = pygame.transform.scale(coin1, (int(0.025 * x_global), int(0.05 * y_global)))

coin2 = pygame.image.load("images/coins/coin2.png")
coin2 = pygame.transform.scale(coin2, (int(0.025 * x_global), int(0.05 * y_global)))

vasak_torn1 = pygame.image.load("images/vasakud_tornid/vasak_torn1.png")
vasak_torn1 = pygame.transform.scale(vasak_torn1, (int(0.2 * y_global), int(0.2 * x_global)))

vasak_torn2 = pygame.image.load("images/vasakud_tornid/vasak_torn2.png")
vasak_torn2 = pygame.transform.scale(vasak_torn2, (int(0.2 * y_global), int(0.2 * x_global)))

vasak_torn3 = pygame.image.load("images/vasakud_tornid/vasak_torn3.png")
vasak_torn3 = pygame.transform.scale(vasak_torn3, (int(0.2 * y_global), int(0.2 * x_global)))

parem_torn1 = pygame.image.load("images/paremad_tornid/parem_torn1.png")
parem_torn1 = pygame.transform.scale(parem_torn1, (int(0.2 * y_global), int(0.2 * x_global)))

parem_torn2 = pygame.image.load("images/paremad_tornid/parem_torn2.png")
parem_torn2 = pygame.transform.scale(parem_torn2, (int(0.2 * y_global), int(0.2 * x_global)))

parem_torn3 = pygame.image.load("images/paremad_tornid/parem_torn3.png")
parem_torn3 = pygame.transform.scale(parem_torn3, (int(0.2 * y_global), int(0.2 * x_global)))

vasak_elud5 = pygame.image.load("images/vasak_elud/vasak_elud5.png")
vasak_elud5 = pygame.transform.scale(vasak_elud5, (int(0.1 * y_global), int(0.03 * x_global)))

vasak_elud4 = pygame.image.load("images/vasak_elud/vasak_elud4.png")
vasak_elud4 = pygame.transform.scale(vasak_elud4, (int(0.1 * y_global), int(0.03 * x_global)))

vasak_elud3 = pygame.image.load("images/vasak_elud/vasak_elud3.png")
vasak_elud3 = pygame.transform.scale(vasak_elud3, (int(0.1 * y_global), int(0.03 * x_global)))

vasak_elud2 = pygame.image.load("images/vasak_elud/vasak_elud2.png")
vasak_elud2 = pygame.transform.scale(vasak_elud2, (int(0.1 * y_global), int(0.03 * x_global)))

vasak_elud1 = pygame.image.load("images/vasak_elud/vasak_elud1.png")
vasak_elud1 = pygame.transform.scale(vasak_elud1, (int(0.1 * y_global), int(0.03 * x_global)))

parem_elud5 = pygame.image.load("images/parem_elud/parem_elud5.png")
parem_elud5 = pygame.transform.scale(parem_elud5, (int(0.1 * y_global), int(0.03 * x_global)))

parem_elud4 = pygame.image.load("images/parem_elud/parem_elud4.png")
parem_elud4 = pygame.transform.scale(parem_elud4, (int(0.1 * y_global), int(0.03 * x_global)))

parem_elud3 = pygame.image.load("images/parem_elud/parem_elud3.png")
parem_elud3 = pygame.transform.scale(parem_elud3, (int(0.1 * y_global), int(0.03 * x_global)))

parem_elud2 = pygame.image.load("images/parem_elud/parem_elud2.png")
parem_elud2 = pygame.transform.scale(parem_elud2, (int(0.1 * y_global), int(0.03 * x_global)))

parem_elud1 = pygame.image.load("images/parem_elud/parem_elud1.png")
parem_elud1 = pygame.transform.scale(parem_elud1, (int(0.1 * y_global), int(0.03 * x_global)))


mehikese_pildid = [pygame.image.load("images/mehike/mehike1.png"), pygame.image.load("images/mehike/mehike2.png"), pygame.image.load("images/mehike/mehike3.png"),\
pygame.image.load("images/mehike/mehike4.png"), pygame.image.load("images/mehike/mehike5.png"), pygame.image.load("images/mehike/mehike6.png"),\
pygame.image.load("images/mehike/mehike7.png"), pygame.image.load("images/mehike/mehike8.png")]
mehike_walkRight = []
mehike_walkLeft = []
for mehike in mehikese_pildid:
    mehike_walkRight.append(pygame.transform.scale(mehike, (int(0.03 * x_global), int(0.1 * y_global))))
for mehike in mehike_walkRight:
    mehike_walkLeft.append(pygame.transform.flip(mehike, True, False))


knight_pildid = [pygame.image.load("images/knight/knight1.png"), pygame.image.load("images/knight/knight2.png"), pygame.image.load("images/knight/knight3.png"),\
pygame.image.load("images/knight/knight4.png"), pygame.image.load("images/knight/knight5.png"), pygame.image.load("images/knight/knight6.png"),\
pygame.image.load("images/knight/knight7.png"), pygame.image.load("images/knight/knight8.png")]
knight_walkRight = []
knight_walkLeft = []
for knight in knight_pildid:
    knight_walkRight.append(pygame.transform.scale(knight, (int(0.07 * x_global), int(0.2 * y_global))))
for knight in knight_walkRight:
    knight_walkLeft.append(pygame.transform.flip(knight, True, False))


skeleton_pildid = [pygame.image.load("images/skeleton/skeleton1.png"), pygame.image.load("images/skeleton/skeleton2.png"), pygame.image.load("images/skeleton/skeleton3.png"),\
pygame.image.load("images/skeleton/skeleton4.png"), pygame.image.load("images/skeleton/skeleton5.png"), pygame.image.load("images/skeleton/skeleton6.png"),\
pygame.image.load("images/skeleton/skeleton7.png"), pygame.image.load("images/skeleton/skeleton8.png"), pygame.image.load("images/skeleton/skeleton9.png"),\
pygame.image.load("images/skeleton/skeleton10.png"), pygame.image.load("images/skeleton/skeleton11.png"), pygame.image.load("images/skeleton/skeleton12.png"), pygame.image.load("images/skeleton/skeleton13.png")]
skeleton_walkRight = []
skeleton_walkLeft = []
for skeleton in skeleton_pildid:
    skeleton_walkRight.append(pygame.transform.scale(skeleton, (int(0.05 * x_global), int(0.13 * y_global))))
for skeleton in skeleton_walkRight:
    skeleton_walkLeft.append(pygame.transform.flip(skeleton, True, False))




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


class Player1(pygame.sprite.Sprite):
    def __init__(self, position, mehike_walkRight):
        super(Player1, self).__init__()
        size = (int(0.03 * x_global), int(0.1 * y_global))
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
    player1 = Player1(position=(0, y_global * 0.79), mehike_walkRight=mehike_walkRight)
    player_list1.add(player1)


class Player2(pygame.sprite.Sprite):
    def __init__(self, position, mehike_walkLeft):
        super(Player2, self).__init__()
        size = (int(0.03 * x_global), int(0.1 * y_global))
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
    player2 = Player2(position=(x_global - int(0.07 * x_global) , y_global * 0.79), mehike_walkLeft=mehike_walkLeft)
    player_list2.add(player2)


class Knight1(pygame.sprite.Sprite):
    def __init__(self, position, knight_walkRight):
        super(Knight1, self).__init__()
        size = (int(0.07 * x_global), int(0.2 * y_global))
        self.rect = pygame.Rect(position, size)
        self.knight_walkRight = knight_walkRight
        self.index = 0
        self.image = knight_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.knight_walkRight)
            self.image = self.knight_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 5
def knight1():
    knight1 = Knight1(position=(0, y_global * 0.7), knight_walkRight=knight_walkRight)
    knight_list1.add(knight1)


class Knight2(pygame.sprite.Sprite):
    def __init__(self, position, knight_walkLeft):
        super(Knight2, self).__init__()
        size = (int(0.07 * x_global), int(0.2 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = knight_walkLeft
        self.index = 0
        self.image = knight_walkLeft[self.index]
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
def knight2():
    knight2 = Knight2(position=(x_global - int(0.07 * x_global) , y_global * 0.7), knight_walkLeft=knight_walkLeft)
    knight_list2.add(knight2)


class Skeleton1(pygame.sprite.Sprite):
    def __init__(self, position, skeleton_walkRight):
        super(Skeleton1, self).__init__()
        size = (int(0.05 * x_global), int(0.13 * y_global))
        self.rect = pygame.Rect(position, size)
        self.skeleton_walkRight = skeleton_walkRight
        self.index = 0
        self.image = skeleton_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.skeleton_walkRight)
            self.image = self.skeleton_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 5
def skeleton1():
    skeleton1 = Skeleton1(position=(0, y_global * 0.76), skeleton_walkRight=skeleton_walkRight)
    skeleton_list1.add(skeleton1)


class Skeleton2(pygame.sprite.Sprite):
    def __init__(self, position, skeleton_walkLeft):
        super(Skeleton2, self).__init__()
        size = (int(0.05 * x_global), int(0.13 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = skeleton_walkLeft
        self.index = 0
        self.image = skeleton_walkLeft[self.index]
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
def skeleton2():
    skeleton2 = Skeleton2(position=(x_global - int(0.07 * x_global) , y_global * 0.76), skeleton_walkLeft=skeleton_walkLeft)
    skeleton_list2.add(skeleton2)



def kokkupuude1():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,1)
        if suvaline == 0:
            player_list1.remove(i)
        elif suvaline == 1:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude2():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,1)
        if suvaline == 0:
            knight_list1.remove(i)
        elif suvaline == 1:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude3():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,10)
        if suvaline == 0:
            knight_list1.remove(i)
        elif suvaline > 0:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude4():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,10)
        if suvaline > 0:
            player_list1.remove(i)
        elif suvaline == 0:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude5():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,5)
        if suvaline > 0:
            player_list1.remove(i)
        elif suvaline == 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude6():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,5)
        if suvaline == 0:
            knight_list1.remove(i)
        elif suvaline > 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude7():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,5)
        if suvaline > 0:
            skeleton_list1.remove(i)
        elif suvaline == 0:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude8():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,5)
        if suvaline == 0:
            skeleton_list1.remove(i)
        elif suvaline > 0:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude9():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0,1)
        if suvaline == 1:
            skeleton_list1.remove(i)
        elif suvaline == 0:
            skeleton_list2.remove(tegelane_hit_list[i])




def draw(vasaktorn, paremtorn, vasakud_elud, paremad_elud, coins1, coins2):
    kokkupuude1()
    kokkupuude2()
    kokkupuude3()
    kokkupuude4()
    kokkupuude5()
    kokkupuude6()
    kokkupuude7()
    kokkupuude8()
    kokkupuude9()
    mängu_screen.blit(taust, (0, 0))
    player_list1.update(dt)
    player_list2.update(dt)
    player_list1.draw(mängu_screen)
    player_list2.draw(mängu_screen)
    knight_list1.update(dt)
    knight_list2.update(dt)
    knight_list1.draw(mängu_screen)
    knight_list2.draw(mängu_screen)
    skeleton_list1.update(dt)
    skeleton_list2.update(dt)
    skeleton_list1.draw(mängu_screen)
    skeleton_list2.draw(mängu_screen)
    vasak_torn_sprite.update()
    vasak_torn_sprite.draw(mängu_screen)
    mängu_screen.blit(vasaktorn, (-0.01 * x_global, 0.55 * y_global))
    parem_torn_sprite.update()
    parem_torn_sprite.draw(mängu_screen)
    mängu_screen.blit(paremtorn, (1.01 * (x_global - int(0.2 * y_global)), 0.55 * y_global))
    mängu_screen.blit(vasakud_elud, (0.015 * x_global, 0.49 * y_global))
    mängu_screen.blit(paremad_elud, (0.925 * x_global, 0.49 * y_global))

    mängu_screen.blit(coin1, (0.015 * x_global, 0.425* y_global))
    mängu_screen.blit(coin2, (0.925 * x_global, 0.425 * y_global))

    basicfont1 = pygame.font.SysFont(None, 80)
    text1 = basicfont1.render(str(round(coins1)), True, (139, 117, 0))
    mängu_screen.blit(text1, (0.045 * x_global, 0.43* y_global))

    basicfont2 = pygame.font.SysFont(None, 80)
    text2 = basicfont2.render(str(round(coins2)), True, (139, 117, 0))
    mängu_screen.blit(text2, (0.955 * x_global, 0.43 * y_global))

    pygame.display.update()

def draw_game_over():
    mängu_screen.blit(game_over, (0, 0))
    pygame.display.update()


player_list2 = pygame.sprite.Group()
player_list1 = pygame.sprite.Group()
knight_list2 = pygame.sprite.Group()
knight_list1 = pygame.sprite.Group()
skeleton_list2 = pygame.sprite.Group()
skeleton_list1 = pygame.sprite.Group()
a = True
b = 0

#viivitus tegelaste lisamiseks, 1- vasak   2-parem
tegelane1_aeg = tegelane_lisamis_delay
tegelane2_aeg = tegelane_lisamis_delay

while a:
    dt = clock.tick(FPS) / 1000

    k1 = pygame.sprite.groupcollide(player_list1, parem_torn_sprite, False, False, collided=None)
    for i in k1:
        player_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b = 1
    k2 = pygame.sprite.groupcollide(player_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k2:
        player_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b = 1
    k3 = pygame.sprite.groupcollide(knight_list1, parem_torn_sprite, False, False, collided=None)
    for i in k3:
        knight_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b = 1
    k4 = pygame.sprite.groupcollide(knight_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k4:
        knight_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b = 1
    k5 = pygame.sprite.groupcollide(skeleton_list1, parem_torn_sprite, False, False, collided=None)
    for i in k5:
        skeleton_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b = 1
    k6 = pygame.sprite.groupcollide(skeleton_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k6:
        skeleton_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b = 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    player1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_j:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    player2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_d:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    knight1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_l:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    knight2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_s:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    skeleton1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_k:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    skeleton2()
                    tegelane2_aeg -= tegelane_lisamis_delay
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                a = False

    if vasaku_torni_elud > 3:
        vasaktorn = vasak_torn1
    if vasaku_torni_elud > 1 and vasaku_torni_elud < 4:
        vasaktorn = vasak_torn2
    if vasaku_torni_elud == 1:
        vasaktorn = vasak_torn3

    if parema_torni_elud > 3:
        paremtorn = parem_torn1
    if parema_torni_elud > 1 and parema_torni_elud < 4:
        paremtorn = parem_torn2
    if parema_torni_elud == 1:
        paremtorn = parem_torn3

    if vasaku_torni_elud == 5:
        vasakud_elud = vasak_elud5
    if vasaku_torni_elud == 4:
        vasakud_elud = vasak_elud4
    if vasaku_torni_elud == 3:
        vasakud_elud = vasak_elud3
    if vasaku_torni_elud == 2:
        vasakud_elud = vasak_elud2
    if vasaku_torni_elud == 1:
        vasakud_elud = vasak_elud1
    if parema_torni_elud == 5:
        paremad_elud = parem_elud5
    if parema_torni_elud == 4:
        paremad_elud = parem_elud4
    if parema_torni_elud == 3:
        paremad_elud = parem_elud3
    if parema_torni_elud == 2:
        paremad_elud = parem_elud2
    if parema_torni_elud == 1:
        paremad_elud = parem_elud1

    if vasakud_coinid < 30:
        vasakud_coinid += 0.01
        coins1 = vasakud_coinid
    if paremad_coinid < 30:
        paremad_coinid += 0.01
        coins2 = paremad_coinid



    if b == 0:
        draw(vasaktorn, paremtorn, vasakud_elud, paremad_elud, coins1, coins2)
    if b == 1:
        draw_game_over()

#    1 on vasakpoolsed ja 2 on parempoolsed
    if tegelane1_aeg < tegelane_lisamis_delay:
        tegelane1_aeg += 1
    if tegelane2_aeg < tegelane_lisamis_delay:
        tegelane2_aeg += 1
pygame.quit()
