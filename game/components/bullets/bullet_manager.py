import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, SPACESHIP_TYPE


class BulletManager:
    def __init__(self):
        self.spaceship_bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] = []

    def update(self, game):
        enemies = game.enemy_manager.get_enemies()
        for spaceship_bullet in self.spaceship_bullets:
            spaceship_bullet.update(self.spaceship_bullets)
            for enemy in enemies:
                if spaceship_bullet.rect.colliderect(enemy.rect):
                    self.spaceship_bullets.remove(spaceship_bullet)
                    game.stats.score += 1
                    game.enemy_manager.remove_enemy(enemy)
                    break
                
        for bullet_enemy in self.enemy_bullets:
            bullet_enemy.update(self.enemy_bullets)
                #Checks if we are colliding with a player
            if bullet_enemy.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet_enemy)
                game.playing = False
                game.stats.death_count += 1
                game.stats.add_score()
                pygame.time.delay(1000)
                break

    def draw(self, screen):
        for bullet in self.spaceship_bullets + self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == SPACESHIP_TYPE and len(self.spaceship_bullets) < 3:
            self.spaceship_bullets.append(bullet)