from manimlib.imports import *

DEFAULT_STROKE_WIDTH=90

class StrokeW(Scene):
    def construct(self):
        DEFAULT_STROKE_WIDTH = 400
        l= Line(DL*100, UR, stroke_width= 100)
        l2= Line(DL*100+UL*100, UR+UL).set_color(GREEN)
        self.add(l,l2)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"StrokeW"
    os.system(command_A + command_B)