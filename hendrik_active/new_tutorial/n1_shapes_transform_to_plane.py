
from manimlib.imports import *

class RotationAroundAxes(Scene):
    def construct(self):
        sq= Square()
        self.add(sq)
        self.wait(0.1)
        sq2= sq.copy()
        sq2.rotate(-20,  OUT+RIGHT) #rotate around the axis which lays between OUT(z) and RIGHT(x)
        self.play(Transform(sq,sq2))


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -i -p   -t --video_dir ~/Downloads/  "
    command_B = module_name +" " +"RotationAroundAxes"
    os.system(command_A + command_B)