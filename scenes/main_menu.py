import pygame.font

from base.button import Button
from base.scene import Scene
from base.text import Text
from scenes.game import Game


class MainMenu(Scene):
    def start(self):
        screen = self.main.screen

        # game title
        game_title = Text((0, 0), pygame.font.Font("fonts\\pixel_title.ttf", 100), "Defense", (255, 255, 255))
        game_title.pos = (screen.screen_size[0] / 2 - game_title.rects["main"].width / 2, 5)
        game_title.update_text()

        # level selector button
        level_selector_button_text = Text((0, 0), pygame.font.Font("fonts\\pixel.ttf", 100), "Level Selector",(255, 255, 255))
        level_selector_button_text.pos = (screen.screen_size[0] / 2 - level_selector_button_text.rects["main"].width / 2, 20 + game_title.rects["main"].x)
        level_selector_button_text.update_text()
        level_selector_button = Button(level_selector_button_text, (0, 255, 0, 200), self.level_selector_button_clicked)

        # settings button
        settings_button_text = Text((0, 0), pygame.font.Font("fonts\\pixel.ttf", 80), "Settings", (255, 255, 255))
        settings_button_text.pos = (screen.screen_size[0] / 2 - settings_button_text.rects["main"].width / 2, 80 + level_selector_button_text.rects["main"].x)
        settings_button_text.update_text()
        settings_button = Button(settings_button_text, (0, 255, 0, 200), self.settings_button_clicked)

        # quit button
        quit_button_text = Text((0, 0), pygame.font.Font("fonts\\pixel.ttf", 80), "Quit", (255, 255, 255))
        quit_button_text.pos = (screen.screen_size[0] / 2 - quit_button_text.rects["main"].width / 2, 80 + settings_button_text.rects["main"].x)
        quit_button_text.update_text()
        quit_button = Button(quit_button_text, (255, 0, 0, 200), self.quit_button_clicked)

        # registration
        self.__drawables__.extend([game_title, level_selector_button, settings_button, quit_button])
        self.__updatables__.extend([level_selector_button, settings_button, quit_button])

    def level_selector_button_clicked(self):
        self.main.set_current_scene(Game(self.main))

    def settings_button_clicked(self):
        pass

    def quit_button_clicked(self):
        self.main.safe_exit()
