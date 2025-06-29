from __future__ import annotations

import os
from panda3d.core import CardMaker
from direct.showbase.ShowBase import ShowBase


class MazeRenderer(ShowBase):
    """Render the maze using Panda3D."""

    def __init__(self, world, player):
        super().__init__()
        self.disableMouse()
        self.world = world
        self.player = player
        asset_dir = os.path.join(os.path.dirname(__file__), os.pardir, "assets")
        self.wall_tex = self.loader.loadTexture(os.path.join(asset_dir, "wall.png"))
        self.floor_tex = self.loader.loadTexture(os.path.join(asset_dir, "floor.png"))
        self._make_floor()
        self._make_walls()

    def _make_floor(self) -> None:
        cm = CardMaker("floor")
        cm.setFrame(0, self.world.width, 0, self.world.height)
        floor = self.render.attachNewNode(cm.generate())
        floor.setP(-90)
        floor.setPos(0, 0, 0)
        floor.setTexture(self.floor_tex)

    def _make_walls(self) -> None:
        for y, row in enumerate(self.world.maze):
            for x, cell in enumerate(row):
                if cell == "#":
                    self._add_wall(x, y)

    def _add_wall(self, x: int, y: int) -> None:
        cm = CardMaker("wall")
        cm.setFrame(0, 1, 0, 1)
        wall = self.render.attachNewNode(cm.generate())
        wall.setPos(x, y, 0)
        wall.setScale(1, 1, 1)
        wall.setTexture(self.wall_tex)
        wall.setH(0)

    def update_camera(self) -> None:
        self.camera.setPos(self.player.x + 0.5, self.player.y - 2, 1.5)
        self.camera.lookAt(self.player.x + 0.5, self.player.y + 0.5, 0.5)

    def task_mgr_step(self) -> None:
        self.taskMgr.step()
