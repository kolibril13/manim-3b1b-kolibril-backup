from manimlib.imports import *

class DrawScene(ThreeDScene):
    # ----- Surfaces
    CONFIG = {
        "zoomed_display_height": 3,
        "zoomed_display_width": 3
    }
    def construct(self):
        self.begin_vertical_camera_rotation(.01)
        self.set_camera_orientation(phi=40 * DEGREES)
        # self.camera.
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.sin(TAU*u)*np.cos(TAU*v),
                np.sin(TAU * u)*np.sin(TAU*v),
                np.cos(TAU*u)
            ]),
            resolution=(32, 32)).fade(0.9)  # Resolution of the surfaces
        #self.add(cylinder.scale(2.5))

        def funca(t):
            u = np.pi/2
            v = t
            return np.array((np.sin(u) * np.cos(v),
                             np.sin(u) * np.sin(v),
                             np.cos(u)))
        dotA = Dot()
        func = ParametricFunction(funca, t_max=TAU, fill_opacity=0)
        #func.scale(2.5)
        new_func = CurvesAsSubmobjects(func.copy())
        new_func.set_color_by_gradient(GREEN_A, GREEN_E)
        dotA.add_updater(lambda m: m.move_to(func.get_end()))
        func.fade(1)

        def funcb(t):
            u = np.pi/2-np.deg2rad(51)
            v = t
            return np.array((np.sin(u) * np.cos(v),
                             np.sin(u) * np.sin(v),
                             np.cos(u)))
        dotB = Dot()
        func2 = ParametricFunction(funcb, t_max=TAU, fill_opacity=0)
        #func2.scale(2.5)
        new_func2 = CurvesAsSubmobjects(func2.copy())
        new_func2.set_color_by_gradient(PURPLE_A, PURPLE_D)
        dotB.add_updater(lambda m: m.move_to(func2.get_end()))
        func2.fade(1)

        # text = TexMobject(r"\omega = \frac{2 \pi}{T} ")
        # text.to_corner(LEFT)
        # text2 = text.copy()
        # self.add_fixed_in_frame_mobjects(text)

        # text3= TexMobject("t = [","0",",","  \\frac{2\pi}{\omega}","]")
        # text3[1].set_color(BLUE)
        # text3[3].set_color(RED)
        # text3.next_to(text2,DOWN)
        # self.add_fixed_in_frame_mobjects(text3)
        VGroup(new_func,func, cylinder, new_func2, func2).scale(3.5)
        self.wait()
        self.play(Write(cylinder))
        self.add(dotA)
        self.add(dotB)

        self.play(
            ShowCreation(new_func),
            ShowCreation(func),
            ShowCreation(new_func2),
            ShowCreation(func2),
            run_time=3.5 ,rate_func= linear
        )
        self.play(
            ShowCreation(new_func),
            ShowCreation(func),
            ShowCreation(new_func2),
            ShowCreation(func2),
            run_time=3.5, rate_func=linear
        )
        self.play(
            ShowCreation(new_func),
            ShowCreation(func),
            ShowCreation(new_func2),
            ShowCreation(func2),
            run_time=3.5, rate_func=linear
        )
        self.wait(3)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "DrawScene"
    os.system(command_A + command_B)

