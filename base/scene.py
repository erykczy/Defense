from base.updatable import Updatable


class Scene(Updatable):
    def __init__(self, main):
        self.main = main
        self.__drawables__ = []
        self.__updatables__ = []

    def start(self):
        pass

    def draw(self, screen):
        for drawable in self.__drawables__:
            drawable.draw(screen)