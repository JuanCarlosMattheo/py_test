import pygame
import random
import sys
from player import Player
from obstacle import Obstacle
from button import Button

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("JJ's Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

OBSTACLE_FREQ = 0.01  # Probability of obstacle appearance per frame

# Score
score = 0
font = pygame.font.Font(None, 36)

all_sprites = pygame.sprite.Group()
player = Player(SCREEN_WIDTH,SCREEN_HEIGHT,WHITE)
all_sprites.add(player)
obstacles = pygame.sprite.Group()
quit_button = Button(RED, 700, 10, 80, 40)
all_sprites = pygame.sprite.Group()
all_sprites.add(quit_button)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new obstacles with a certain probability
    if random.random() < OBSTACLE_FREQ:
        obstacle = Obstacle(SCREEN_WIDTH,SCREEN_HEIGHT,BLACK)
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

    # Update
    all_sprites.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, obstacles, True)
    for hit in hits:
        # Handle collision (e.g., decrease score)
        pass

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()