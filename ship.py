import pygame

class Ship:
    """ A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Start a decimal value for the ship horizontal position
        self.x = float(self.rect.x)
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update the ship position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x
        