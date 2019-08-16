from manimlib.imports import *

class llaa(Scene):
    def construct(self):
        dot = Dot()
        dot2= Dot().shift(LEFT)
        dot3 = VMobject().interpolate(dot, dot2, alpha=0.4)
        self.add(dot,dot2,dot3)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l  -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"llaa"
    os.system(command_A + command_B)