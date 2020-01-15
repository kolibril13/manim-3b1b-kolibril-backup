import matplotlib as mpl
from manimlib.imports import *
from PIL import Image

class Shapes(Scene):
    def construct(self):
        s1 = Square(fill_opacity=0.3).shift(LEFT)
        s2 = Square(fill_opacity=0.3, color=RED)
        self.add(s2)
        self.add(s1)
        print(self.mobjects)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -s   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Shapes"
    os.system(command_A + command_B)