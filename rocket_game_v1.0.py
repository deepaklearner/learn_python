import pygame
import sys

if __name__ =="__main__":
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("rocket game")
    screen.fill(color=(100,100,100))

    while(True):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

                



    