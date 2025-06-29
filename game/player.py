# player.py
from panda3d.core import NodePath, Vec3

class PlayerController:
    def __init__(self):
        self.node = NodePath("player")
        self.node.set_pos(1, 1, 0.5)

        base.camera.reparent_to(self.node)
        base.camera.set_pos(0, 0, 0)
        base.camera.look_at(0, 1, 0)

    def move_forward(self, speed):
        self.node.set_pos(self.node, Vec3(0, speed, 0))

    def move_right(self, speed):
        self.node.set_pos(self.node, Vec3(speed, 0, 0))

    def rotate(self, angle_deg):
        self.node.set_h(self.node.get_h() + angle_deg)
