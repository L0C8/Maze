import os
from panda3d.core import (
    TextureStage, Texture, NodePath, CardMaker, LVector3, Filename
)

TILE_SIZE = 1.0 
ASSET_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets')

class World:
    def __init__(self, maze_data):
        self.node = NodePath("MazeRoot")
        self.load_textures()
        self.build_maze(maze_data)

    def load_textures(self):
        self.wall_tex = loader.loadTexture(Filename.from_os_specific(os.path.join(ASSET_DIR, "wall.png")))
        self.floor_tex = loader.loadTexture(Filename.from_os_specific(os.path.join(ASSET_DIR, "floor.png")))
        self.ceil_tex = loader.loadTexture(Filename.from_os_specific(os.path.join(ASSET_DIR, "ceiling.png")))

    def build_maze(self, maze):
        rows = len(maze)
        cols = len(maze[0])
        for y in range(rows):
            for x in range(cols):
                xpos = x * TILE_SIZE
                ypos = y * TILE_SIZE

                self.add_floor(xpos, ypos)
                self.add_ceiling(xpos, ypos)

                if maze[y][x] == 1:
                    self.add_wall(xpos, ypos)

    def add_floor(self, x, y):
        cm = CardMaker('floor')
        cm.set_frame(-0.5, 0.5, -0.5, 0.5)
        card = self.node.attach_new_node(cm.generate())
        card.set_texture(self.floor_tex)
        card.set_pos(x, y, 0)
        card.set_hpr(0, -90, 0)

    def add_ceiling(self, x, y):
        cm = CardMaker('ceiling')
        cm.set_frame(-0.5, 0.5, -0.5, 0.5)
        card = self.node.attach_new_node(cm.generate())
        card.set_texture(self.ceil_tex)
        card.set_pos(x, y, TILE_SIZE)
        card.set_hpr(0, 90, 0)

    def add_wall(self, x, y):
        cube = self.node.attach_new_node("wall")

        faces = [
            ((0, 0, 0), (0, 0.5, 0)),      # front
            ((180, 0, 0), (0, -0.5, 0)),   # back
            ((90, 0, 0), (-0.5, 0, 0)),    # left
            ((-90, 0, 0), (0.5, 0, 0)),    # right
        ]
        for hpr, offset in faces:
            cm = CardMaker('side')
            cm.set_frame(-0.5, 0.5, -0.5, 0.5)
            face = cube.attach_new_node(cm.generate())
            face.set_texture(self.wall_tex)
            face.set_pos(*offset)
            face.set_hpr(*hpr)
            face.set_two_sided(True) 

        cube.set_scale(TILE_SIZE)
        cube.set_pos(x, y, TILE_SIZE / 2)