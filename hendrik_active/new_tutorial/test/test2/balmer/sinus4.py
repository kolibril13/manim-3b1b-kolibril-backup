from manimlib.imports import *

class BalmerX(Scene):

    def construct(self):
        self.play(Write(TextMobject("Hello world"), run_time=1))
        self.play(Dot().shift, DOWN, run_time=3)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -m --video_dir ~/Downloads/  "
    command_B = module_name +" " +"BalmerX"
    os.system(command_A + command_B)