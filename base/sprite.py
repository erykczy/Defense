import pygame.transform

from base.drawable import Drawable
from base.updatable import Updatable


class Sprite(Drawable):
    def __init__(self, surfaces, rects):
        self.surfaces = surfaces
        self.rects = rects

    def draw(self, screen):
        for surface_name in self.surfaces:
            screen.blit(self.surfaces[surface_name], self.rects[surface_name])

    def copy(self):
        surfaces = {}
        rects = {}

        # coping surfaces
        for surface_name in self.surfaces:
            surfaces[surface_name] = self.surfaces[surface_name].copy()
        # coping animated rects
        for rect_name in self.rects:
            rects[rect_name] = self.rects[rect_name].copy()

        return Sprite(surfaces, rects)

    def scale(self, size):
        for surface_name in self.surfaces:
            self.surfaces[surface_name] = pygame.transform.scale(self.surfaces[surface_name], (size, size))


# ANIMATED SURFACES PARAMETER EXAMPLE:
# {
#      0: (surface, next_frame_delay),
#      1: (surface, next_frame_delay)
# }
class AnimatedSprite(Sprite, Updatable):
    def __init__(self, animated_surfaces, rects, surfaces):
        super().__init__(surfaces, rects)
        self.__animated_surfaces__ = animated_surfaces
        self.__current_frame__ = 0
        self.__frame_delay__ = self.__animated_surfaces__[self.__current_frame__][1]

    def update(self, clock):
        self.__frame_delay__ -= clock.get_time()
        if self.__frame_delay__ <= 0:
            self.__current_frame__ += 1
            if self.__current_frame__ == len(self.__animated_surfaces__):
                self.__current_frame__ = 0
            frame_info = self.__animated_surfaces__[self.__current_frame__]
            self.__frame_delay__ = frame_info[1]

    def scale(self, size):
        super(AnimatedSprite, self).scale(size)
        animated_surfaces = {}

        for frame in self.__animated_surfaces__:
            frame_info = self.__animated_surfaces__[frame]
            animated_surfaces[frame] = (pygame.transform.scale(frame_info[0], (size, size)), frame_info[1])

        self.__animated_surfaces__ = animated_surfaces

    def draw(self, screen):
        super(AnimatedSprite, self).draw(screen)

        frame_info = self.__animated_surfaces__[self.__current_frame__]
        surface = frame_info[0]
        screen.blit(surface, self.rects["main"])

    def copy(self):
        sprite = super(AnimatedSprite, self).copy()
        animated_surfaces = {}

        # coping animated surfaces
        for frame in self.__animated_surfaces__:
            frame_info = self.__animated_surfaces__[frame]
            animated_surfaces[frame] = (frame_info[0].copy(), frame_info[1])

        return AnimatedSprite(animated_surfaces, sprite.rects, sprite.surfaces)

