from manimlib.imports import *


class FLOWER(ParametricSurface):
    CONFIG = {
        "resolution": (5, 10),
        "radius": 1,
        "u_min": 0.001,
        "u_max": PI - 0.001,
        "v_min": 0,
        "v_max": TAU,
    }

    def __init__(self, **kwargs):
        ParametricSurface.__init__(
            self, self.param_knosp,**kwargs
        )
        self.scale(self.radius)

    def param_knosp(self,u, v):
        x = np.sin(u) * np.cos(v)
        y = np.sin(u) * np.sin(v)
        z = u
        return np.array([x, y, z])

class FLOWERCHANGE(FLOWER):
    def __init__(self,**kwargs):
        FLOWER.__init__(self,**kwargs)

class Generation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        sphere=FLOWERCHANGE()


        axes = ThreeDAxes()
        self.add(sphere,axes)
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Generation"
    os.system(command_A + command_B)


