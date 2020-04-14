from manimlib.imports import *

class Planexx(VMobject):
    CONFIG = {
        "Pixel":2
    }
    def __init__(self, size , **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
    def init_colors(self):
        self.bars = VGroup()
        bar = Dot(radius= self.Pixel)
        self.bars.add(bar)
        self.add(self.bars)
        print("yes")

    def get_lower_left_point(self):
        return self.bars.get_center()

    def color_plane(self):
        self.bars.set_color(GREEN)

class lala(Scene):
    def construct(self):
        my_plane= Planexx(2)
        print(my_plane.color_plane())
        self.add(my_plane)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lala"
    os.system(command_A + command_B)