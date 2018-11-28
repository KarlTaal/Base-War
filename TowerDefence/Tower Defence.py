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

vasakud_ikoonid1 = pygame.image.load("images/vasakud_tegelased/raam1.png")
vasakud_ikoonid1 = pygame.transform.scale(vasakud_ikoonid1, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_ikoonid2 = pygame.image.load("images/vasakud_tegelased/raam2.png")
vasakud_ikoonid2 = pygame.transform.scale(vasakud_ikoonid2, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_ikoonid3 = pygame.image.load("images/vasakud_tegelased/raam3.png")
vasakud_ikoonid3 = pygame.transform.scale(vasakud_ikoonid3, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_ikoonid4 = pygame.image.load("images/vasakud_tegelased/raam4.png")
vasakud_ikoonid4 = pygame.transform.scale(vasakud_ikoonid4, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_ikoonid5 = pygame.image.load("images/vasakud_tegelased/raam5.png")
vasakud_ikoonid5 = pygame.transform.scale(vasakud_ikoonid5, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_ikoonid6 = pygame.image.load("images/vasakud_tegelased/raam6.png")
vasakud_ikoonid6 = pygame.transform.scale(vasakud_ikoonid6, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_ikoonid7 = pygame.image.load("images/vasakud_kuulid/raam1.png")
vasakud_ikoonid7 = pygame.transform.scale(vasakud_ikoonid7, (int(0.1 * x_global), int(0.1 * y_global)))

vasakud_ikoonid8 = pygame.image.load("images/vasakud_kuulid/raam2.png")
vasakud_ikoonid8 = pygame.transform.scale(vasakud_ikoonid8, (int(0.1 * x_global), int(0.1 * y_global)))

paremad_ikoonid1 = pygame.image.load("images/paremad_tegelased/raam1.png")
paremad_ikoonid1 = pygame.transform.scale(paremad_ikoonid1, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_ikoonid2 = pygame.image.load("images/paremad_tegelased/raam2.png")
paremad_ikoonid2 = pygame.transform.scale(paremad_ikoonid2, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_ikoonid3 = pygame.image.load("images/paremad_tegelased/raam3.png")
paremad_ikoonid3 = pygame.transform.scale(paremad_ikoonid3, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_ikoonid4 = pygame.image.load("images/paremad_tegelased/raam4.png")
paremad_ikoonid4 = pygame.transform.scale(paremad_ikoonid4, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_ikoonid5 = pygame.image.load("images/paremad_tegelased/raam5.png")
paremad_ikoonid5 = pygame.transform.scale(paremad_ikoonid5, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_ikoonid6 = pygame.image.load("images/paremad_tegelased/raam6.png")
paremad_ikoonid6 = pygame.transform.scale(paremad_ikoonid6, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_ikoonid7 = pygame.image.load("images/paremad_kuulid/raam1.png")
paremad_ikoonid7 = pygame.transform.scale(paremad_ikoonid7, (int(0.1 * x_global), int(0.1 * y_global)))

paremad_ikoonid8 = pygame.image.load("images/paremad_kuulid/raam2.png")
paremad_ikoonid8 = pygame.transform.scale(paremad_ikoonid8, (int(0.1 * x_global), int(0.1 * y_global)))

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


punanekuul_pildid = [pygame.image.load("images/punane_kuul/punane1.png"), pygame.image.load("images/punane_kuul/punane2.png"), pygame.image.load("images/punane_kuul/punane3.png"),\
pygame.image.load("images/punane_kuul/punane4.png"), pygame.image.load("images/punane_kuul/punane5.png"), pygame.image.load("images/punane_kuul/punane6.png")]
punanekuul_walkRight = []
punanekuul_walkLeft = []
for kuul in punanekuul_pildid:
    punanekuul_walkRight.append(pygame.transform.scale(kuul, (int(0.1 * x_global), int(0.1 * y_global))))
for kuul in punanekuul_walkRight:
    punanekuul_walkLeft.append(pygame.transform.flip(kuul, True, False))


lillakuul_pildid = [pygame.image.load("images/lilla_kuul/lilla1.png"), pygame.image.load("images/lilla_kuul/lilla2.png"), pygame.image.load("images/lilla_kuul/lilla3.png"),\
pygame.image.load("images/lilla_kuul/lilla4.png"), pygame.image.load("images/lilla_kuul/lilla5.png"), pygame.image.load("images/lilla_kuul/lilla6.png")]
lillakuul_walkRight = []
lillakuul_walkLeft = []
for kuul in lillakuul_pildid:
    lillakuul_walkRight.append(pygame.transform.scale(kuul, (int(0.1 * x_global), int(0.1 * y_global))))
for kuul in lillakuul_walkRight:
    lillakuul_walkLeft.append(pygame.transform.flip(kuul, True, False))


wizard_pildid = [pygame.image.load("images/wizard/wizard1.png"), pygame.image.load("images/wizard/wizard2.png"), pygame.image.load("images/wizard/wizard3.png"),\
pygame.image.load("images/wizard/wizard4.png"), pygame.image.load("images/wizard/wizard5.png")]
wizard_walkRight = []
wizard_walkLeft = []
for wizard in wizard_pildid:
    wizard_walkRight.append(pygame.transform.scale(wizard, (int(0.05 * x_global), int(0.18 * y_global))))
for wizard in wizard_walkRight:
    wizard_walkLeft.append(pygame.transform.flip(wizard, True, False))


orc_pildid = [pygame.image.load("images/orc/orc1.png"), pygame.image.load("images/orc/orc2.png"), pygame.image.load("images/orc/orc3.png"),\
pygame.image.load("images/orc/orc4.png"), pygame.image.load("images/orc/orc5.png"), pygame.image.load("images/orc/orc6.png")]
orc_walkRight = []
orc_walkLeft = []
for orc in orc_pildid:
    orc_walkRight.append(pygame.transform.scale(orc, (int(0.08 * x_global), int(0.11 * y_global))))
for orc in orc_walkRight:
    orc_walkLeft.append(pygame.transform.flip(orc, True, False))


eye_pildid = [pygame.image.load("images/eye/eye1.png"), pygame.image.load("images/eye/eye2.png"), pygame.image.load("images/eye/eye3.png"),\
pygame.image.load("images/eye/eye4.png")]
eye_walkRight = []
eye_walkLeft = []
for eye in eye_pildid:
    eye_walkRight.append(pygame.transform.scale(eye, (int(0.06 * x_global), int(0.18 * y_global))))
for eye in eye_walkRight:
    eye_walkLeft.append(pygame.transform.flip(eye, True, False))


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
    knight_walkRight.append(pygame.transform.scale(knight, (int(0.05 * x_global), int(0.15 * y_global))))
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


class Punanekuul1(pygame.sprite.Sprite):
    def __init__(self, position, punanekuul_walkRight):
        super(Punanekuul1, self).__init__()
        size = (int(0.1 * x_global), int(0.1 * y_global))
        self.rect = pygame.Rect(position, size)
        self.punanekuul_walkRight = punanekuul_walkRight
        self.index = 0
        self.image = punanekuul_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.01
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.punanekuul_walkRight)
            self.image = self.punanekuul_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 15
def punanekuul1():
    punanekuul1 = Punanekuul1(position=(0, y_global * 0.78), punanekuul_walkRight=punanekuul_walkRight)
    punanekuul_list1.add(punanekuul1)


class Punanekuul2(pygame.sprite.Sprite):
    def __init__(self, position, punanekuul_walkLeft):
        super(Punanekuul2, self).__init__()
        size = (int(0.1 * x_global), int(0.1 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = punanekuul_walkLeft
        self.index = 0
        self.image = punanekuul_walkLeft[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.01
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= 15
def punanekuul2():
    punanekuul2 = Punanekuul2(position=(x_global - int(0.1 * x_global), y_global * 0.78), punanekuul_walkLeft=punanekuul_walkLeft)
    punanekuul_list2.add(punanekuul2)


class Lillakuul1(pygame.sprite.Sprite):
    def __init__(self, position, lillakuul_walkRight):
        super(Lillakuul1, self).__init__()
        size = (int(0.1 * x_global), int(0.1 * y_global))
        self.rect = pygame.Rect(position, size)
        self.lillakuul_walkRight = lillakuul_walkRight
        self.index = 0
        self.image = lillakuul_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.01
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.lillakuul_walkRight)
            self.image = self.lillakuul_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 15
def lillakuul1():
    lillakuul1 = Lillakuul1(position=(0, y_global * 0.78), lillakuul_walkRight=lillakuul_walkRight)
    lillakuul_list1.add(lillakuul1)


class Lillakuul2(pygame.sprite.Sprite):
    def __init__(self, position, lillakuul_walkLeft):
        super(Lillakuul2, self).__init__()
        size = (int(0.1 * x_global), int(0.1 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = lillakuul_walkLeft
        self.index = 0
        self.image = lillakuul_walkLeft[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.01
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= 15
def lillakuul2():
    lillakuul2 = Lillakuul2(position=(x_global - int(0.1 * x_global), y_global * 0.78), lillakuul_walkLeft=lillakuul_walkLeft)
    lillakuul_list2.add(lillakuul2)


class Orc1(pygame.sprite.Sprite):
    def __init__(self, position, orc_walkRight):
        super(Orc1, self).__init__()
        size = (int(0.08 * x_global), int(0.11 * y_global))
        self.rect = pygame.Rect(position, size)
        self.orc_walkRight = orc_walkRight
        self.index = 0
        self.image = orc_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.orc_walkRight)
            self.image = self.orc_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 5
def orc1():
    orc1 = Orc1(position=(0, y_global * 0.78), orc_walkRight=orc_walkRight)
    orc_list1.add(orc1)


class Orc2(pygame.sprite.Sprite):
    def __init__(self, position, orc_walkLeft):
        super(Orc2, self).__init__()
        size = (int(0.08 * x_global), int(0.11 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = orc_walkLeft
        self.index = 0
        self.image = orc_walkLeft[self.index]
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
def orc2():
    orc2 = Orc2(position=(x_global - int(0.08 * x_global) , y_global * 0.78), orc_walkLeft=orc_walkLeft)
    orc_list2.add(orc2)


class Wizard1(pygame.sprite.Sprite):
    def __init__(self, position, wizard_walkRight):
        super(Wizard1, self).__init__()
        size = (int(0.05 * x_global), int(0.18 * y_global))
        self.rect = pygame.Rect(position, size)
        self.wizard_walkRight = wizard_walkRight
        self.index = 0
        self.image = wizard_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.wizard_walkRight)
            self.image = self.wizard_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 5
def wizard1():
    wizard1 = Wizard1(position=(0, y_global * 0.73), wizard_walkRight=wizard_walkRight)
    wizard_list1.add(wizard1)


class Wizard2(pygame.sprite.Sprite):
    def __init__(self, position, wizard_walkLeft):
        super(Wizard2, self).__init__()
        size = (int(0.05 * x_global), int(0.18 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = wizard_walkLeft
        self.index = 0
        self.image = wizard_walkLeft[self.index]
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
def wizard2():
    wizard2 = Wizard2(position=(x_global - int(0.05 * x_global) , y_global * 0.73), wizard_walkLeft=wizard_walkLeft)
    wizard_list2.add(wizard2)


class Eye1(pygame.sprite.Sprite):
    def __init__(self, position, eye_walkRight):
        super(Eye1, self).__init__()
        size = (int(0.06 * x_global), int(0.18 * y_global))
        self.rect = pygame.Rect(position, size)
        self.eye_walkRight = eye_walkRight
        self.index = 0
        self.image = eye_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = 0.1
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.eye_walkRight)
            self.image = self.eye_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += 5
def eye1():
    eye1 = Eye1(position=(0, y_global * 0.74), eye_walkRight=eye_walkRight)
    eye_list1.add(eye1)


class Eye2(pygame.sprite.Sprite):
    def __init__(self, position, eye_walkLeft):
        super(Eye2, self).__init__()
        size = (int(0.06 * x_global), int(0.18 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = eye_walkLeft
        self.index = 0
        self.image = eye_walkLeft[self.index]
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
def eye2():
    eye2 = Eye2(position=(x_global - int(0.06 * x_global), y_global * 0.74), eye_walkLeft=eye_walkLeft)
    eye_list2.add(eye2)


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
    player2 = Player2(position=(x_global - int(0.03 * x_global), y_global * 0.79), mehike_walkLeft=mehike_walkLeft)
    player_list2.add(player2)


class Knight1(pygame.sprite.Sprite):
    def __init__(self, position, knight_walkRight):
        super(Knight1, self).__init__()
        size = (int(0.05 * x_global), int(0.15 * y_global))
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
    knight1 = Knight1(position=(0, y_global * 0.75), knight_walkRight=knight_walkRight)
    knight_list1.add(knight1)


class Knight2(pygame.sprite.Sprite):
    def __init__(self, position, knight_walkLeft):
        super(Knight2, self).__init__()
        size = (int(0.05 * x_global), int(0.15 * y_global))
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
    knight2 = Knight2(position=(x_global - int(0.05 * x_global), y_global * 0.75), knight_walkLeft=knight_walkLeft)
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
    skeleton2 = Skeleton2(position=(x_global - int(0.05 * x_global), y_global * 0.76), skeleton_walkLeft=skeleton_walkLeft)
    skeleton_list2.add(skeleton2)



def kokkupuude1():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            player_list1.remove(i)
        elif suvaline == 1:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude2():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            knight_list1.remove(i)
        elif suvaline == 1:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude3():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline == 0:
            knight_list1.remove(i)
        elif suvaline > 0:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude4():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline > 0:
            player_list1.remove(i)
        elif suvaline == 0:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude5():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline > 0:
            player_list1.remove(i)
        elif suvaline == 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude6():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 0:
            knight_list1.remove(i)
        elif suvaline > 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude7():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline > 0:
            skeleton_list1.remove(i)
        elif suvaline == 0:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude8():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 0:
            skeleton_list1.remove(i)
        elif suvaline > 0:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude9():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 1:
            skeleton_list1.remove(i)
        elif suvaline == 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude10():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 15)
        if suvaline > 0:
            player_list1.remove(i)
        elif suvaline == 0:
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude11():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 20)
        if suvaline > 0:
            player_list1.remove(i)
        elif suvaline == 0:
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude12():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 25)
        if suvaline > 0:
            player_list1.remove(i)
        elif suvaline == 0:
            wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude13():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline > 0:
            skeleton_list1.remove(i)
        elif suvaline == 0:
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude14():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 15)
        if suvaline > 0:
            skeleton_list1.remove(i)
        elif suvaline == 0:
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude15():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 20)
        if suvaline > 0:
            skeleton_list1.remove(i)
        elif suvaline == 0:
            wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude16():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline > 0:
            knight_list1.remove(i)
        elif suvaline == 0:
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude17():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline > 0:
            knight_list1.remove(i)
        elif suvaline == 0:
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude18():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 15)
        if suvaline > 0:
            knight_list1.remove(i)
        elif suvaline == 0:
            wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude19():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 15)
        if suvaline == 0:
            orc_list1.remove(i)
        elif suvaline > 0:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude20():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline == 0:
            orc_list1.remove(i)
        elif suvaline > 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude21():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 0:
            orc_list1.remove(i)
        elif suvaline > 0:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude22():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            orc_list1.remove(i)
        elif suvaline == 1:
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude23():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline > 0:
            orc_list1.remove(i)
        elif suvaline == 0:
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude24():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline > 0:
            orc_list1.remove(i)
        elif suvaline == 0:
            wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude25():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 20)
        if suvaline == 0:
            eye_list1.remove(i)
        elif suvaline > 0:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude26():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 15)
        if suvaline == 0:
            eye_list1.remove(i)
        elif suvaline > 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude27():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline == 0:
            eye_list1.remove(i)
        elif suvaline > 0:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude28():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 0:
            eye_list1.remove(i)
        elif suvaline > 0:
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude29():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            eye_list1.remove(i)
        elif suvaline == 1:
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude30():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline > 0:
            eye_list1.remove(i)
        elif suvaline == 0:
            wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude31():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 25)
        if suvaline == 0:
            wizard_list1.remove(i)
        elif suvaline > 0:
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude32():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 20)
        if suvaline == 0:
            wizard_list1.remove(i)
        elif suvaline > 0:
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude33():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 15)
        if suvaline == 0:
            wizard_list1.remove(i)
        elif suvaline > 0:
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude34():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 10)
        if suvaline == 0:
            wizard_list1.remove(i)
        elif suvaline > 0:
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude35():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 0:
            wizard_list1.remove(i)
        elif suvaline > 0:
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude36():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            wizard_list1.remove(i)
        elif suvaline == 1:
            wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude37():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        player_list2.remove(tegelane_hit_list[i])
def kokkupuude38():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude39():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        knight_list2.remove(tegelane_hit_list[i])
def kokkupuude40():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        eye_list2.remove(tegelane_hit_list[i])
def kokkupuude41():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude42():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        orc_list2.remove(tegelane_hit_list[i])
def kokkupuude43():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, player_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        player_list1.remove(tegelane_hit_list[i])
def kokkupuude44():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, skeleton_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        skeleton_list1.remove(tegelane_hit_list[i])
def kokkupuude45():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, knight_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        knight_list1.remove(tegelane_hit_list[i])
def kokkupuude46():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, eye_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        eye_list1.remove(tegelane_hit_list[i])
def kokkupuude47():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, orc_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        orc_list1.remove(tegelane_hit_list[i])
def kokkupuude48():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, wizard_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        wizard_list1.remove(tegelane_hit_list[i])
def kokkupuude49():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, lillakuul_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        lillakuul_list1.remove(i)
        lillakuul_list2.remove(tegelane_hit_list[i])





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
    kokkupuude10()
    kokkupuude11()
    kokkupuude12()
    kokkupuude13()
    kokkupuude14()
    kokkupuude15()
    kokkupuude16()
    kokkupuude17()
    kokkupuude18()
    kokkupuude19()
    kokkupuude20()
    kokkupuude21()
    kokkupuude22()
    kokkupuude23()
    kokkupuude24()
    kokkupuude25()
    kokkupuude26()
    kokkupuude27()
    kokkupuude28()
    kokkupuude29()
    kokkupuude30()
    kokkupuude31()
    kokkupuude32()
    kokkupuude33()
    kokkupuude34()
    kokkupuude35()
    kokkupuude36()
    kokkupuude37()
    kokkupuude38()
    kokkupuude39()
    kokkupuude40()
    kokkupuude41()
    kokkupuude42()
    kokkupuude43()
    kokkupuude44()
    kokkupuude45()
    kokkupuude46()
    kokkupuude47()
    kokkupuude48()
    kokkupuude49()

    mängu_screen.blit(taust, (0, 0))

    #(int(0.05 * x_global), int(0.1 * y_global)) - ruutude suurused
    mängu_screen.blit(vasakud_ikoonid1, (0, 0))
    mängu_screen.blit(vasakud_ikoonid2, ((int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasakud_ikoonid3, (2 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasakud_ikoonid4, (3 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasakud_ikoonid5, (4 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasakud_ikoonid6, (5 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(paremad_ikoonid6, (x_global - int(0.05 * x_global), 0))
    mängu_screen.blit(paremad_ikoonid5, (x_global - 2 * (int(0.05 * x_global)) - 5, 0))
    mängu_screen.blit(paremad_ikoonid4, (x_global - 3 * (int(0.05 * x_global)) - 10, 0))
    mängu_screen.blit(paremad_ikoonid3, (x_global - 4 * (int(0.05 * x_global)) - 15, 0))
    mängu_screen.blit(paremad_ikoonid2, (x_global - 5 * (int(0.05 * x_global)) - 20, 0))
    mängu_screen.blit(paremad_ikoonid1, (x_global - 6 * (int(0.05 * x_global)) - 25, 0))

    mängu_screen.blit(vasakud_ikoonid7, (0, int(0.1 * y_global) + 5))
    mängu_screen.blit(vasakud_ikoonid8, ((int(0.1 * x_global) + 5), int(0.1 * y_global) + 5))
    mängu_screen.blit(paremad_ikoonid8, (x_global - int(0.1 * x_global), int(0.1 * y_global) + 5))
    mängu_screen.blit(paremad_ikoonid7, (x_global - 2 * (int(0.1 * x_global)) - 5, int(0.1 * y_global) + 5))

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
    eye_list1.update(dt)
    eye_list2.update(dt)
    eye_list1.draw(mängu_screen)
    eye_list2.draw(mängu_screen)
    orc_list1.update(dt)
    orc_list2.update(dt)
    orc_list1.draw(mängu_screen)
    orc_list2.draw(mängu_screen)
    wizard_list1.update(dt)
    wizard_list2.update(dt)
    wizard_list1.draw(mängu_screen)
    wizard_list2.draw(mängu_screen)
    lillakuul_list1.update(dt)
    lillakuul_list2.update(dt)
    lillakuul_list1.draw(mängu_screen)
    lillakuul_list2.draw(mängu_screen)
    punanekuul_list1.update(dt)
    punanekuul_list2.update(dt)
    punanekuul_list1.draw(mängu_screen)
    punanekuul_list2.draw(mängu_screen)
    vasak_torn_sprite.update()
    #vasak_torn_sprite.draw(mängu_screen)
    mängu_screen.blit(vasaktorn, (-0.01 * x_global, 0.55 * y_global))
    parem_torn_sprite.update()
    #parem_torn_sprite.draw(mängu_screen)
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
orc_list2 = pygame.sprite.Group()
orc_list1 = pygame.sprite.Group()
eye_list2 = pygame.sprite.Group()
eye_list1 = pygame.sprite.Group()
wizard_list2 = pygame.sprite.Group()
wizard_list1 = pygame.sprite.Group()
lillakuul_list2 = pygame.sprite.Group()
lillakuul_list1 = pygame.sprite.Group()
punanekuul_list2 = pygame.sprite.Group()
punanekuul_list1 = pygame.sprite.Group()
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
    k7 = pygame.sprite.groupcollide(eye_list1, parem_torn_sprite, False, False, collided=None)
    for i in k7:
        eye_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b = 1
    k8 = pygame.sprite.groupcollide(eye_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k8:
        eye_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b = 1
    k9 = pygame.sprite.groupcollide(orc_list1, parem_torn_sprite, False, False, collided=None)
    for i in k9:
        orc_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b = 1
    k10 = pygame.sprite.groupcollide(orc_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k10:
        orc_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b = 1
    k11 = pygame.sprite.groupcollide(wizard_list1, parem_torn_sprite, False, False, collided=None)
    for i in k11:
        wizard_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b = 1
    k12 = pygame.sprite.groupcollide(wizard_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k12:
        wizard_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b = 1
    k13 = pygame.sprite.groupcollide(lillakuul_list1, parem_torn_sprite, False, False, collided=None)
    for i in k13:
        lillakuul_list1.remove(i)
    k14 = pygame.sprite.groupcollide(lillakuul_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k14:
        lillakuul_list2.remove(i)
    k15 = pygame.sprite.groupcollide(punanekuul_list1, parem_torn_sprite, False, False, collided=None)
    for i in k15:
        punanekuul_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b = 1
    k16 = pygame.sprite.groupcollide(punanekuul_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k16:
        punanekuul_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b = 1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    player1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_u:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    player2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_e:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    knight1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_o:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    knight2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_w:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    skeleton1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_i:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    skeleton2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_s:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    eye1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_k:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    eye2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_a:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    orc1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_j:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    orc2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_d:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    wizard1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_l:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    wizard2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_z:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    lillakuul1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_n:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    lillakuul2()
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_x:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    punanekuul1()
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_m:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    punanekuul2()
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
