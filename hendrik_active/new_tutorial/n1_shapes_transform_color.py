
from manimlib.imports import *

class Text(Scene):
    CONFIG = {
        "y_min": 0,
        "y_max": 10    }
    def construct(self):

        sq= Square()
        self.add(sq)
        self.play(sq.set_opacity, 1)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l    -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Text"
    os.system(command_A + command_B)