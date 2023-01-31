import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, al_game):
        super().__init__()
        self.screen = al_game.screen
        self.settings = al_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_hight)
        self.rect.midtop = al_game.ship.rect.midtop

        self.y = float(self.rect.y)
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)