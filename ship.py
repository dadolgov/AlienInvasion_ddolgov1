"""ship controls and visuals
Author: Dmitrii Dolgov
Date: 4/9/2026
    """
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Handles movement, weapon management, boundary checking and ship sprite rendering
    """
    def __init__(self, game:"AlienInvasion", arsenal:"Arsenal")->None:
        """references game settings and screen parameters,
        creates a ship at the starting position,
        loads and processes the ship sprite file,
        links to the Arsenal class

        Args:
            game (AlienInvasion): active game instance
            arsenal (Arsenal): the arsenal class for weapon handling
        """
        self.game=game
        self.settings=game.settings
        self.screen=game.screen
        self.boundaries=self.screen.get_rect()

        self.image=pygame.image.load(self.settings.ship_file)
        self.image=pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))
        self.image = pygame.transform.rotate(self.image, 270)

        self.rect=self.image.get_rect()
        self.rect.midleft=self.boundaries.midleft
        self.moving_up=False
        self.moving_down=False
        self.y=float(self.rect.y)

        self.arsenal=arsenal

    def _center_ship(self):
        """resets the ship positionsing
        """
        self.rect.midleft=self.boundaries.midleft
        self.y=float(self.rect.y)

    def update(self):
        """updating the position of the ship and weapon status"""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """moves the within the screen boundaries
        """
        temp_speed=self.settings.ship_speed
        if self.moving_up and self.rect.top>self.boundaries.top:
            self.y-=temp_speed
        if self.moving_down and self.rect.bottom<self.boundaries.bottom:
            self.y+=temp_speed
        
        self.rect.y=self.y

    def draw(self)->None:
        """draws the ship and bullets on the screen
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)
    
    def fire(self)->bool:
        """attempts to create a bullet on the screen.

        Returns:
            bool: True if the bullet was created. False if bullet wasn't created due to 
            bullet amount limits
        """
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False

