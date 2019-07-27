from manimlib.imports import *

class aaaa(Scene):
    def construct(self):
        dot = Dot()
        interpolate_color(GREEN, RED,BLUE, 2)
        self.add(dot)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"aaaa"
    os.system(command_A + command_B)