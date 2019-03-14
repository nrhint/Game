#Nathan Hinton
#This will be an ide game. hopefuly...

#Starting with a tutuorial from online:
#https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python
import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

playerImg = pygame.image.load("resources/images/dude.png")

while 1:
    screen.fill(0)
    screen.blit(playerImg, (100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
