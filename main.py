import sys
import pygame
from constants import *
from helper import load_image
from player import Player
from random import randint
from enemy import Enemy
from camera import Camera
from obstacle import Obstacle

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
player_bullets_group = pygame.sprite.Group()
enemies_bullets_group = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()

for i in range(50):
    Obstacle(obstacles_group)

background = pygame.transform.scale(load_image('background.jpg'), (WIDTH, HEIGHT * 2))
camera = Camera(background.get_rect().h)
player = Player(player_group, player_bullets_group, enemies_group, enemies_bullets_group, obstacles_group)

running = True

font = pygame.font.Font(None, 30)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            player_group.update(event)

    prev_dy = camera.dy
    camera.update(player)

    if prev_dy != camera.dy:
        for sprite in obstacles_group:
            camera.apply(sprite)

    if randint(1, 130) % 40 == 0:
        Enemy(enemies_group, player_bullets_group, enemies_bullets_group, player)

    screen.fill(pygame.Color(0, 0, 0))
    screen.blit(background, (0, camera.dy - HEIGHT // 2))

    enemies_group.update()
    enemies_bullets_group.update()
    player_bullets_group.update()
    player_group.update()

    enemies_group.draw(screen)
    enemies_bullets_group.draw(screen)
    player_bullets_group.draw(screen)
    player_group.draw(screen)
    obstacles_group.draw(screen)

    string_rendered = font.render(f'Life {player.life}', 1, pygame.Color('white'))
    rect = string_rendered.get_rect()
    rect.top = 10
    rect.x = 10
    screen.blit(string_rendered, rect)

    pygame.display.flip()

    clock.tick(FPS)

    if player.life <= 0:
        string_rendered = font.render(f'GAME OVER', 1, pygame.Color('white'))
        rect = string_rendered.get_rect()
        rect.top = HEIGHT // 2
        rect.x = WIDTH // 2 - rect.w // 2
        screen.blit(string_rendered, rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        break

pygame.quit()
sys.exit()