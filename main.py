#Nathan Hinton
#This will be an ide game. hopefuly...

#Starting with a tutuorial from online:
#https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python
import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
keys = [False, False, False, False]
playerPos = [100, 100]
screen = pygame.display.set_mode((width, height))

playerImg = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

while 1:
    screen.fill(0)
    #Set bg:
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass, (x*100, y*100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    #Draw player:
    screen.blit(playerImg, playerPos)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #Check for key press:
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    keys[0] = True
                elif event.key == K_a:
                    keys[1] = True
                elif event.key == K_s:
                    keys[2] = True
                elif event.key == K_d:
                    keys[3] = True
            if event.type == pygame.KEYUP:
                if event.key == K_w:
                    keys[0] = False
                elif event.key == K_a:
                    keys[1] = False
                elif event.key == K_s:
                    keys[2] = False
                elif event.key == K_d:
                    keys[3] = False
