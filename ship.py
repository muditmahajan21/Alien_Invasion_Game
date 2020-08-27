import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #Class to manage ship.
    def __init__(self, ai_game):
        #Initialise and set the starting position of ship.

        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Start the new ship at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        #Movement flag.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        #Draw ship at its current location.
        self.screen.blit(self.image, self.rect)

    def update(self):
        #Update the ship's movement based on movement flag.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        #Create the ship on the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)