import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
window = pygame.display.set_mode((1300,700))
pygame.display.set_caption("Undersea Adventure","Undersea Adventure")
pygame.key.set_repeat(1,1)

def drawText(text, size, color, centerX, centerY):
    font=pygame.font.Font("comicSansMS.ttf", size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

background = pygame.image.load("backGround.gif")
clam = pygame.image.load("clam.gif")
bubble = pygame.image.load("bubble.gif")

shipUP = clam
shipLEFT = pygame.transform.rotate(shipUP, 90.0)
shipDOWN = pygame.transform.rotate(shipLEFT, 90.0)
shipRIGHT = pygame.transform.rotate(shipDOWN, 90.0)
shipX = randint(0,1234)
shipY = randint(0,634)
speed = 1
ticks = 0
ship = shipUP
inU = 0
inD = 0
inR = 0
inL = 0
bubble1 = False
bubble2 = False
bubble3 = False
bubbleDelayAmount = 100
bubbleDelay = -bubbleDelayAmount-1
shooters = 1

while True:
    
    ticks+=1
    mousePos=pygame.mouse.get_pos()
    mousePressed=pygame.mouse.get_pressed()

    bubbleAimX=(mousePos[0]+shipX)/2
    bubbleAimY=(mousePos[1]+shipY)/2
    #Bubble Shooting
    if sum(mousePressed) > 0 and ticks-bubbleDelay>bubbleDelayAmount/shooters:
            if not(bubble1):    
                bubble1 = True
                bubbleX1 = shipX-12
                bubbleY1 = shipY-12
                slope = 0
                b1x = 0
                b1y = 0
                if not(mousePos[0] == shipX):
                    slope = (mousePos[1]-shipY)/(mousePos[0]-shipX)
                if abs(slope) < 0.3:
                    b1x = 6
                    b1y = 0
                elif abs(slope) < 1:
                    b1x = 5
                    b1y = 2.5
                elif abs(slope) < 2:
                    b1x = 3.2
                    b1y = 3.2
                elif abs(slope) < 4:
                    b1x = 2.5
                    b1y = 5
                else:
                    b1x = 0
                    b1y = 6
                if mousePos[1] < shipY:
                        b1y *= -1
                if mousePos[0] < shipX:
                    b1x *= -1
                bubbleDelay = ticks
            elif not(bubble2) and shooters >= 2:
                bubble2 = True
                bubbleX2 = shipX-12
                bubbleY2 = shipY-12
                slope = 0
                b2x = 0
                b2y = 0
                if not(mousePos[0] == shipX):
                    slope = (mousePos[1]-shipY)/(mousePos[0]-shipX)
                if abs(slope) < 0.3:
                    b2x = 6
                    b2y = 0
                elif abs(slope) < 1:
                    b2x = 5
                    b2y = 2.5
                elif abs(slope) < 2:
                    b2x = 3.2
                    b2y = 3.2
                elif abs(slope) < 4:
                    b2x = 2.5
                    b2y = 5
                else:
                    b2x = 0
                    b2y = 6
                if mousePos[1] < shipY:
                    b2y *= -1
                if mousePos[0] < shipX:
                    b2x *= -1
                bubbleDelay = ticks
            elif not(bubble3) and shooters >= 3:
                bubble3 = True
                bubbleX3 = shipX-12
                bubbleY3 = shipY-12
                slope = 0
                b3x = 0
                b3y = 0
                if not(mousePos[0] == shipX):
                    slope = (mousePos[1]-shipY)/(mousePos[0]-shipX)
                if abs(slope) < 0.3:
                    b3x = 6
                    b3y = 0
                elif abs(slope) < 1:
                    b3x = 5
                    b3y = 2.5
                elif abs(slope) < 2:
                    b3x = 3.2
                    b3y = 3.2
                elif abs(slope) < 4:
                    b3x = 2.5
                    b3y = 5
                else:
                    b3x = 0
                    b3y = 6
                if mousePos[1] < shipY:
                    b3y *= -1
                if mousePos[0] < shipX:
                    b3x *= -1
                bubbleDelay = ticks
    #Event Detection
    for event in pygame.event.get():
        if (event.type==KEYUP and event.key==K_ESCAPE) or event.type==QUIT:
            pygame.quit()
            sys.exit()
                

                    
    #Movement
    keys=pygame.key.get_pressed()
    if keys[K_w]:
            if shipY > 90:
                shipY -= speed
                ship = shipUP
                inU += 0.1*speed
                inD -= 0.05*speed

    elif keys[K_s]:
            if shipY < 652:
                shipY += speed
                ship = shipDOWN
                inD += 0.1*speed
                inU -= 0.05*speed

    elif keys[K_a]:
            if shipX > 1:
                shipX -= speed
                ship = shipLEFT
                inL += 0.1*speed
                inR -= 0.05*speed

    elif keys[K_d]:
            if shipX < 1255:
                shipX += speed
                ship = shipRIGHT
                inR += 0.1*speed
                inL -= 0.05*speed
    #Inertia
    inU -= 0.05*speed
    inD -= 0.05*speed
    inL -= 0.05*speed
    inR -= 0.05*speed
    if inU<0:
        inU=0
    if inD<0:
        inD=0
    if inL<0:
        inL=0
    if inR<0:
        inR=0
    shipX += inR
    shipY += inD
    shipX -= inL
    shipY -= inU
    if shipY < 90:
        inU -= 0.1
        inD += 0.1
    if shipY > 668:
        shipY -= 1
        inU += 0.05
        inD -= 0.05
    if shipX < 32:
        shipX += 1
        inR += 0.05
        inL -= 0.05
    if shipX > 1268:
        shipX -= 1
        inL += 0.05
        inR -= 0.05

    window.blit(background,(0,0))

    if bubble1:
        bubbleX1 += b1x
        bubbleY1 += b1y
        window.blit(bubble, (bubbleX1, bubbleY1))
        if bubbleX1>1300 or bubbleX1<-24 or bubbleY1>700 or bubbleY1<-24:
            bubble1=False
    if bubble2:
        bubbleX2 += b2x
        bubbleY2 += b2y
        window.blit(bubble, (bubbleX2, bubbleY2))
        if bubbleX2>1300 or bubbleX2<-24 or bubbleY2>700 or bubbleY2<-24:
            bubble2=False
    if bubble3:
        bubbleX3 += b3x
        bubbleY3 += b3y
        window.blit(bubble, (bubbleX3, bubbleY3))
        if bubbleX3>1300 or bubbleX3<-24 or bubbleY3>700 or bubbleY3<-24:
            bubble3=False 
        
    window.blit(ship, (shipX-32, shipY-32))
    #pygame.draw.line(window, (0,0,0), (shipX,shipY), (bubbleAimX,bubbleAimY), 1)
    #aiming line
    pygame.display.update()
