import random
from typing import List

Cell = str


def generate_maze(width: int, height: int) -> List[List[Cell]]:
    """Generate a maze using depth-first search.

    Args:
        width: The maze width (must be odd).
        height: The maze height (must be odd).
    Returns:
        A 2D list where "#" represents a wall and " " represents a passage.
    """
    if width % 2 == 0 or height % 2 == 0:
        raise ValueError("Width and height must be odd numbers")

    maze: List[List[Cell]] = [["#" for _ in range(width)] for _ in range(height)]

    def neighbors(x: int, y: int) -> List[tuple[int, int]]:
        dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        out = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 < nx < width and 0 < ny < height:
                out.append((nx, ny))
        random.shuffle(out)
        return out

    stack = [(1, 1)]
    maze[1][1] = " "

    while stack:
        x, y = stack[-1]
        nbs = [n for n in neighbors(x, y) if maze[n[1]][n[0]] == "#"]
        if not nbs:
            stack.pop()
            continue
        nx, ny = nbs[0]
        maze[ny][nx] = " "
        maze[(ny + y) // 2][(nx + x) // 2] = " "
        stack.append((nx, ny))

    return maze
