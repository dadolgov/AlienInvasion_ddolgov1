"""Contains the arsenal data and methods: clip size, bullet drawing, update and removal.
Author:Dmitrii Dolgov
Date: 4/9/2026
    """
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """manages ship's weaponry
    """
    def __init__(self, game:'AlienInvasion')->None:
        """Takes references from the game instance and settings.

        Args:
            game (AlienInvasion): main game instance
        """
        self.game=game
        self.settings=game.settings
        self.arsenal=pygame.sprite.Group()

    def update_arsenal(self)->None:
        """updates bullet position and removes it once it reaches the end of screen
        """
        self.arsenal.update()
        self.remove_bullets_offscreen()

    def remove_bullets_offscreen(self)->None:
        """removes a bullet once it reaches the end of screen
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.left>=self.settings.screen_w:
                self.arsenal.remove(bullet)

    def draw(self)->None:
        """draws bullets on the screen
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self)->bool:
        """creates a bullet on the screen, if the ammount of bullets is below limit

        Returns:
            bool: returns True if the bullet was created.
                  returns False if maximum amount of bullets on screen was reached
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet=Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False