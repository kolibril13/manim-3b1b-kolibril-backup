from manimlib.imports import *

class DrawScene(ThreeDScene):
    # ----- Surfaces
    def construct(self):

        self.set_camera_orientation(phi=45 * DEGREES)
        self.camera.frame_center.shift(3.5 * LEFT)
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5)  # Resolution of the surfaces
        self.add(cylinder.scale(2))
        dot = Dot()

        def func(t):
            return np.array((np.cos( t), np.sin( t), 1))

        func = ParametricFunction(func, t_max=TAU, fill_opacity=0)
        func.scale(2)
        new_func = CurvesAsSubmobjects(func.copy())
        new_func.set_color_by_gradient(BLUE, WHITE, RED)
        dot.add_updater(lambda m: m.move_to(func.get_end()))
        func.fade(1)
        self.add(dot)
        text = TexMobject(r" S_1(",r"t",r")= R \left( \begin{array}{c} cos(\omega t) \\ sin(\omega t)\\ 0 \end{array} \right)+ \left( \begin{array}{c} 0 \\ 0\\ 1 \end{array} \right) ")
        text.to_corner(LEFT).shift(3.5*LEFT)
        text2 = text.copy()
        text[1].set_color(BLUE)
        self.add_fixed_in_frame_mobjects(text)
        text2[1].set_color(RED)

        text3= TexMobject("t = [","0",",","  \\frac{2\pi}{\omega}","]")
        text3[1].set_color(BLUE)
        text3[3].set_color(RED)
        text3.next_to(text2,DOWN)
        self.add_fixed_in_frame_mobjects(text3)
        self.wait()
        self.play(
            ShowCreation(new_func),
            ShowCreation(func),
            Transform(text, text2),
            run_time=3.5
        )
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "DrawScene"
    os.system(command_A + command_B)

