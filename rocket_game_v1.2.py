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
            x = self.screen.get_width() / 2 
            y = self.screen.get_height() / 2

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.KEYDOWN == pygame.K_RIGHT:
                        x +=  1
                
                pygame.draw.circle(self.screen, "red", pygame.Vector2(x , y), 40)
                pygame.display.flip()


                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ =="__main__":
    game_obj = rocket_game()
    game_obj.run()


                



    