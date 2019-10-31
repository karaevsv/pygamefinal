import pygame
from constants import *
from helper import load_image
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.group = group
        self.image = pygame.transform.scale(load_image('box.jpg'), (BOX_SIZE, BOX_SIZE))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = randint(BOX_SIZE // 2, WIDTH - BOX_SIZE // 2)
        self.rect.y = randint(-HEIGHT * 2, HEIGHT * 2)
        self.start_x = self.rect.x
        self.start_y = self.rect.y