from manimlib.imports import *

class DrawScenec(ThreeDScene):
    # ----- Surfaces
    CONFIG = {
        "zoomed_display_height": 3,
        "zoomed_display_width": 3
    }
    def construct(self):
        #self.begin_vertical_camera_rotation(.01)
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
            u = np.pi/2-0.03*t
            v = t
            return np.array((np.sin(u) * np.cos(v),
                             np.sin(u) * np.sin(v),
                             np.cos(u)))
        dotA = Dot()
        func = ParametricFunction(funca, t_max=8*TAU, fill_opacity=0)
        #func.scale(2.5)
        new_func = CurvesAsSubmobjects(func.copy())
        new_func.set_color_by_gradient(GREEN_A, GREEN_E)
        dotA.add_updater(lambda m: m.move_to(func.get_end()))
        func.fade(1)
        VGroup(new_func,func, cylinder).scale(3.5)
        self.wait()
        #self.play(Write(cylinder))
        self.add(dotA)

        self.play(
            ShowCreation(new_func),
            ShowCreation(func),
            run_time=10 ,rate_func= linear
        )


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "DrawSceneb"
    os.system(command_A + command_B)

