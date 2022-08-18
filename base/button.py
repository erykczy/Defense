import pygame.mouse

from base.sprite import Sprite
from base.updatable import Updatable


class Button(Sprite, Updatable):
    def __init__(self, sprite, hover_color, click_event):
        super().__init__(sprite.surfaces, sprite.rects)
        self.__hover_color__ = hover_color
        self.__click_event__ = click_event

        # creating hover surface
        self.surfaces["hover"] = self.surfaces["main"].copy().convert_alpha()
        self.rects["hover"] = self.rects["main"].copy()

        # setting color of hover surface
        surface = self.surfaces["hover"]
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                if surface.get_at((x, y))[3] != 0:
                    surface.set_at((x, y), hover_color)

    def update(self, clock):
        if self.rects["main"].collidepoint(pygame.mouse.get_pos()):
            # hover
            if self.surfaces["hover"].get_alpha() != self.__hover_color__[3]:
                self.surfaces["hover"].set_alpha(self.__hover_color__[3])

            # click
            if pygame.mouse.get_pressed()[0]:
                if self.__click_event__ is not None:
                    self.__click_event__()
        else:
            self.surfaces["hover"].set_alpha(0)