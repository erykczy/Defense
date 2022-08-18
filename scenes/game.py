import pygame.image

from base.camera import Camera
from base.scene import Scene
from base.sprite import AnimatedSprite, Sprite
from base.tile_map import TileMap
from tools import TupleT


class Game(Scene):
    def __init__(self, main):
        super(Game, self).__init__(main)
        self.__camera_speed__ = 20
        self.__background_tile_map__ = None
        self.__tile_map__ = None
        self.__camera__ = None
        self.grid_size = 60 #60
        self.map_size = (40, 40)
        self.game_objects = []

    def start(self):
        screen = self.main.screen

        # CAMERA INITIALIZATION
        offset = 1
        camera_pos = TupleT.add_value(self.map_size, offset)
        camera_pos = TupleT.devide_by_value(camera_pos, 2)
        camera_pos = TupleT.multiply_by_value(camera_pos, self.grid_size)
        camera_pos = TupleT.round(camera_pos)
        #center = (round((self.map_size[0] + offset) / 2 * self.grid_size), round((self.map_size[1] + offset) / 2 * self.grid_size))
        self.__camera__ = Camera(self, (camera_pos[0]-round(screen.screen_size[0]/2), camera_pos[1]-round(screen.screen_size[1]/2)))

        # CREATING TILE MAPS
        self.__tile_map__ = TileMap(self.grid_size, True)
        self.__background_tile_map__ = TileMap(self.grid_size, True)

        # PUTTING BACKGROUND TILES
        background_surface = pygame.image.load("images\\tiles\\background.png").convert_alpha()
        self.__background_tile_map__.fill((0, 0), self.map_size, Sprite({"main": background_surface}, {"main": background_surface.get_rect()}))

        map_border_surface = pygame.image.load("images\\tiles\\map_border.png").convert_alpha()
        map_border_sprite = Sprite({"main": map_border_surface}, {"main": map_border_surface.get_rect()})

        self.__background_tile_map__.fill((0, 0), (self.map_size[0], 0), map_border_sprite)
        self.__background_tile_map__.fill((0, 0), (0, self.map_size[1]), map_border_sprite)
        self.__background_tile_map__.fill((self.map_size[0], 0), (self.map_size[0], self.map_size[1]), map_border_sprite)
        self.__background_tile_map__.fill((0, self.map_size[1]), (self.map_size[0], self.map_size[1]), map_border_sprite)


        # PUTTING OBJECT TO DEFEND
        object_to_defend = AnimatedSprite({
            0: (pygame.image.load("images\\tiles\\money\\money0.png").convert_alpha(), 100*3),
            1: (pygame.image.load("images\\tiles\\money\\money1.png").convert_alpha(), 100*3),
            2: (pygame.image.load("images\\tiles\\money\\money0.png").convert_alpha(), 100*3),
            3: (pygame.image.load("images\\tiles\\money\\money2.png").convert_alpha(), 100*3),
            4: (pygame.image.load("images\\tiles\\money\\money0.png").convert_alpha(), 100*3),
            5: (pygame.image.load("images\\tiles\\money\\money3.png").convert_alpha(), 100*3),
            6: (pygame.image.load("images\\tiles\\money\\money0.png").convert_alpha(), 100*3),
            7: (pygame.image.load("images\\tiles\\money\\money4.png").convert_alpha(), 100),
            8: (pygame.image.load("images\\tiles\\money\\money5.png").convert_alpha(), 100),
            9: (pygame.image.load("images\\tiles\\money\\money6.png").convert_alpha(), 100),
            10: (pygame.image.load("images\\tiles\\money\\money7.png").convert_alpha(), 100),
            11: (pygame.image.load("images\\tiles\\money\\money8.png").convert_alpha(), 100),
            12: (pygame.image.load("images\\tiles\\money\\money9.png").convert_alpha(), 100),
            13: (pygame.image.load("images\\tiles\\money\\money10.png").convert_alpha(), 100),
            14: (pygame.image.load("images\\tiles\\money\\money11.png").convert_alpha(), 100),
            15: (pygame.image.load("images\\tiles\\money\\money12.png").convert_alpha(), 100)
        }, {"main": pygame.image.load("images\\tiles\\money\\money0.png").convert_alpha().get_rect()}, {})
        object_to_defend_pos = TupleT.devide_by_value(self.map_size, 2)
        object_to_defend_pos = TupleT.round(object_to_defend_pos)
        self.__tile_map__.put_sprite(object_to_defend, object_to_defend_pos)

        # REGISTRATION
        self.__drawables__.extend([self.__background_tile_map__, self.__tile_map__])
        self.__updatables__.extend([self.__background_tile_map__, self.__tile_map__, self.__camera__])
        self.game_objects.extend([self.__background_tile_map__, self.__tile_map__])

    def update(self, clock):
        # KEYS
        keys = pygame.key.get_pressed()

        # CAMERA MOVE
        if keys[pygame.K_w]:
            self.__camera__.move((0, -self.__camera_speed__))
        if keys[pygame.K_s]:
            self.__camera__.move((0, self.__camera_speed__))
        if keys[pygame.K_d]:
            self.__camera__.move((self.__camera_speed__, 0))
        if keys[pygame.K_a]:
            self.__camera__.move((-self.__camera_speed__, 0))

