import pygame
import random
from player import Player
from enemy import Enemy
from sprites import *
from button import Button

pygame.init()
screen_width = 1200
screen_height = 800
root = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fight Things")

start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
FPS = 60
run = True
enemies = pygame.sprite.Group()
enemy1 = Enemy(screen_width, 100, 50, 50, False)
enemies.add(enemy1)
player = Player(100, 100, 50, 50, False)
def update_enemies():
    global start_time
    if ((pygame.time.get_ticks()- start_time)/1000) > random.randint(1, 3):
        start_time = pygame.time.get_ticks()
        enemies.add(Enemy(screen_width, 100, 50, 50, False))
def draw_window():
    root.fill((255, 255, 255))
    enemies.draw(root)
    enemies.update()
    player.draw(root)
    update_enemies()

start = False
def home_screen():
    root.fill((40, 40, 40))
    font = pygame.font.SysFont("comicsans", 100)
    text = font.render("Fight Things", 1, (255, 255, 255))
    root.blit(text, (screen_width/2 - text.get_width()/2, screen_height/10 - text.get_height()/2))
    button = Button(screen_width/2 - 100, screen_height/2 - 50, 200, 100, (255, 0, 0), "Start")
    button.draw(root)
    pos = pygame.mouse.get_pos()
    if button.is_over(pos):
        if pygame.mouse.get_pressed()[0]:
            global start
            start = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if start:
        draw_window()
    else:
        home_screen()
    pygame.display.update()

