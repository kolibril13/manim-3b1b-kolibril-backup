from manimlib.imports import *

class No1(Scene):
    def construct(self):
        dot_anchor = Dot(radius= 0.6, color= RED)
        dot1 = Dot().shift(dot_anchor.get_center()+UP)
        self.add(dot_anchor)
        self.play(dot1.copy().shift, DOWN ,run_time=0.5)
        self.play(FadeOut(self.mobjects[1]),
                dot1.copy().shift, DOWN,run_time=0.5)
        self.play(FadeOut(self.mobjects[1]),
                  dot1.copy().shift, DOWN, run_time=0.5)
        self.play(FadeOut(self.mobjects[1]),
                  dot1.copy().shift, DOWN,run_time=0.5)
        self.play(FadeOut(self.mobjects[1]),
                  dot1.copy().shift, DOWN, run_time=0.5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -m  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No1"
    os.system(command_A + command_B)