import pygame
import random
import time


pygame.init()
#initialize pygame.mixer
pygame.mixer.init(frequency = 44100, size = -16, channels = 4, buffer = 2**12)
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)




FPS = 60
clock = pygame.time.Clock()
tegelane_lisamis_delay = 20
vasaku_torni_elud = 5
parema_torni_elud = 5
vasakud_coinid = 0
paremad_coinid = 0
mute_muutuja = 0

#sõnumid
sõnumid = ["There is actually a poem written by Tim Peters named as THE ZEN OF PYTHON which can be read by just writing “import this” in the interpreter.",\
           "You can use an “else” clause with a “for” loop in Python. It’s a special type of syntax that executes only if the for loop exits naturally, without any break statements.",\
           "In Python, everything is done by reference. It doesn’t support pointers.",\
           "We can’t define Infinities right? But wait! Not for Python.",\
           "Python was named after the comedy troupe Monty Python.",\
           "Python was created in 1991 by Guido Van Rossum.",\
           "There are Java and C variants of Python called JPython and CPython.",\
           "Python is an interpretive language, meaning you don’t need to compile it.",\
           "Python is part of the open source community, meaning plenty of independent programmers are out there building libraries and adding functionality to Python.",\
           "Python is one of the official languages at Google.",\
           "Python has done away with braces. Find out what happens when you try importing braces.",\
           "Programmer: An organism that turns caffeine and pizza into software.",\
           "Software developers like to solve problems. If there are no problems available, they will create their own problems. It’s an addiction.",\
           "Algorithm: Word used by programmers when they do not want to explain what they did.",\
           "A programmer puts two glasses on his bedside table before going to sleep. A full one, in case he gets thirsty, and an empty one, in case he doesn’t.",\
           "Hardware- The part of a computer that you can kick.",\
           "Chuck Norris can take a screenshot of his blue screen.",\
           "99 little bugs in the code, 99 bugs in the code, 1 bug fixed...compile again, 100 little bugs in the code.",\
           "Debugging is like being the detective in a crime drama where you are also the murderer.",\
           "The best thing about a Boolean is that even if you are wrong, you are only off by a bit."]
            ##########################################################################################     -pikkus, kus teksti suurus muutub
#windows
try:
    muusika = 0
    import ctypes
    ctypes.windll.user32.SetProcessDPIAware()
    true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
    y_global = int(true_res[1])
    x_global = int(y_global * (16/9))# arvutab suhte järgi x'i, siis on suhe koguaeg sama, ükskõik mis resolutsiooniga
    mängu_screen = pygame.display.set_mode((x_global, y_global), pygame.FULLSCREEN)

#mac
except:
    muusika = 1
    infoObject = pygame.display.Info()
    y_global = infoObject.current_h
    x_global = int(y_global * (16/9))
    mängu_screen = pygame.display.set_mode((x_global, y_global), pygame.FULLSCREEN)

#MÄNGU NIMI
pygame.display.set_caption("BASE WAR")

#LAEB PILDID JA MUUDAB NEED SOBIVAKS SUURUSEKS
game_over_vasakpool = pygame.image.load("images/taustad/game_over_parem.png")
game_over_vasakpool = pygame.transform.scale(game_over_vasakpool, (x_global, y_global))
game_over_parempool = pygame.image.load("images/taustad/game_over_vasak.png")
game_over_parempool = pygame.transform.scale(game_over_parempool, (x_global, y_global))
start_screen = pygame.image.load("images/taustad/start_screen.png")
start_screen = pygame.transform.scale(start_screen, (x_global, y_global))
instructions = pygame.image.load("images/taustad/instructions.png")
instructions = pygame.transform.scale(instructions, (x_global, y_global))


vasakud_tuhm1 = pygame.image.load("images/vasakud_tegelased/tuhm1.png")
vasakud_tuhm1 = pygame.transform.scale(vasakud_tuhm1, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_tuhm2 = pygame.image.load("images/vasakud_tegelased/tuhm2.png")
vasakud_tuhm2 = pygame.transform.scale(vasakud_tuhm2, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_tuhm3 = pygame.image.load("images/vasakud_tegelased/tuhm3.png")
vasakud_tuhm3 = pygame.transform.scale(vasakud_tuhm3, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_tuhm4 = pygame.image.load("images/vasakud_tegelased/tuhm4.png")
vasakud_tuhm4 = pygame.transform.scale(vasakud_tuhm4, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_tuhm5 = pygame.image.load("images/vasakud_tegelased/tuhm5.png")
vasakud_tuhm5 = pygame.transform.scale(vasakud_tuhm5, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_tuhm6 = pygame.image.load("images/vasakud_tegelased/tuhm6.png")
vasakud_tuhm6 = pygame.transform.scale(vasakud_tuhm6, (int(0.05 * x_global), int(0.1 * y_global)))

vasakud_tuhm7 = pygame.image.load("images/vasakud_kuulid/tuhm1.png")
vasakud_tuhm7 = pygame.transform.scale(vasakud_tuhm7, (int(0.1 * x_global), int(0.1 * y_global)))

vasakud_tuhm8 = pygame.image.load("images/vasakud_kuulid/tuhm2.png")
vasakud_tuhm8 = pygame.transform.scale(vasakud_tuhm8, (int(0.1 * x_global), int(0.1 * y_global)))

paremad_tuhm1 = pygame.image.load("images/paremad_tegelased/tuhm1.png")
paremad_tuhm1 = pygame.transform.scale(paremad_tuhm1, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_tuhm2 = pygame.image.load("images/paremad_tegelased/tuhm2.png")
paremad_tuhm2 = pygame.transform.scale(paremad_tuhm2, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_tuhm3 = pygame.image.load("images/paremad_tegelased/tuhm3.png")
paremad_tuhm3 = pygame.transform.scale(paremad_tuhm3, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_tuhm4 = pygame.image.load("images/paremad_tegelased/tuhm4.png")
paremad_tuhm4 = pygame.transform.scale(paremad_tuhm4, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_tuhm5 = pygame.image.load("images/paremad_tegelased/tuhm5.png")
paremad_tuhm5 = pygame.transform.scale(paremad_tuhm5, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_tuhm6 = pygame.image.load("images/paremad_tegelased/tuhm6.png")
paremad_tuhm6 = pygame.transform.scale(paremad_tuhm6, (int(0.05 * x_global), int(0.1 * y_global)))

paremad_tuhm7 = pygame.image.load("images/paremad_kuulid/tuhm1.png")
paremad_tuhm7 = pygame.transform.scale(paremad_tuhm7, (int(0.1 * x_global), int(0.1 * y_global)))

paremad_tuhm8 = pygame.image.load("images/paremad_kuulid/tuhm2.png")
paremad_tuhm8 = pygame.transform.scale(paremad_tuhm8, (int(0.1 * x_global), int(0.1 * y_global)))

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

taust = pygame.image.load("images/taustad/taust.png")
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



#Laeb heli
if muusika == 0:
    suremine_mees = pygame.mixer.Sound("audio/suremine_mees.wav")
    suremine_knight = pygame.mixer.Sound("audio/suremine_knight.wav")
    suremine_võlur = pygame.mixer.Sound("audio/suremine_võlur.wav")
    suremine_orc = pygame.mixer.Sound("audio/suremine_orc.wav")
    suremine_eye = pygame.mixer.Sound("audio/suremine_eye.wav")
    suremine_skeleton = pygame.mixer.Sound("audio/suremine_skeleton.wav")
    kuul_vastastevastu = pygame.mixer.Sound("audio/kuul_vastastevastu.wav")
    kuul_tornivastu = pygame.mixer.Sound("audio/kuul_tornivastu.wav")
    kuul_heli = pygame.mixer.Sound("audio/kuul.wav")
    torni_pihtasaamine = pygame.mixer.Sound("audio/torni_pihtasaamine.wav")
    mäng_muusika = pygame.mixer.Sound("audio/mäng.wav")
    mittemäng_muusika = pygame.mixer.Sound("audio/mittemäng.wav")



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
        self.animation_time = (y_global * 0.00009259)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.punanekuul_walkRight)
            self.image = self.punanekuul_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        #self.rect.x += int(0.014 * y_global)
        self.rect.x += int(0.023 * y_global)
def punanekuul1():
    punanekuul1 = Punanekuul1(position=(0, y_global * 0.78), punanekuul_walkRight=punanekuul_walkRight)
    punanekuul_list1.add(punanekuul1)
    channel1.play(kuul_heli)
    channel1.set_volume(0.4)


class Punanekuul2(pygame.sprite.Sprite):
    def __init__(self, position, punanekuul_walkLeft):
        super(Punanekuul2, self).__init__()
        size = (int(0.1 * x_global), int(0.1 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = punanekuul_walkLeft
        self.index = 0
        self.image = punanekuul_walkLeft[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = (y_global * 0.00009259)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        #self.rect.x -= int(0.014 * y_global)
        self.rect.x -= int(0.023 * y_global)
def punanekuul2():
    punanekuul2 = Punanekuul2(position=(x_global - int(0.1 * x_global), y_global * 0.78), punanekuul_walkLeft=punanekuul_walkLeft)
    punanekuul_list2.add(punanekuul2)
    channel1.play(kuul_heli)
    channel1.set_volume(0.2)


class Lillakuul1(pygame.sprite.Sprite):
    def __init__(self, position, lillakuul_walkRight):
        super(Lillakuul1, self).__init__()
        size = (int(0.1 * x_global), int(0.1 * y_global))
        self.rect = pygame.Rect(position, size)
        self.lillakuul_walkRight = lillakuul_walkRight
        self.index = 0
        self.image = lillakuul_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = (y_global * 0.00009259)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.lillakuul_walkRight)
            self.image = self.lillakuul_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        #self.rect.x += int(0.014 * y_global)
        self.rect.x += int(0.023 * y_global)
def lillakuul1():
    lillakuul1 = Lillakuul1(position=(0, y_global * 0.78), lillakuul_walkRight=lillakuul_walkRight)
    lillakuul_list1.add(lillakuul1)
    channel1.play(kuul_heli)
    channel1.set_volume(0.2)

class Lillakuul2(pygame.sprite.Sprite):
    def __init__(self, position, lillakuul_walkLeft):
        super(Lillakuul2, self).__init__()
        size = (int(0.1 * x_global), int(0.1 * y_global))
        self.rect = pygame.Rect(position, size)
        self.images = lillakuul_walkLeft
        self.index = 0
        self.image = lillakuul_walkLeft[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = (y_global * 0.00009259)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        #self.rect.x -= int(0.014 * y_global)
        self.rect.x -= int(0.023 * y_global)
def lillakuul2():
    lillakuul2 = Lillakuul2(position=(x_global - int(0.1 * x_global), y_global * 0.78), lillakuul_walkLeft=lillakuul_walkLeft)
    lillakuul_list2.add(lillakuul2)
    channel1.play(kuul_heli)
    channel1.set_volume(0.2)


class Orc1(pygame.sprite.Sprite):
    def __init__(self, position, orc_walkRight):
        super(Orc1, self).__init__()
        size = (int(0.08 * x_global), int(0.11 * y_global))
        self.rect = pygame.Rect(position, size)
        self.orc_walkRight = orc_walkRight
        self.index = 0
        self.image = orc_walkRight[self.index]
        self.velocity = pygame.math.Vector2(0, 0)
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.orc_walkRight)
            self.image = self.orc_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.wizard_walkRight)
            self.image = self.wizard_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.eye_walkRight)
            self.image = self.eye_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.mehike_walkRight)
            self.image = self.mehike_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.knight_walkRight)
            self.image = self.knight_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000092593)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000046296)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.skeleton_walkRight)
            self.image = self.skeleton_walkRight[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x += int(0.0047 * y_global)
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
        self.animation_time = (y_global * 0.000046296)
        self.current_time = 0

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.x -= int(0.0047 * y_global)
def skeleton2():
    skeleton2 = Skeleton2(position=(x_global - int(0.05 * x_global), y_global * 0.76), skeleton_walkLeft=skeleton_walkLeft)
    skeleton_list2.add(skeleton2)



def kokkupuude1():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, player_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list1.remove(i)
        elif suvaline == 1:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude2():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, knight_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list1.remove(i)
        elif suvaline == 1:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude3():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, player_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 4
        elif suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude4():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, knight_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list1.remove(i)
        elif suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list2.remove(tegelane_hit_list[i])
            if paremad_coinid < 999:
                paremad_coinid += 4
def kokkupuude5():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, skeleton_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list1.remove(i)
        elif suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 2
def kokkupuude6():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, skeleton_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 2
        elif suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude7():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, knight_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list1.remove(i)
        elif suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 2
def kokkupuude8():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, player_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 2
        elif suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude9():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, skeleton_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 1:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list1.remove(i)
        elif suvaline == 0:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude10():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, orc_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 7)
        if suvaline < 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list1.remove(i)
        elif suvaline == 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 6
def kokkupuude11():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, eye_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 9)
        if suvaline < 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list1.remove(i)
        elif suvaline == 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 8
def kokkupuude12():
    tegelane_hit_list = pygame.sprite.groupcollide(player_list1, wizard_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 11)
        if suvaline < 11:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list1.remove(i)
        elif suvaline == 11:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 10
def kokkupuude13():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, orc_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list1.remove(i)
        elif suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 4
def kokkupuude14():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, eye_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 7)
        if suvaline < 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list1.remove(i)
        elif suvaline == 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 6
def kokkupuude15():
    tegelane_hit_list = pygame.sprite.groupcollide(skeleton_list1, wizard_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 9)
        if suvaline < 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list1.remove(i)
        elif suvaline == 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 8
def kokkupuude16():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, orc_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list1.remove(i)
        elif suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 2
def kokkupuude17():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, eye_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list1.remove(i)
        elif suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 4
def kokkupuude18():
    tegelane_hit_list = pygame.sprite.groupcollide(knight_list1, wizard_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 7)
        if suvaline < 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list1.remove(i)
        elif suvaline == 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 6
def kokkupuude19():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, player_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 7)
        if suvaline == 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 6
        elif suvaline < 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude20():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, skeleton_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 6
        elif suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude21():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, knight_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 2
        elif suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude22():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, orc_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list1.remove(i)
        elif suvaline == 1:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude23():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, eye_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list1.remove(i)
        elif suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 2
def kokkupuude24():
    tegelane_hit_list = pygame.sprite.groupcollide(orc_list1, wizard_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list1.remove(i)
        elif suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 4
def kokkupuude25():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, player_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 9)
        if suvaline == 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 8
        elif suvaline < 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude26():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, skeleton_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 7)
        if suvaline == 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 6
        elif suvaline < 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude27():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, knight_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 4
        elif suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude28():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, orc_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 2
        elif suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude29():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, eye_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list1.remove(i)
        elif suvaline == 1:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude30():
    tegelane_hit_list = pygame.sprite.groupcollide(eye_list1, wizard_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list1.remove(i)
        elif suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list2.remove(tegelane_hit_list[i])
            if vasakud_coinid < 999:
                vasakud_coinid += 2
def kokkupuude31():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, player_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 11)
        if suvaline == 11:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 10
        elif suvaline < 11:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_mees)
            player_list2.remove(tegelane_hit_list[i])
def kokkupuude32():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, skeleton_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 9)
        if suvaline == 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 8
        elif suvaline < 9:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_skeleton)
            skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude33():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, knight_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 7)
        if suvaline == 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 6
        elif suvaline < 7:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_knight)
            knight_list2.remove(tegelane_hit_list[i])
def kokkupuude34():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, orc_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 5)
        if suvaline == 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 4
        elif suvaline < 5:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_orc)
            orc_list2.remove(tegelane_hit_list[i])
def kokkupuude35():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, eye_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 3)
        if suvaline == 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list1.remove(i)
            if paremad_coinid < 999:
                paremad_coinid += 2
        elif suvaline < 3:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_eye)
            eye_list2.remove(tegelane_hit_list[i])
def kokkupuude36():
    tegelane_hit_list = pygame.sprite.groupcollide(wizard_list1, wizard_list2, False, False, collided=None)
    global vasakud_coinid
    global paremad_coinid
    for i in tegelane_hit_list:
        suvaline = random.randint(0, 1)
        if suvaline == 0:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list1.remove(i)
        elif suvaline == 1:
            if muusika == 0:
                pygame.mixer.Sound.play(suremine_võlur)
            wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude37():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, player_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_mees)
        player_list2.remove(tegelane_hit_list[i])
def kokkupuude38():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, skeleton_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_skeleton)
        skeleton_list2.remove(tegelane_hit_list[i])
def kokkupuude39():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, knight_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_knight)
        knight_list2.remove(tegelane_hit_list[i])
def kokkupuude40():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, eye_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_eye)
        eye_list2.remove(tegelane_hit_list[i])
def kokkupuude41():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, wizard_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_võlur)
        wizard_list2.remove(tegelane_hit_list[i])
def kokkupuude42():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, orc_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_orc)
        orc_list2.remove(tegelane_hit_list[i])
def kokkupuude43():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, player_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_mees)
        player_list1.remove(tegelane_hit_list[i])
def kokkupuude44():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, skeleton_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_skeleton)
        skeleton_list1.remove(tegelane_hit_list[i])
def kokkupuude45():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, knight_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_knight)
        knight_list1.remove(tegelane_hit_list[i])
def kokkupuude46():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, eye_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_eye)
        eye_list1.remove(tegelane_hit_list[i])
def kokkupuude47():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, orc_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_orc)
        orc_list1.remove(tegelane_hit_list[i])
def kokkupuude48():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list2, wizard_list1, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Sound.play(suremine_võlur)
        wizard_list1.remove(tegelane_hit_list[i])
def kokkupuude49():
    tegelane_hit_list = pygame.sprite.groupcollide(lillakuul_list1, lillakuul_list2, False, False, collided=None)
    for i in tegelane_hit_list:
        if muusika == 0:
            pygame.mixer.Sound.play(kuul_vastastevastu)
            pygame.mixer.Channel(0).stop()
        lillakuul_list1.remove(i)
        lillakuul_list2.remove(tegelane_hit_list[i])


class Button_Play:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Play',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.045)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_play = Button_Play(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.55), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus


class Button_Instructions:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Instructions',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_instructions = Button_Instructions(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.645), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus


class Button_ESC1:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Quit',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_ESC1 = Button_ESC1(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.74), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus


class Button_Back:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Back',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_back = Button_Back((5, 5, (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus


class Button_Play_Again:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Play again',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_play_again = Button_Play_Again(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.55), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus


class Button_Mainmenu1:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Main menu',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_mainmenu1 = Button_Mainmenu1(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.645), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus


class Button_ESC2:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Quit',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_ESC2 = Button_ESC2(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.74), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus


class Button_Mainmenu2:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Main menu',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_mainmenu2 = Button_Mainmenu2(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.645), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus

class Button_ESC3:
    def __init__(self, rect, command, **kwargs):
        self.process_kwargs(kwargs)
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.function = command
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def process_kwargs(self, kwargs):
        settings = {
            'color': pygame.Color(122, 197, 205),
            'text': 'Quit',
            'font': pygame.font.SysFont('Comic Sans MS', int(y_global * 0.025)),
            'hover_color': (83,134,139),
            'font_color': pygame.Color('white'),
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)
button_ESC3 = Button_ESC3(((x_global * 0.5 - x_global * 0.1 * 0.5),(y_global * 0.74), (x_global * 0.1), (y_global * 0.07)), command=None)  #asukoht, suurus

def draw(vasaktorn, paremtorn, vasakud_elud, paremad_elud, vasak1, vasak2, vasak3, vasak4, vasak5, vasak6, vasak7, vasak8,\
         parem1, parem2, parem3, parem4, parem5, parem6, parem7, parem8):

    global vasakud_coinid
    global paremad_coinid
    if vasakud_coinid < 999:
        vasakud_coinid += 0.1
    if paremad_coinid < 999:
        paremad_coinid += 0.1

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
    mängu_screen.blit(vasak1, (0, 0))
    mängu_screen.blit(vasak2, ((int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasak3, (2 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasak4, (3 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasak5, (4 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(vasak6, (5 * (int(0.05 * x_global) + 5), 0))
    mängu_screen.blit(parem6, (x_global - int(0.05 * x_global), 0))
    mängu_screen.blit(parem5, (x_global - 2 * (int(0.05 * x_global)) - 5, 0))
    mängu_screen.blit(parem4, (x_global - 3 * (int(0.05 * x_global)) - 10, 0))
    mängu_screen.blit(parem3, (x_global - 4 * (int(0.05 * x_global)) - 15, 0))
    mängu_screen.blit(parem2, (x_global - 5 * (int(0.05 * x_global)) - 20, 0))
    mängu_screen.blit(parem1, (x_global - 6 * (int(0.05 * x_global)) - 25, 0))

    mängu_screen.blit(vasak7, (0, int(0.1 * y_global) + 5))
    mängu_screen.blit(vasak8, ((int(0.1 * x_global) + 5), int(0.1 * y_global) + 5))
    mängu_screen.blit(parem8, (x_global - int(0.1 * x_global), int(0.1 * y_global) + 5))
    mängu_screen.blit(parem7, (x_global - 2 * (int(0.1 * x_global)) - 5, int(0.1 * y_global) + 5))

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

    basicfont1 = pygame.font.SysFont("Arial", int(x_global * 0.036))
    text1 = basicfont1.render(str(round(vasakud_coinid)), True, (139, 117, 0))
    mängu_screen.blit(text1, (0.04 * x_global, 0.415* y_global))

    basicfont2 = pygame.font.SysFont("Arial", int(x_global * 0.036))
    text2 = basicfont2.render(str(round(paremad_coinid)), True, (139, 117, 0))
    mängu_screen.blit(text2, (0.95 * x_global, 0.415 * y_global))

    pygame.display.update()

def draw_game_over(t):
    mängu_screen.blit(t, (0, 0))
    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.55 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_play_again.draw(mängu_screen)
    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.645 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_mainmenu1.draw(mängu_screen)
    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.74 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_ESC2.draw(mängu_screen)
    pygame.display.update()


def draw_start_screen():
    mängu_screen.blit(start_screen, (0, 0))
    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.55 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  #asukoht, suurus
    button_play.draw(mängu_screen)
    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.645 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_instructions.draw(mängu_screen)
    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.74 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_ESC1.draw(mängu_screen)
    pygame.display.update()

def draw_instructions():
    mängu_screen.blit(instructions, (0, 0))
    pygame.draw.rect(mängu_screen, (0, 0, 0), [0, 0, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_back.draw(mängu_screen)
    pygame.display.update()

def draw_pause():
    paus = pygame.image.load("images/paus/paus.png")
    paus = pygame.transform.scale(paus, (x_global, y_global))
    paus = pygame.transform.smoothscale(paus, (x_global, y_global))
    mängu_screen.blit(paus, (0, 0))

    paused_font = pygame.font.SysFont("Comic Sans MS", int(x_global * 0.1))
    paused = paused_font.render("Paused", True, (139, 117, 0))
    paused_rect = paused.get_rect(center=(x_global / 2, y_global / 2))
    mängu_screen.blit(paused, paused_rect)

    global valik
    if len(sõnumid[valik]) < 90:
        m = 0.02
    else:
        m = 0.01
    sõnum_font = pygame.font.SysFont("Comic Sans MS", int(x_global * m))
    sõnum = sõnum_font.render(sõnumid[valik], True, (139, 117, 0))
    sõnum_rect = sõnum.get_rect(center=(x_global / 2, y_global / 2))
    mängu_screen.blit(sõnum, (sõnum_rect[0], sõnum_rect[1] + y_global * 0.1))


    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.645 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_mainmenu2.draw(mängu_screen)
    pygame.draw.rect(mängu_screen, (0, 0, 0), [x_global * 0.5 - (x_global * 0.1 + 10) * 0.5, y_global * 0.74 - 5, (x_global * 0.1 + 10), (y_global * 0.07 + 10)])  # asukoht, suurus
    button_ESC1.draw(mängu_screen)

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
b_parem = 3
b_vasak = 3
pausi_arv = 0
mängumuusika = 0
mittemängumuusika = 0

#viivitus tegelaste lisamiseks, 1- vasak   2-parem
tegelane1_aeg = tegelane_lisamis_delay
tegelane2_aeg = tegelane_lisamis_delay


while a:
    dt = clock.tick(FPS) / 1000

    k1 = pygame.sprite.groupcollide(player_list1, parem_torn_sprite, False, False, collided=None)
    for i in k1:
        player_list1.remove(i)
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b_parem = 1
    k2 = pygame.sprite.groupcollide(player_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k2:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        player_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b_vasak = 1
    k3 = pygame.sprite.groupcollide(knight_list1, parem_torn_sprite, False, False, collided=None)
    for i in k3:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        knight_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b_parem = 1
    k4 = pygame.sprite.groupcollide(knight_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k4:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        knight_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b_vasak = 1
    k5 = pygame.sprite.groupcollide(skeleton_list1, parem_torn_sprite, False, False, collided=None)
    for i in k5:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        skeleton_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b_parem = 1
    k6 = pygame.sprite.groupcollide(skeleton_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k6:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        skeleton_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b_vasak = 1
    k7 = pygame.sprite.groupcollide(eye_list1, parem_torn_sprite, False, False, collided=None)
    for i in k7:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        eye_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b_parem = 1
    k8 = pygame.sprite.groupcollide(eye_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k8:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        eye_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b_vasak = 1
    k9 = pygame.sprite.groupcollide(orc_list1, parem_torn_sprite, False, False, collided=None)
    for i in k9:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        orc_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b_parem = 1
    k10 = pygame.sprite.groupcollide(orc_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k10:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        orc_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b_vasak = 1
    k11 = pygame.sprite.groupcollide(wizard_list1, parem_torn_sprite, False, False, collided=None)
    for i in k11:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        wizard_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b_parem = 1
    k12 = pygame.sprite.groupcollide(wizard_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k12:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
        wizard_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b_vasak = 1
    k13 = pygame.sprite.groupcollide(lillakuul_list1, parem_torn_sprite, False, False, collided=None)
    for i in k13:
        lillakuul_list1.remove(i)
        if muusika == 0:
            pygame.mixer.Channel(0).fadeout(1000)
    k14 = pygame.sprite.groupcollide(lillakuul_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k14:
        lillakuul_list2.remove(i)
        if muusika == 0:
            pygame.mixer.Channel(0).fadeout(1000)
    k15 = pygame.sprite.groupcollide(punanekuul_list1, parem_torn_sprite, False, False, collided=None)
    for i in k15:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
            channel4.play(kuul_tornivastu)
        punanekuul_list1.remove(i)
        parema_torni_elud -= 1
        if parema_torni_elud == 0:
            b_parem = 1
    k16 = pygame.sprite.groupcollide(punanekuul_list2, vasak_torn_sprite, False, False, collided=None)
    for i in k16:
        if muusika == 0:
            pygame.mixer.Sound.play(torni_pihtasaamine)
            channel4.play(kuul_tornivastu)
        punanekuul_list2.remove(i)
        vasaku_torni_elud -= 1
        if vasaku_torni_elud == 0:
            b_vasak = 1

    #b_vasak ja b_parem:
        #b = 3 - start screen
        #b = 0 - mäng
        #b = 1 - end screen
        #b = 2 - instructions
        #b = 4 - paus
    for event in pygame.event.get():
        cursor = pygame.mouse.get_pos()

        #Play vajutamine
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and b_vasak == 3 and b_parem == 3 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.55) <= cursor[1] <= (y_global * 0.55 + y_global * 0.07):
            b_parem = 0
            b_vasak = 0
            paremad_coinid = 0
            vasakud_coinid = 0
            vasaku_torni_elud = 5
            parema_torni_elud = 5
            player_list2.empty()
            player_list1.empty()
            knight_list2.empty()
            knight_list1.empty()
            skeleton_list2.empty()
            skeleton_list1.empty()
            orc_list2.empty()
            orc_list1.empty()
            eye_list2.empty()
            eye_list1.empty()
            wizard_list2.empty()
            wizard_list1.empty()
            lillakuul_list2.empty()
            lillakuul_list1.empty()
            punanekuul_list2.empty()
            punanekuul_list1 .empty()

        #Instructons vajutamine
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and b_vasak == 3 and b_parem == 3 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.645) <= cursor[1] <= (y_global * 0.645 + y_global * 0.07):
            b_parem = 2
            b_vasak = 2

        #Quit vajutamine 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and b_vasak == 3 and b_parem == 3 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.74) <= cursor[1] <= (y_global * 0.74 + y_global * 0.07):
            a = False

        #Back vajutamine, instructionite alt
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and b_vasak == 2 and b_parem == 2 \
        and 5 <= cursor[0] <= x_global * 0.1 + 5 \
        and 5 <= cursor[1] <= (y_global * 0.07 + 5):
            b_vasak = 3
            b_parem = 3


        #play again vajutamine
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.55) <= cursor[1] <= (y_global * 0.55 + y_global * 0.07):
            if b_vasak == 1 or b_parem == 1:
                vasaku_torni_elud = 5
                parema_torni_elud = 5
                b_parem = 0
                b_vasak = 0
                paremad_coinid = 0
                vasakud_coinid = 0
                player_list2.empty()
                player_list1.empty()
                knight_list2.empty()
                knight_list1.empty()
                skeleton_list2.empty()
                skeleton_list1.empty()
                orc_list2.empty()
                orc_list1.empty()
                eye_list2.empty()
                eye_list1.empty()
                wizard_list2.empty()
                wizard_list1.empty()
                lillakuul_list2.empty()
                lillakuul_list1.empty()
                punanekuul_list2.empty()
                punanekuul_list1.empty()

        #mainmenu vajutamine1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.645) <= cursor[1] <= (y_global * 0.645 + y_global * 0.07):
            if b_vasak == 1 or b_parem == 1:
                b_parem = 3
                b_vasak = 3

        #Quit vajutamine 2
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.74) <= cursor[1] <= (y_global * 0.74 + y_global * 0.07):
            if b_vasak == 1 or b_parem == 1:
                a = False

        # vajutamine
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and 5 <= cursor[1] <= (5 + y_global * 0.07) and b_vasak == 4 and b_parem == 4:
            print("laall")


        #PAUSI NUPP
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pausi_arv % 2 == 0 and b_parem == 0 and b_vasak == 0:
                pausi_arv += 1
                pygame.image.save(mängu_screen, "images/paus/paus.png")
                b_vasak = 4
                b_parem = 4
                sõnumid_pikkus = len(sõnumid)
                valik = random.randint(0, sõnumid_pikkus - 1)
            elif event.key == pygame.K_SPACE and pausi_arv % 2 != 0 and b_vasak == 4 and b_parem == 4:
                pausi_arv += 1
                b_vasak = 0
                b_parem = 0

        #mainmenu vajutamine2
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and b_vasak == 4 and b_parem == 4 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.645) <= cursor[1] <= (y_global * 0.645 + y_global * 0.07):
            b_parem = 3
            b_vasak = 3
            pausi_arv += 1

        #Quit vajutamine 3
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and b_vasak == 4 and b_parem == 4 \
        and (x_global * 0.5 - x_global * 0.1 * 0.5) <= cursor[0] <= (x_global * 0.5 - x_global * 0.1 * 0.5 + x_global * 0.1) \
        and (y_global * 0.74) <= cursor[1] <= (y_global * 0.74 + y_global * 0.07):
            a = False



        #tegelaste nupud
        if event.type == pygame.KEYDOWN and b_vasak == 0 and b_parem == 0:
            if event.key == pygame.K_q and vasakud_coinid >= 5:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    player1()
                    vasakud_coinid -= 5
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_u and paremad_coinid >= 5:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    player2()
                    paremad_coinid -= 5
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_e and vasakud_coinid >= 15:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    knight1()
                    vasakud_coinid -= 15
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_o and paremad_coinid >= 15:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    knight2()
                    paremad_coinid -= 15
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_w and vasakud_coinid >= 10:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    skeleton1()
                    vasakud_coinid -= 10
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_i and paremad_coinid >= 10:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    skeleton2()
                    paremad_coinid -= 10
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_s and vasakud_coinid >= 25:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    eye1()
                    vasakud_coinid -= 25
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_k and paremad_coinid >= 25:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    eye2()
                    paremad_coinid -= 25
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_a and vasakud_coinid >= 20:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    orc1()
                    vasakud_coinid -= 20
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_j and paremad_coinid >= 20:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    orc2()
                    paremad_coinid -= 20
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_d and vasakud_coinid >= 30:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    wizard1()
                    vasakud_coinid -= 30
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_l and paremad_coinid >= 30:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    wizard2()
                    paremad_coinid -= 30
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_z and vasakud_coinid >= 100:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    lillakuul1()
                    vasakud_coinid -= 100
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_n and paremad_coinid >= 100:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    lillakuul2()
                    paremad_coinid -= 100
                    tegelane2_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_x and vasakud_coinid >= 100:
                if tegelane1_aeg == tegelane_lisamis_delay:
                    punanekuul1()
                    vasakud_coinid -= 100
                    tegelane1_aeg -= tegelane_lisamis_delay
            if event.key == pygame.K_m and paremad_coinid >= 100:
                if tegelane2_aeg == tegelane_lisamis_delay:
                    punanekuul2()
                    paremad_coinid -= 100
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


    if round(vasakud_coinid) < 5:
        vasak1 = vasakud_tuhm1
    else:
        vasak1 = vasakud_ikoonid1
    if round(vasakud_coinid) < 10:
        vasak2 = vasakud_tuhm2
    else:
        vasak2 = vasakud_ikoonid2
    if round(vasakud_coinid) < 15:
        vasak3 = vasakud_tuhm3
    else:
        vasak3 = vasakud_ikoonid3
    if round(vasakud_coinid) < 20:
        vasak4 = vasakud_tuhm4
    else:
        vasak4 = vasakud_ikoonid4
    if round(vasakud_coinid) < 25:
        vasak5 = vasakud_tuhm5
    else:
        vasak5 = vasakud_ikoonid5
    if round(vasakud_coinid) < 30:
        vasak6 = vasakud_tuhm6
    else:
        vasak6 = vasakud_ikoonid6
    if round(vasakud_coinid) < 100:
        vasak7 = vasakud_tuhm7
    else:
        vasak7 = vasakud_ikoonid7
    if round(vasakud_coinid) < 100:
        vasak8 = vasakud_tuhm8
    else:
        vasak8 = vasakud_ikoonid8


    if round(paremad_coinid) < 5:
        parem1 = paremad_tuhm1
    else:
        parem1 = paremad_ikoonid1
    if round(paremad_coinid) < 10:
        parem2 = paremad_tuhm2
    else:
        parem2 = paremad_ikoonid2
    if round(paremad_coinid) < 15:
        parem3 = paremad_tuhm3
    else:
        parem3 = paremad_ikoonid3
    if round(paremad_coinid) < 20:
        parem4 = paremad_tuhm4
    else:
        parem4 = paremad_ikoonid4
    if round(paremad_coinid) < 25:
        parem5 = paremad_tuhm5
    else:
        parem5 = paremad_ikoonid5
    if round(paremad_coinid) < 30:
        parem6 = paremad_tuhm6
    else:
        parem6 = paremad_ikoonid6
    if round(paremad_coinid) < 100:
        parem7 = paremad_tuhm7
    else:
        parem7 = paremad_ikoonid7
    if round(paremad_coinid) < 100:
        parem8 = paremad_tuhm8
    else:
        parem8 = paremad_ikoonid8

    #otsustab millist ekraani näidata
    if b_parem == 3 and b_vasak == 3:
        mittemängumuusika += 1
        if muusika == 0 and mittemängumuusika == 1:
            channel3.play(mittemäng_muusika, loops=-1)
            #paneb taustamuusika 50% peale
            channel3.set_volume(0.5)
        draw_start_screen()
        mängumuusika = 0
        channel2.stop()
    if b_parem == 0 and b_vasak == 0:
        mittemängumuusika = 0
        channel3.stop()
        draw(vasaktorn, paremtorn, vasakud_elud, paremad_elud, vasak1, vasak2, vasak3, vasak4, vasak5,
             vasak6, vasak7, vasak8, parem1, parem2, parem3, parem4, parem5, parem6, parem7, parem8)
        mängumuusika += 1
        channel2.unpause()
        if muusika == 0 and mängumuusika == 1:
            channel2.play(mäng_muusika, loops=-1)
            #paneb taustamuusika volüümi 10% peale
            channel2.set_volume(0.2)
    if b_parem == 1:
        mittemängumuusika += 1
        if muusika == 0 and mittemängumuusika == 1:
            channel3.play(mittemäng_muusika, loops=-1)
        t = game_over_parempool
        draw_game_over(t)
        mängumuusika = 0
        channel2.stop()
    if b_vasak == 1:
        mittemängumuusika += 1
        if muusika == 0 and mittemängumuusika == 1:
            channel3.play(mittemäng_muusika, loops=-1)
        t = game_over_vasakpool
        draw_game_over(t)
        mängumuusika = 0
        channel2.stop()
    if b_parem == 2 and b_vasak == 2:
        draw_instructions()
        mängumuusika = 0
        channel2.stop()
    if b_vasak == 4 and b_parem == 4:
        draw_pause()
        channel2.pause()

#    1 on vasakpoolsed ja 2 on parempoolsed
    if tegelane1_aeg < tegelane_lisamis_delay:
        tegelane1_aeg += 1
    if tegelane2_aeg < tegelane_lisamis_delay:
        tegelane2_aeg += 1
pygame.quit()

#meelespea:
#hetkel kui nõrgem võidab siis tuleb coine juurde, sama tugevad on vastakuti või siis tugevam võidab nõrgemat- siis ei tule coine juurde
