from dataclasses import dataclass


@dataclass
class Player:
    x: int
    y: int

    def move(self, dx: int, dy: int, world) -> None:
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < world.width and 0 <= ny < world.height:
            if not world.is_wall(nx, ny):
                self.x, self.y = nx, ny
