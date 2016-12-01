import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
window = pygame.display.set_mode((1300,700))
pygame.display.set_caption("Undersea Adventure","Undersea Adventure")
pygame.key.set_repeat(1,1)

def drawText(text, size, color, centerX, centerY):
    font=pygame.font.Font("PressStart2P.ttf", size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

background = pygame.image.load("backGround.gif")

while True:

    window.blit(background,(0,0))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if (event.type==KEYUP and event.key==K_ESCAPE)or event.type==QUIT:
            pygame.quit()
            sys.exit()
