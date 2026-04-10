"""methods and settings related to in-game projectile
Author: Dmitrii Dolgov
Date: 4/9/2026
    """
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Holds settings and methods for a standard bullet

    Args:
        Sprite : image of a bullet, .png
    """
    def __init__(self, game:"AlienInvasion")->None:
        """references the screen and game settings, links the sprites,
        sets up the size of the sprite used

        Args:
            game (AlienInvasion): active game instance
        """
        super().__init__()
        self.screen=game.screen
        self.settings=game.settings

        self.image=pygame.image.load(self.settings.bullet_file)
        self.image=pygame.transform.scale(self.image,(self.settings.bullet_w, self.settings.bullet_h))
        self.image=pygame.transform.rotate(self.image,270)

        self.rect=self.image.get_rect()
        self.rect.midleft=game.ship.rect.midleft
        self.x = float(self.rect.x)

    def update(self)->None:
        """updates the position of a bullet
        """
        self.x+=self.settings.bullet_speed
        self.rect.x=self.x
    
    def draw_bullet(self)->None:
        """draws the bullet on a screen
        """
        self.screen.blit(self.image, self.rect)