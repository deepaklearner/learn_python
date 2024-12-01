import pygame
import sys

class rocket_game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("rocket game")
        screen.fill(color=(100,100,100))

    def run(self):
        while(True):
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ =="__main__":
    game_obj = rocket_game()
    game_obj.run()


                



    