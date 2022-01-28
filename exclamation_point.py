import pygame

class Exclamation_point():
    
    def __init__(self, screen):
        """ Инициализирует и задает его начальную позицию."""
        self.screen = screen
        
        # Загрузка изображения и получения прямоугольника.
        self.image = pygame.image.load('images/chess-3413412_640.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Изображение в центре.
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        """ Рисует в текущей позиции."""
        self.screen.blit(self.image, self.rect)
