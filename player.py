import pygame
from sprites import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, facing_right):
        pygame.sprite.Sprite.__init__(self)
        if facing_right:
            self.image = pygame.transform.scale(sprites["Char 19"]["Idle"][0], (width, height))
        else:
            self.image = pygame.transform.flip(pygame.transform.scale(sprites["Char 19"]["Idle"][0], (width, height)), True, False)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.jumping = False
        self.jumping2 = False
        self.gravity = 10
        self.height = height
        self.width = width
        self.facing_right = facing_right
        self.count = 0
        self.double_jump_unlocked = False
        self.fuel = 100
        self.jetpack_unlocked = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and not self.jumping2 and not self.jetpack_unlocked:
            if not self.jumping:
                self.jumping = True
                self.rect.y -= 10
                self.gravity = -12
            elif self.jumping and self.count > 8 and self.double_jump_unlocked:
                self.gravity = -14
                self.jumping2 = True
        elif self.jetpack_unlocked and keys[pygame.K_UP] and self.fuel > 0:
            if self.rect.y < 300:
                self.rect.y = 300
            else:
                self.rect.y -= 1
                self.gravity = -3
                self.fuel -= .5
        if self.rect.y < (700-(self.height/2)) and not self.jumping:
            self.rect.y += self.gravity
            self.gravity += 1
        elif self.rect.y >= (700-(self.height/2)):
            self.rect.y = 700-(self.height/2)
            self.gravity = 10
            self.jumping = False
            self.jumping2 = False
        elif self.jumping:
            self.rect.y += self.gravity*2
            self.gravity += 1

    def update(self):
        pass

    def draw(self, root):
        self.move()
        root.blit(self.image, self.rect)
        if self.jumping:
            self.count += 1
        else:
            self.count = 0