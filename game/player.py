from panda3d.core import NodePath, Vec3
from direct.showbase.DirectObject import DirectObject
from panda3d.core import WindowProperties


MOUSE_SENSITIVITY = 0.2
MOVE_SPEED = 5

class PlayerController(DirectObject):

    def __init__(self):
        super().__init__()

        self.node = NodePath("player")
        self.node.set_pos(1, 1, 0.5)
        self.node.set_scale(0.5)
        # Attach the player node to the scene graph so the
        # camera (which will be parented to this node) is part
        # of the world. Without this the view remains grey and
        # none of the input works because the camera is not
        # rendering any objects.
        self.node.reparent_to(render)

        base.camera.reparent_to(self.node)
        base.camera.set_pos(0, 0, 0)
        base.camera.set_hpr(0, 0, 0)

        self.key_map = {"w": False, "s": False, "a": False, "d": False}
        for key in self.key_map:
            self.accept(key, self.set_key, [key, True])
            self.accept(f"{key}-up", self.set_key, [key, False])

        self.props = WindowProperties()
        self.center = None
        self.disable_mouse_look()

        taskMgr.add(self.update, "player-update")

    def disable_mouse_look(self):
        base.disable_mouse()
        self.props.setCursorHidden(True)
        base.win.requestProperties(self.props)
        self.center = (base.win.get_x_size() // 2, base.win.get_y_size() // 2)
        base.win.movePointer(0, *self.center)

    def set_key(self, key, value):
        self.key_map[key] = value

    def update(self, task):
        dt = globalClock.get_dt()
        speed = MOVE_SPEED * dt

        if self.key_map["w"]:
            self.node.set_pos(self.node, Vec3(0, speed, 0))
        if self.key_map["s"]:
            self.node.set_pos(self.node, Vec3(0, -speed, 0))
        if self.key_map["a"]:
            self.node.set_pos(self.node, Vec3(-speed, 0, 0))
        if self.key_map["d"]:
            self.node.set_pos(self.node, Vec3(speed, 0, 0))

        if base.mouseWatcherNode.hasMouse():
            pointer = base.win.get_pointer(0)
            dx = pointer.get_x() - self.center[0]
            dy = pointer.get_y() - self.center[1]
            self.node.set_h(self.node.get_h() - dx * MOUSE_SENSITIVITY)
            base.camera.set_p(clamp(base.camera.get_p() - dy * MOUSE_SENSITIVITY, -90, 90))
            base.win.movePointer(0, *self.center)

        return task.cont


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))
