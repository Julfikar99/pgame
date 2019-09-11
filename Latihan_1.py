import pygame, sys

from pygame.locals import *


# Latihan untuk pemrograman game
# untuk kelas semester VII InfoUMMU

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

while True: # main game loop

    for event in pygame.event.get():

        if event.type == QUIT:

            pygame.quit()

            sys.exit()

    pygame.display.update()
