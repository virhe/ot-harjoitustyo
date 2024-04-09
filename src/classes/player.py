import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self, keys, walls):
        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            dy = -5
        if keys[pygame.K_s]:
            dy = 5
        if keys[pygame.K_a]:
            dx = -5
        if keys[pygame.K_d]:
            dx = 5

        self.rect.x += dx
        collision = pygame.sprite.spritecollideany(self, walls)
        if collision:
            self.rect.x -= dx

        self.rect.y += dy
        collision = pygame.sprite.spritecollideany(self, walls)
        if collision:
            self.rect.y -= dy
