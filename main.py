import pygame
from base.screen import Screen
from scenes import main_menu


class Main:
    def __init__(self):
        pygame.init()

        self.__max_time_left_to_quit__ = 1000 * 0.3
        self.__time_left_to_quit__ = self.__max_time_left_to_quit__

        self.__clock__ = pygame.time.Clock()
        self.screen = Screen((1280, 800), "Defense")

        self.__current_scene__ = None
        self.set_current_scene(main_menu.MainMenu(self))

        while True:
            self.update()

    def update(self):
        # UPDATING

        self.__current_scene__.update(self.__clock__)

        for updatable in self.__current_scene__.__updatables__:
            updatable.update(self.__clock__)

        # EVENTS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.safe_exit()

        # KEYS

        keys_pressed = pygame.key.get_pressed()

        # quiting
        if keys_pressed[pygame.K_ESCAPE]:
            if self.__time_left_to_quit__ <= 0:
                self.safe_exit()
            self.__time_left_to_quit__ -= self.__clock__.get_time()
        else:
            self.__time_left_to_quit__ = self.__max_time_left_to_quit__

        # GRAPHICS

        screen = self.screen.screen
        screen.fill((36, 36, 36))

        self.__current_scene__.draw(screen)

        pygame.display.update()

        # MISC

        self.__clock__.tick(60)

    def safe_exit(self):
        pygame.quit()
        exit()

    def set_current_scene(self, scene):
        self.__current_scene__ = scene
        scene.start()


Main()
