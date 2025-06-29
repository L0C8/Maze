import random

def generate_maze(width, height):
    width = width if width % 2 == 1 else width + 1
    height = height if height % 2 == 1 else height + 1

    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        maze[y][x] = 0
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if maze[ny][nx] == 1:
                    maze[y + dy // 2][x + dx // 2] = 0
                    carve(nx, ny)

    start = (1, 1)
    carve(*start)

    end = start
    for y in range(height - 2, 0, -1):
        for x in range(width - 2, 0, -1):
            if maze[y][x] == 0:
                end = (x, y)
                break
        if end != start:
            break

    return maze, start, end
