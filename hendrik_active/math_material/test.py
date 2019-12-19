from manimlib.imports import *

class change(Scene):
    def construct(self):
        dot = VGroup(Dot(radius=1), Dot(radius=1).shift(LEFT))
        print(dot.submobjects)
        self.add(dot)
        self.play(ApplyFunction(lambda m : m[0].set_color(RED) and m.shift(UP)  , dot ))
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"change"
    os.system(command_A + command_B)