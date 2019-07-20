from manimlib.imports import *

class Example(Scene):
    def construct(self):
        scale_fac=10
        dot = Dot()
        dot2=Dot().move_to(LEFT)
        line = Line(dot.get_center(),dot2.get_center())
        line.set_stroke(width=2)
        a=VGroup(dot,dot2,line)
        b=a.copy()
        b.scale(scale_factor=scale_fac)
        b.set_stroke(width=2*scale_fac)
        b.shift(DOWN)
        self.add(a,b)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s    -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lalll"
    os.system(command_A + command_B)