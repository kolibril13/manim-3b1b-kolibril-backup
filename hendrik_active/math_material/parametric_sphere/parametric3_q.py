from manimlib.imports import *

class CylindricalCoordinates(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES)
        self.begin_ambient_camera_rotation(0.4)
        self.camera.frame_center.shift(3.5 * LEFT)
        axes = ThreeDAxes()
        def func(t):
            return np.array((np.cos(2* t), np.sin(2* t), 0.5+np.cos(t)))
        func = ParametricFunction(func, t_max=TAU, fill_opacity=0)
        func.scale(2)
        self.add(func)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "CylindricalCoordinates"
    os.system(command_A + command_B)

