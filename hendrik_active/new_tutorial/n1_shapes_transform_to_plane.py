
from manimlib.imports import *

class Text(Scene):
    CONFIG = {
        "y_min": 0,
        "y_max": 10    }
    def construct(self):

        sq= Square()
        self.add(sq)
        self.wait(0.1)
        sq2= sq.copy()
        sq2.rotate(-20,[0,1,0.05])
        self.play(Transform(sq,sq2))


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p     -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Text"
    os.system(command_A + command_B)