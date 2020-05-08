from manimlib.imports import *

class RotationsIn3d(Scene):
    def construct(self):
        def func(time):
            param = ParametricFunction(
                lambda u: np.array([
                    2 * u ** 2,
                    4 * u,
                    0
                ]), color=RED, t_min=0, t_max=1)
            return param
        curve1 = func(0)
        curve2 = curve1.copy()
        def update_curve(d,dt):
            d.rotate_about_origin(dt)
        def update_curve_back(d,dt):
            d.rotate_about_origin(-dt)
        curve2.add_updater(update_curve)
        self.add(curve1,curve2)
        self.wait(PI/2)
        curve2.remove_updater(update_curve)
        curve2.add_updater(update_curve_back)
        self.wait(PI/2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "RotationsIn3d"
    os.system(command_A + command_B)
