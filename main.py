from __future__ import annotations

import argparse

from game.world import World
from game.player import Player


MOVE_MAP = {
    "w": (0, -1),
    "s": (0, 1),
    "a": (-1, 0),
    "d": (1, 0),
}


def display(world: World, player: Player) -> None:
    for y, row in enumerate(world.maze):
        line = []
        for x, cell in enumerate(row):
            if x == player.x and y == player.y:
                line.append("P")
            else:
                line.append(cell)
        print("".join(line))


def run(width: int, height: int) -> None:
    world = World.from_size(width, height)
    player = Player(1, 1)

    while True:
        display(world, player)
        cmd = input("Move (w/a/s/d or q to quit): ").strip().lower()
        if cmd == "q":
            break
        if cmd in MOVE_MAP:
            dx, dy = MOVE_MAP[cmd]
            player.move(dx, dy, world)
        print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple maze game")
    parser.add_argument("width", type=int, nargs="?", default=21)
    parser.add_argument("height", type=int, nargs="?", default=21)
    args = parser.parse_args()
    run(args.width, args.height)


if __name__ == "__main__":
    main()
