from manimlib.imports import *
# from active_projects.ode.part2.shared_constructs import *
from active_projects.diffyq.part2.shared_constructs import *
from hendrik_active.resusable_hendrik.histograms import *
from hendrik_active.resusable_hendrik.image_pro import *
class Ex1(ThreeDScene):
    def empty_k_space(self):
        PIXELS = 121
        square_ALL = [Square(fill_opacity=1, side_length=0.14) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % np.sqrt(PIXELS) == 0:
                j += 1
            k = i - j * np.sqrt(PIXELS)
            square_to_move.move_to((LEFT * k + j * DOWN) * 0.2)
        term = VGroup(*[square for square in square_ALL]).scale(3)
        return term

    def construct(self):
        term= self.empty_k_space()
        term.move_to(ORIGIN)
        term.set_color(BLACK)
        term.set_opacity(0.5)
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = TextMobject("This is a 3D text").scale(2).set_shade_in_3d(True)
        text3d.rotate(PI / 2, axis=RIGHT)
        self.add(axes, text3d,term)
        self.wait()
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s   -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Ex1"
    os.system(command_A + command_B)
