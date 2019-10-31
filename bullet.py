import pygame
from constants import *
from helper import load_image

class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, x, y, image_name):
        super().__init__(group)
        self.group = group
        self.image = pygame.transform.scale(load_image(image_name), (BULLET_WIDTH, BULLET_HEIGHT))
        self.x = x
        self.y = y
        self.direction = 1

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.y
        self.rect.left = self.x - self.rect.width

    def update(self):
        self.rect.bottom += self.direction * STEP * 2
        if self.rect.bottom <= 0:
            self.group.remove(self)


class Bullet_enemy(Bullet):
    def __init__(self, group, x, y):
        super().__init__(group, x, y, 'bullet_enemy.png')
        self.rect.bottom = self.y + BULLET_HEIGHT

class Bullet_player(Bullet):
    def __init__(self, group, x, y):
        super().__init__(group, x, y, 'bullet_player.png')
        self.direction = -1