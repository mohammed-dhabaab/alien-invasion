import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__() # super(Bullet, self).__init__() # Python 2.7 syntax
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and get its rect.
        self.image = pygame.image.load('.\\assets\\spaceships\\alien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Positioning the alien:
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        # Movement flag
        # self.moving_right = False
        # self.moving_left = False
        # self.moving_top = False
        # self.moving_down = False
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True