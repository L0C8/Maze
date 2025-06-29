from __future__ import annotations

import argparse
import os
import pygame

from game.world import World
from game.player import Player
from game.renderer import MazeRenderer

MOVE_MAP = {
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
}


def run(width: int, height: int) -> None:
    world = World.from_size(width, height)
    player = Player(1, 1)
    app = MazeRenderer(world, player)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("3D Maze")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in MOVE_MAP:
                    dx, dy = MOVE_MAP[event.key]
                    player.move(dx, dy, world)

        app.update_camera()
        app.task_mgr_step()
        pygame.display.flip()

    pygame.quit()


def main() -> None:
    parser = argparse.ArgumentParser(description="3D maze game")
    parser.add_argument("width", type=int, nargs="?", default=21)
    parser.add_argument("height", type=int, nargs="?", default=21)
    args = parser.parse_args()
    run(args.width, args.height)


if __name__ == "__main__":
    main()
