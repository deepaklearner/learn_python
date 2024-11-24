import pygame

class Ship:
    """ A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        # self.rect.midbottom = self.screen_rect.center
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update the ship position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
        