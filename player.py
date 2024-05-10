import pygame

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5
JUMP_HEIGHT = 15

class Player(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height,white):
        super().__init__()
        self._screen_width = screen_width
        self._screen_height = screen_height
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = self._screen_width // 2
        self.rect.bottom = screen_height - 10
        self.vel_y = 0
        self.jumping = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = -JUMP_HEIGHT
            self.jumping = True

        # Apply gravity
        self.vel_y += 1
        self.rect.y += self.vel_y
        if self.rect.bottom >= self._screen_height - 10:
            self.rect.bottom = self._screen_height - 10
            self.jumping = False
