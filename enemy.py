import pygame
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, face_right):
        pygame.sprite.Sprite.__init__(self)
        if face_right:
            self.image = pygame.transform.scale(pygame.image.load("characters/Char 01/Idle/skeleton-Idle_0.png"), (width, height))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load("characters/Char 01/Idle/skeleton-Idle_0.png"), (width, height)), True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.jumping = False
        self.gravity = 10
        self.facing_right = face_right
        self.height = height
        self.width = width
        self.frame = 0
        self.animation = ""

    def move(self):
        if self.rect.y < (700-(self.height/2)) and not self.jumping:
            self.rect.y += self.gravity
            self.gravity += 1
        elif self.rect.y >= (700-(self.height/2)):
            self.rect.y = 700-(self.height/2)
            self.gravity = 10
            self.jumping = False
        if self.rect.x > 0 and not self.facing_right:
            self.rect.x -= self.speed
        else:
            self.kill()




    def update(self):
        self.move()