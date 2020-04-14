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

        sphere = ParametricSurface(
            lambda u, v: np.array([
                np.sin(TAU*u)*np.cos(TAU*v),
                np.sin(TAU * u)*np.sin(TAU*v),
                np.cos(TAU*u)
            ]),
            resolution=(32, 32)).fade(0.9)  # Resolution of the surfaces
        def funca(r,u,v):
            return np.array((r*np.sin(u) * np.cos(v),
                             r*np.sin(u) * np.sin(v),
                             r*np.cos(u)))

        arrow = Line(funca(1,PI/4,-PI/3),funca(1.5,PI/4,-PI/3))
        final= VGroup(arrow, sphere).scale(3.5)
        self.add(final)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "DrawScenec"
    os.system(command_A + command_B)

