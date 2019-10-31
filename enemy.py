import pygame
from constants import *
from helper import load_image
from bullet import Bullet_enemy
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, player_bullets_group, enemies_bullets_group, player):
        super().__init__(group)
        self.group = group
        self.player_bullets_group = player_bullets_group
        self.enemies_bullets_group = enemies_bullets_group
        self.image = pygame.transform.scale(load_image('enemy.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.start_x = randint(PLAYER_WIDTH // 2, WIDTH - PLAYER_WIDTH // 2)
        self.start_y = PLAYER_HEIGHT
        self.player = player

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.start_y
        self.rect.left = self.start_x - self.rect.width

    def update(self):
        self.rect.bottom += STEP
        if pygame.sprite.spritecollideany(self, self.player_bullets_group):
            self.group.remove(self)
            self.player.life += 1
            return

        if self.rect.bottom >= HEIGHT:
            self.group.remove(self)
            return

        if randint(1, 100) % 20 == 0:
            Bullet_enemy(self.enemies_bullets_group, self.rect.left + PLAYER_WIDTH // 2, self.rect.bottom)