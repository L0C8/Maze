from direct.showbase.ShowBase import ShowBase
from game.world import World
from game.player import PlayerController
from utils.maze_gen import generate_maze

class PyMazeApp(ShowBase):
    def __init__(self):
        super().__init__()

        maze = generate_maze(32, 17)
        world = World(maze)
        world.node.reparent_to(self.render)

        self.player = PlayerController()
        self.player.node.reparent_to(self.render)

app = PyMazeApp()
app.run()
