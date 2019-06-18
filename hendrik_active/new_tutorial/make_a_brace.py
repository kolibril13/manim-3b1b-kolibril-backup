from manimlib.imports import *

class Bracee(Scene):
    def construct(self):
        dot = Dot()
        dot2= Dot([2,1,0])
        line = Line(dot,dot2)
        b=Brace(VGroup(dot,dot2),UP)
        eq_text = b.get_tex("x-x_1")

        self.add(dot)
        self.add((dot2), line,b, eq_text)
        self.wait(2)


    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -sl -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Bracee"
    os.system(command_A + command_B)