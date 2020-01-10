from manimlib.imports import *

class CylindricalCoordinates(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=10 * DEGREES)
        axes = ThreeDAxes()
        surf = ParametricSurface(
            lambda u,v : np.array([
                u,
                v,
                3*u+v**2
            ]),
            resolution=(6, 6),
            v_min=-1,v_max=1,u_min=-3,u_max=2,
        )

        self.add(surf)
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "CylindricalCoordinates"
    os.system(command_A + command_B)

