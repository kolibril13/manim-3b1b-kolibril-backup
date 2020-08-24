from manim import *

class BalmerX(Scene):

    def construct(self):
        dotphoton= Dot().scale(4).set_color("#2800ff")
        arc= Arc(-TAU/2, 3*TAU/2, radius=dotphoton.get_width()/2 , arc_center= dotphoton.get_center())
        self.add(dotphoton)
        dotphoton.set_stroke(WHITE)
        self.play(Write(arc))
        self.wait()

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -m --video_dir ~/Downloads/  "
    command_B = module_name +" " +"BalmerX"
    os.system(command_A + command_B)