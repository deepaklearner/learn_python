import pygame
import sys

class rocket_game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("rocket game")
        self.screen.fill(color=(100,100,100))

    def run(self):
        while(True):
            image2 = pygame.image.load("rocket.png")
            pygame.display.flip()
            pygame.Surface.blit(self.screen,image2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ =="__main__":
    game_obj = rocket_game()
    game_obj.run()


                



    