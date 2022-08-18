from base.drawable import Drawable
from tools import TupleT


class GameObject(Drawable):
    def move(self, delta_pos):
        self.set_pos(TupleT.add(self.get_pos(), delta_pos))

    def set_pos(self, pos):
        pass

    def get_pos(self):
        return []
