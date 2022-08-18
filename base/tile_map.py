from base.game_object import GameObject
from base.updatable import Updatable
from tools import TupleT


class TileMap(GameObject, Updatable):
    def __init__(self, grid_size, auto_scale):
        self.__position__ = (0, 0)
        self.__tiles__ = {}
        self.grid_size = grid_size
        self.__auto_scale__ = auto_scale

    def put_sprite(self, sprite_template, tile_pos):
        sprite = sprite_template.copy()
        if self.__auto_scale__:
            self.auto_scale(sprite)

        pos = self.get_pos_of_tile(tile_pos)
        sprite.rects["main"].x = pos[0]
        sprite.rects["main"].y = pos[1]
        self.__tiles__[tile_pos] = sprite

    def fill(self, tile_pos0, tile_pos1, sprite_template):
        for x in range(tile_pos0[0], tile_pos1[0]+1):
            for y in range(tile_pos0[1], tile_pos1[1]+1):
                self.put_sprite(sprite_template, (x, y))

    # tile pos -> sprite (tile)
    def get_tile(self, tile_pos):
        return self.__tiles__[tile_pos]

    # pos in px -> tile pos
    def get_tile_pos(self, pos):
        return TupleT.devide_by_value(pos, self.grid_size)

    # tile pos -> pos in px
    def get_pos_of_tile(self, tile_pos):
        pos = TupleT.multiply_by_value(tile_pos, self.grid_size)
        pos = TupleT.add(pos, self.get_pos())
        return pos

    def auto_scale(self, sprite):
        sprite.scale(self.grid_size)

    def move(self, delta_pos):
        for tile_pos in self.__tiles__:
            sprite = self.get_tile(tile_pos)
            for rect_name in sprite.rects:
                sprite.rects[rect_name].x += delta_pos[0]
                sprite.rects[rect_name].y += delta_pos[1]
        self.__position__ = TupleT.add(self.get_pos(), delta_pos)

    def set_pos(self, pos):
        delta = TupleT.subtract(pos, self.get_pos())
        self.move(delta)

    def get_pos(self):
        return self.__position__

    def update(self, clock):
        for tile_pos in self.__tiles__:
            if isinstance(self.get_tile(tile_pos), Updatable):
                self.get_tile(tile_pos).update(clock)

    def draw(self, screen):
        for tile_pos in self.__tiles__:
            self.get_tile(tile_pos).draw(screen)
