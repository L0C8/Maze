# main.py
from direct.showbase.ShowBase import ShowBase
from game.world import World
from game.player import PlayerController
from utils.maze_gen import generate_maze

class PyMazeApp(ShowBase):
    def __init__(self):
        super().__init__()
        
        maze, start, end = generate_maze(11, 11)

        # -------- debug ---------------------------------------
        print("Maze size:", len(maze), "x", len(maze[0]))
        print("Start:", start, "End:", end)
        # ------------------------------------------------------
        for y, row in enumerate(maze):
            line = ""
            for x, cell in enumerate(row):
                if (x, y) == start:
                    line += "S"
                elif (x, y) == end:
                    line += "E"
                else:
                    line += "." if cell == 0 else "#"
            print(line)

        self.world = World(maze)
        self.world.node.reparent_to(self.render)

        self.disable_mouse()

        self.player = PlayerController()
        self.player.node.set_pos(start[0], start[1], 0.5)

app = PyMazeApp()
app.run()
