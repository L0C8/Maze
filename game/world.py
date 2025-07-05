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

                if maze[y][x] == 0:
                    self.add_floor(xpos, ypos)
                    self.add_ceiling(xpos, ypos)
                else:
                    self.add_walls_for_cell(x, y, maze, rows, cols)

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

    def add_wall_segment(self, x, y, h):
        cm = CardMaker('wall')
        cm.set_frame(-0.5, 0.5, -0.5, 0.5)
        wall = self.node.attach_new_node(cm.generate())
        wall.set_texture(self.wall_tex)
        wall.set_pos(x, y, TILE_SIZE / 2)
        wall.set_h(h)
        wall.set_scale(TILE_SIZE)
        wall.set_two_sided(True)

    def add_walls_for_cell(self, cx, cy, maze, rows, cols):
        xpos = cx * TILE_SIZE
        ypos = cy * TILE_SIZE

        # North (+y)
        if cy + 1 >= rows or maze[cy + 1][cx] == 0:
            self.add_wall_segment(xpos, ypos + TILE_SIZE / 2, 0)

        # South (-y)
        if cy - 1 < 0 or maze[cy - 1][cx] == 0:
            self.add_wall_segment(xpos, ypos - TILE_SIZE / 2, 180)

        # West (-x)
        if cx - 1 < 0 or maze[cy][cx - 1] == 0:
            self.add_wall_segment(xpos - TILE_SIZE / 2, ypos, 90)

        # East (+x)
        if cx + 1 >= cols or maze[cy][cx + 1] == 0:
            self.add_wall_segment(xpos + TILE_SIZE / 2, ypos, -90)
