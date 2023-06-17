import pygame

from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import DEFAULT_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP,  SPACESHIP_TYPE


class Spaceship(Sprite):
    
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = SPACESHIP_TYPE
        self.power_up = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0

    def update(self, game, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)

    def move_left(self):
        self.rect.x -= 10
        if self.rect.left <= -20:
            self.rect.x = SCREEN_WIDTH - 20
        
    def move_right(self):
        self.rect.x += 10
        if self.rect.right >= SCREEN_WIDTH + 20 :
            self.rect.x = -20

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def set_image(self, size=(75, 75), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset_power_up(self):
        self.power_up = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0
        self.set_image()