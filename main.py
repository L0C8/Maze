from direct.showbase.ShowBase import ShowBase
from game.world import World
from utils.maze_gen import generate_maze

class PyMazeApp(ShowBase):
    def __init__(self):
        super().__init__()

        maze = generate_maze(11, 11)
        world = World(maze)
        world.node.reparent_to(self.render)

        self.disable_mouse()
        self.camera.set_pos(1, 1, 0.5)
        self.camera.look_at(1, 2, 0.5)

app = PyMazeApp()
app.run()