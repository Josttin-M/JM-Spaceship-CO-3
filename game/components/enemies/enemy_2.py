import pygame
import random
import math
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = 'left'
RIGHT = 'right'

class Enemy_2(Sprite):
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_X = 4
    SPEED_Y = 0.4

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE

        self.movement = random.choice([LEFT, RIGHT])
        self.move_x = random.randint(30, 100)

    def update(self, ships):
        if self.movement == LEFT:
            self.rect.x -= self.SPEED_X
        else:
            self.rect.x += self.SPEED_X

        self.rect.y = self.Y_POS + int(50 * math.sin(self.rect.x / 50))
        self.Y_POS += self.SPEED_Y

        if self.rect.x >= SCREEN_WIDTH - 50 or self.rect.x <= 0:
            self.movement = LEFT if self.movement == RIGHT else RIGHT

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
