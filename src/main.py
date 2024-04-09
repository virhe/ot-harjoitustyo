import sys
import pygame

from src.classes.player import Player
from src.classes.wall import Wall

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player()

walls = pygame.sprite.Group()
walls.add(Wall(0, 0, 800, 10))
walls.add(Wall(0, 0, 10, 600))
walls.add(Wall(790, 0, 10, 600))
walls.add(Wall(0, 590, 800, 10))

is_running = True
while is_running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()
    player.update(keys, walls)

    screen.fill((0, 0, 0))

    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (0, 0, 255), player.rect)

    pygame.display.update()

pygame.quit()
sys.exit()
