import pygame
from constants import *
from helper import load_image
from bullet import Bullet_player

class Player(pygame.sprite.Sprite):
    def __init__(self, group, player_bullets_group, enemy_group, enemy_bullets_group, obstacles_group):
        super().__init__(group)
        self.player_bullets_group = player_bullets_group
        self.image = pygame.transform.scale(load_image('player.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.start_x = WIDTH // 2
        self.start_y = HEIGHT // 2
        self.motion = STOP
        self.enemy_group = enemy_group
        self.enemy_bullets_group = enemy_bullets_group
        self.obstacles_group = obstacles_group
        self.life = 100

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.respawn()

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_a:
                self.motion = LEFT
            if args[0].key == pygame.K_d:
                self.motion = RIGHT
            if args[0].key == pygame.K_w:
                self.motion = FORW
            if args[0].key == pygame.K_s:
                self.motion = BACKW
            if args[0].key == pygame.K_SPACE:
                Bullet_player(self.player_bullets_group, self.rect.left + PLAYER_WIDTH // 2, self.rect.top)

        if args and args[0].type == pygame.KEYUP:
            if args[0].key == pygame.K_a or args[0].key == pygame.K_d or args[0].key == pygame.K_w or \
                    args[0].key == pygame.K_s:
                self.motion = STOP

        if self.motion == LEFT:
            self.rect.x -= STEP
        elif self.motion == RIGHT:
            self.rect.x += STEP
        elif self.motion == FORW:
            self.rect.y -= STEP
        elif self.motion == BACKW:
            self.rect.y += STEP

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        if pygame.sprite.spritecollideany(self, self.enemy_group) or \
                pygame.sprite.spritecollideany(self, self.enemy_bullets_group) or \
                pygame.sprite.spritecollideany(self, self.obstacles_group):
            self.life -= 1
            self.respawn()

    def respawn(self):
        self.rect.bottom = self.start_y - self.rect.h // 2
        self.rect.left = self.start_x - self.rect.w // 2

