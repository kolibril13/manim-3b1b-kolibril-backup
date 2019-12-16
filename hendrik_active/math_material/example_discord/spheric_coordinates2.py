from manimlib.imports import *

class DrawScene(ThreeDScene):
    # ----- Surfaces
    CONFIG = {
        "zoomed_display_height": 3,
        "zoomed_display_width": 3
    }
    def construct(self):
        self.begin_vertical_camera_rotation(.1)
        self.set_camera_orientation(phi=40 * DEGREES)
        axes = ThreeDAxes()
        sphere = ParametricSurface(
            lambda u, v: np.array([
                np.sin(TAU*u)*np.cos(TAU*v),
                np.sin(TAU * u)*np.sin(TAU*v),
                np.cos(TAU*u)
            ]),
            resolution=(32, 32)).fade(0.9)  # Resolution of the surfaces

        self.add(sphere)

        def funca(u,v,r):
            return np.array((r*np.sin(u) * np.cos(v),
                             r*np.sin(u) * np.sin(v),
                             r*np.cos(u)))
        Dots_inner= VGroup()
        for i in range(0,10): #inner shell
            r = 1
            phi= np.random.uniform(0, 2*np.pi)
            tau= np.random.uniform(0, 2*np.pi)
            dot= Dot(color= BLUE)
            dot.move_to(funca(phi,tau,1))
            Dots_inner.add(dot)
        self.add(Dots_inner)

        sphere2= sphere.copy()
        self.add(sphere2.scale(2))
        Dots_outer= VGroup()
        for i in range(0,10): #inner shell
            r = 1
            phi= np.random.uniform(0, 2*np.pi)
            tau= np.random.uniform(0, 2*np.pi)
            dot= Dot(color= RED)
            dot.move_to(funca(phi,tau,2))
            Dots_outer.add(dot)
        self.add(Dots_outer)
        self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "DrawScene"
    os.system(command_A + command_B)

