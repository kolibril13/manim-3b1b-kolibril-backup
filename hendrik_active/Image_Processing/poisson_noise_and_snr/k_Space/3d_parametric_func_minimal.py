from manimlib.imports import *

class Example(ThreeDScene):

    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        sphere=Sphere()
        axes = ThreeDAxes()
        self.add(sphere,axes)
        self.move_camera(frame_center=LEFT*3)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -l -s -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Example"
    os.system(command_A + command_B)