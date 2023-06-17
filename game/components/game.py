import pygame

from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.powerups.power_up_manager import PowerUpManager
from game.components.spaceship import Spaceship
from game.components.stats import Stats

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.stats = Stats()
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu("-- Press any key to start --", text_size=35)
        self.power_up_manager = PowerUpManager()

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while not self.playing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.reset_play()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(self, user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score(self.screen)
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.stats.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)

    def show_menu(self):
        if self.stats.death_count > 0:
            self.menu.update_message(f"-- Press any key to restart the game --")
            self.menu.update_stats(f"Score: {self.stats.score}   Max score: {self.stats.max_score}   Deaths: {self.stats.death_count}")
        self.menu.draw(self.screen)
        self.menu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False

    def reset_play(self):
        self.enemy_manager.reset()
        self.stats.reset_stats()
        self.power_up_manager.reset()