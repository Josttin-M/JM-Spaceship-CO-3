import pygame
from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:
    
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self, message, stats_message="", text_size = 30):
        self.font = pygame.font.Font(FONT_STYLE, text_size)
        self.icon = pygame.transform.scale(ICON, (100, 95))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        self.update_message(message)
        self.update_stats(stats_message)

    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()

    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        screen.blit(self.stats_message, self.stats_message_rect)
        pygame.display.update()

    def update_text(self, message, center_pos):
        text = self.font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=center_pos)
        return text, text_rect

    def update_message(self, message):
        self.message = message
        self.text, self.text_rect = self.update_text(message, (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT))

    def update_stats(self, stats_message):
        self.stats_message = stats_message
        self.stats_message, self.stats_message_rect = self.update_text(stats_message, (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100))