import pygame
from pygame.sprite import Sprite

class Ship:
    


    def __init__(self,al_game):
        super().__init__()
        
        self.screen = al_game.screen
        self.settings = al_game.settings
        self.screen_rect = al_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed    
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x    
    def blitme(self):
        self.screen.blit(self.image, self.rect)    

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)