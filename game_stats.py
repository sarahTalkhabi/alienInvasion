import pygame
from pygame.sprite import Sprite 

class GameStats:
   def __init__(self, al_game):
        super().__init__()
        
        self.settings = al_game.settings
        self.reset_stats()
        self.high_score = 0 
        
   def reset_stats(self):
      self.ships_left = self.settings.ship_limit
      self.score = 0 
      self.level = 1   
    
        
      