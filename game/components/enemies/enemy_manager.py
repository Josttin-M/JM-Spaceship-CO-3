from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self, game):
        if not self.enemies: # [] {} 0 "" -> false | [1] {1: 1} 1 -2 "a" -> true
            self.enemies.append(Enemy())
            self.enemies.append(Enemy2())

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def get_enemies(self):
        return self.enemies
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)