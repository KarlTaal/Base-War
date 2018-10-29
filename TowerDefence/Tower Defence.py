import pygame
import ctypes
import time

pygame.init()


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
    mehike_walkRight.append(pygame.transform.scale(mehike, (int(0.15 * x_global), int(0.15 * y_global))))
    
def mehike():
    mängu_screen.blit(mehike_walkRight[0], (0.3 * x_global, 0.75 * y_global))      #praegu esitab listist ainult esimest elementi aga oleks vaja et esitab pilte listist järjest ja iga järgmise pildi natuke paremale, et jääks mulje et kõnniks edasi
        


def draw():
    #loob kujutised
    mängu_screen.blit(taust, (0, 0))
    if keys[pygame.K_DOWN]:
        mehike()
    mängu_screen.blit(vasak_torn, (0, 0.635 * y_global))
    mängu_screen.blit(parem_torn, (x_global - int(0.15 * y_global), 0.635 * y_global))
    pygame.display.update()
    
a = True
while a:        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        a = False
    draw()
    
pygame.quit()