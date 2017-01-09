import pygame, sys
from pygame.locals import *
def drawText(window, text, size, color, left, top):
    font=pygame.font.Font("comicSansMS.ttf", size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.left=left
    textpos.top=top
    window.blit(renderedText, textpos)
def done(window):
    pygame.draw.line(window,(0,60,120),(0,350),(1300,350),200)
    drawText(window, "Are you sure you want to quit? Your Progress will not be saved.",42,(100,120,255),27,265)
    drawText(window, "Yes                 No",54,(100,120,255),433,345)
    pygame.draw.rect(window, (100,120,255), (424,355,110,65), 5)
    pygame.draw.rect(window, (100,120,255), (777,355,110,65), 5)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                break
        mousePos=pygame.mouse.get_pos()
        mousePressed=pygame.mouse.get_pressed()
        if mousePos[1]>355 and mousePos[1]<420 and mousePos[0]>777 and mousePos[0]<887 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            break
        if mousePos[1]>355 and mousePos[1]<420 and mousePos[0]>424 and mousePos[0]<534 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            pygame.quit()
            sys.exit(0)
def shipCheck(window, shooters, cannons, cannonType, bloops, netshooters, speed, HP, maxHP, points, capturedSpies, minnowRounds, shipName):
    pygame.draw.rect(window, (176,148, 122), (300,100,700,500), 0)
    drawText(window, "Name: "+shipName, 42, (0,0,0), 345, 125)
    drawText(window, "Bubble Shooters: "+str(shooters), 36, (0,0,0), 550, 200)
    drawText(window, "Cannons: "+str(cannons)+cannonType, 36, (0,0,0), 550, 200)
def buyShip(window, ship, points, capturesSpies):
    pass
    #Also need to import images
