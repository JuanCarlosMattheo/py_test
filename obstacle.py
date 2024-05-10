import pygame
import random

# Obstacle settings
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 5

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height,black):
        super().__init__()
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._black = black
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(self._black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self._screen_width - OBSTACLE_WIDTH)
        self.rect.y = -OBSTACLE_HEIGHT

    def update(self):
        self.rect.y += OBSTACLE_SPEED
        if self.rect.top > self._screen_height:
            self.rect.x = random.randint(0, self._screen_width - OBSTACLE_WIDTH)
            self.rect.y = -OBSTACLE_HEIGHT
            global score
            score += 1
