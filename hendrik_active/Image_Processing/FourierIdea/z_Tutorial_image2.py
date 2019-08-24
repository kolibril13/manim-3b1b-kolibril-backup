from manimlib.imports import *
from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis


from manimlib.imports import *
#display options
from manimlib.imports import *

class ImageScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.begin_ambient_camera_rotation()
        Disp_array= VMobject()
        for x in range(-3, 3):
            for y in range(-3, 3):
                for z in range(-3, 3):
                    dot = Dot(point=(x, y, z))
                    Disp_array.add(dot)
        [Disp_array.submobjects[i].set_color(RED) for i in range(0,100)]
        self.add(Disp_array)
        self.wait(2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -m --video_dir ~/Downloads/  "
    command_B = module_name +" " +"ImageScene"
    os.system(command_A + command_B)