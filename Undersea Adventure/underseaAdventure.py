import pygame, sys
from pygame.locals import *
from random import randint, uniform
from math import sqrt
from underseaMethods import *

pygame.init()
window = pygame.display.set_mode((1300,700))
pygame.display.set_caption("Undersea Adventure","Undersea Adventure")
pygame.key.set_repeat(1,1)

background = pygame.image.load("backGround.gif")
clam = pygame.image.load("clam.gif")
bubbleImage = pygame.image.load("bubble.gif")
fishImage = pygame.image.load("fish.gif")
urchinImage = pygame.image.load("urchin.gif")

ship = clam
shipX = randint(0,1234)
shipY = randint(0,634)
shipName = "Clam"
shooters = 1
speed = 0.5                         #INITIAL SPEED
ticks = 0
inU = 0
inD = 0
inR = 0
inL = 0
bubbles = []
#bubble = [Bubble X, Bubble Y, X-speed, Y-Speed]
bubbleDelayAmount = 100               #SINGLE BUBBLE CANNON FIRE RATE
bubbleDelay = -bubbleDelayAmount-1
fishes = []
#fish = [image, fish X, fishY, scale, speed]
#reward is speed rounded to whole number
fishChance =  250
rotationSpeed = 2
bubbleSpeed = 3                      #SPEED OF BUBBLES
degrees = randint(0,359)
cannonType = ''
bloops = 0
netshooters = 0
HP = 20
maxHP = 20
points = 0
capturedSpies = 0
minnowRounds = 0
cannons = 0

'''
enemies = []
#ENEMIES ARE LISTS STARTING WITH A TYPE AND INCLUDING  HP, SPEED, MOVEMENT PATTERNS, IMAGES, ETC
urchinstart = randint(0,2):
if urchinstart = 0:
    urchinX = -80
    urchinY = randint(60,700)
elif urchinstart = 1:
    urchinX = randint(-80,1380)
    urchinY = 700
else:
    urchinX = 1300
    urchinY = randint(60,700)

urchinHP = 50
urchinSpeed = 
    
URCHIN = [urchinX, urchinY,"URCHIN",urchinHP, urchinSpeed]
'''

while True:
    
    ticks+=1
    mousePos=pygame.mouse.get_pos()
    mousePressed=pygame.mouse.get_pressed()
    window.blit(background,(0,0))
    shipCheck(window, shooters, cannons, cannonType, bloops, netshooters, speed, HP, maxHP, points, capturedSpies, minnowRounds, shipName)

    #bubbleAimX=(mousePos[0]+shipX)/2
    #bubbleAimY=(mousePos[1]+shipY)/2
    '''
    #Make Fish 1
    if not(fish1OnScreen) and randint(0,150) == 1:
        fish1OnScreen = True
        if randint(0,1) == 0:
            direction = -1
            fish1X = 1300
            fish1 = fish1L
        else:
            direction = 1
            fish1X = -64
            fish1 = fish1R
        fish1Y = randint(0, 652)
    '''
    #Make Fish
    if randint(1,fishChance) == 1:
        scale = uniform(0.25,1.5)
        fishSpeed = 2/scale
        direction = ['left','right'][randint(0,1)]
        fishX = -128
        flip = False
        if direction == 'left':
            fishSpeed *= -1                                    
            fishX = 1300
            flip = True
        fishY = randint(64,700-round(42*scale))
        image = pygame.transform.scale(pygame.transform.flip(fishImage, flip, False), (round(64*scale), round(42*scale)))                         
        fishes.append([fishX, fishY, scale, fishSpeed, image])
    
    #Bubble Shooting
    if sum(mousePressed) > 0 and ticks-bubbleDelay>bubbleDelayAmount/shooters:
        bx = shipX+32 - mousePos[0] 
        by = shipY+32 - mousePos[1] 
        magnitude = sqrt(bx*bx+by*by) 
        bx /= magnitude 
        by /= magnitude
        bubbles.append([shipX+32, shipY+32, bx, by])
        bubbleDelay = ticks

    '''
    #Fish1 Stuff
    if fish1OnScreen:
        fish1X += direction
        window.blit(fish1, (fish1X, fish1Y))
        if fish1X < -65 or fish1X > 1301:
            fish1OnScreen = False
    '''
    for fish in fishes:
        fish[0]+=fish[3]
        window.blit(fish[4],(fish[0],fish[1]))
        
            
    #Event Detection
    for event in pygame.event.get():
        if (event.type==KEYUP and event.key==K_ESCAPE) or event.type==QUIT:
            done(window)
                

                    
    #Movement
    keys=pygame.key.get_pressed()
    if degrees > 359:
        degrees = 0
    if degrees < 0:
        degrees = 359
                    
    if keys[K_w]:
            if shipY > 90:
                inU += 0.1*speed
                inD -= 0.05*speed
            if 180 > degrees > 0:
                degrees -= rotationSpeed
            elif 360 > degrees > 180:
                degrees += rotationSpeed

    if keys[K_s]:
            if shipY < 652:
                inD += 0.1*speed
                inU -= 0.05*speed
            if 180 > degrees > 0:
                degrees += rotationSpeed
            elif 360 > degrees > 180:
                degrees -= rotationSpeed

    if keys[K_a]:
            if shipX > 1:
                inL += 0.1*speed
                inR -= 0.05*speed
            if 270 > degrees >= 90:
                degrees -= rotationSpeed
            else:
                degrees += rotationSpeed

    if keys[K_d]:
            if shipX < 1255:
                inR += 0.1*speed
                inL -= 0.05*speed
            if 270 >= degrees > 90:
                degrees += rotationSpeed
            else:
                degrees -= rotationSpeed
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
        
    for bubble in bubbles:
        bubble[0] -= bubbleSpeed*bubble[2]
        bubble[1] -= bubbleSpeed*bubble[3]
        window.blit(bubbleImage, (bubble[0],bubble[1]))
        if bubble[0]>1300 or bubble[0]<-24 or bubble[1]>700 or bubble[1]<-24:
            bubbles.remove(bubble)
        for fish in fishes:
            if fish[0]-24 < bubble[0] < fish[0]+(64*fish[2]) and fish[1]-24 < bubble[1] < fish[1]+(42*fish[2]):
                fishes.remove(fish)
                bubbles.remove(bubble)
            
    window.blit(pygame.transform.rotate(ship, degrees), (shipX, shipY))
    #pygame.draw.line(window, (0,0,0), (shipX,shipY), (bubbleAimX,bubbleAimY), 1)
    #aiming line
    pygame.display.update()
