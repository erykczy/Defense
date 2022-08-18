import pygame.display


class Screen:
    screen = None
    screen_size = None

    def __init__(self, screen_size, screen_title):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(screen_title)
