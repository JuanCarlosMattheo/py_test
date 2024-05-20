import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height, text=''):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.render_text()

    def render_text(self):
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Change text color to black
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.blit(text_surface, text_rect)

    def update(self):
        pass