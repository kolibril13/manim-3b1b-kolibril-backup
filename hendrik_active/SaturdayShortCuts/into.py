from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        dot = SVGMobject("/home/jan-hendrik/python/projects/manim/hendrik_active/SaturdayShortCuts/pylogo.svg")
        self.add(dot)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Intro"
    os.system(command_A + command_B)