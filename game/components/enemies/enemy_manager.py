from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self):
        if not self.enemies: # [] {} 0 "" -> false | [1] {1: 1} 1 -2 "a" -> true
            self.enemies.append(Enemy())
            self.enemies.append(Enemy_2())

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)