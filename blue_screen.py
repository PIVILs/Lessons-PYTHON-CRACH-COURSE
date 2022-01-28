import sys

import pygame

from exclamation_point import Exclamation_point

def blue_screen():
    # Создает экран.
    screen = pygame.display.set_mode((1820, 980 ))
    pygame.display.set_caption("Exclamation point")
    bg_color = (137, 207, 240)
    
    exclamation_point = Exclamation_point(screen)
    
    while True:
        """ Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        exclamation_point.blitme()        
        # Отображение экрана
        pygame.display.flip()
        
        
blue_screen()
