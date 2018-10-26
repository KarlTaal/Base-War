import pygame
import ctypes

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

#kast mida liigutada saab
x = 0
y = 0
width = 0.1 * x_global
height = 0.1 * y_global
vel = 10




a = True
while a:    
    pygame.time.delay(2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = False
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x = x - vel
    if keys[pygame.K_RIGHT]:
        x = x + vel
    if keys[pygame.K_UP]:
        y = y - vel
    if keys[pygame.K_DOWN]:
        y = y + vel
    if keys[pygame.K_ESCAPE]:
        a = False
        
    
    #loob kujutised
    mängu_screen.blit(taust, (0, 0))
    mängu_screen.blit(vasak_torn, (0, y_global- 0.365 * y_global))
    mängu_screen.blit(parem_torn, (x_global - int(0.15 * y_global), y_global- 0.365 * y_global))
    pygame.draw.rect(mängu_screen, (255, 0 , 0), (x, y ,width, height))
    pygame.display.update()
    

pygame.quit()