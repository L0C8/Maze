from __future__ import annotations
from dataclasses import dataclass
from typing import List

from utils.maze_gen import generate_maze, Cell


@dataclass
class World:
    maze: List[List[Cell]]

    @classmethod
    def from_size(cls, width: int, height: int) -> "World":
        maze = generate_maze(width, height)
        return cls(maze)

    @property
    def width(self) -> int:
        return len(self.maze[0]) if self.maze else 0

    @property
    def height(self) -> int:
        return len(self.maze)

    def is_wall(self, x: int, y: int) -> bool:
        return self.maze[y][x] == "#"
