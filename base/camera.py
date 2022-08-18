from base.updatable import Updatable
from tools import TupleT


class Camera(Updatable):
    def __init__(self, game_scene, start_pos):
        self.__game_scene__ = game_scene
        self.__position__ = (0, 0)
        self.set_pos(start_pos)

    def move(self, delta_pos):
        self.set_pos(TupleT.add(self.get_pos(), delta_pos))

    def set_pos(self, pos):
        map_size_offset = 500
        map_size = TupleT.multiply_by_value(self.__game_scene__.map_size, self.__game_scene__.grid_size)
        map_size = TupleT.subtract(map_size, self.__game_scene__.main.screen.screen_size)
        map_size = TupleT.add_value(map_size, map_size_offset)
        x = pos[0]
        y = pos[1]

        if x < -map_size_offset:
            x = -map_size_offset
        if y < -map_size_offset:
            y = -map_size_offset
        if x > map_size[0]:
            x = map_size[0]
        if y > map_size[1]:
            y = map_size[1]

        self.__position__ = (x, y)

    def get_pos(self):
        return self.__position__

    def update(self, clock):
        for game_object in self.__game_scene__.game_objects:
            game_object.set_pos(TupleT.negative(self.get_pos()))
