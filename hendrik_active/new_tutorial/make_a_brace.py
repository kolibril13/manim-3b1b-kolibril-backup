from manimlib.imports import *

class MakeBrace(Scene):
    def construct(self):
        dot = Dot([0,0,0])
        dot2= Dot([2,1,0])
        line = Line(dot,dot2)
        b=Brace(VGroup(dot,dot2),direction= line.copy().rotate(PI/2).get_unit_vector())
        eq_text = b.get_tex("x-x_1")
        self.add(dot,dot2)
        self.add(line,b, eq_text)
        self.wait()


    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -sl -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"MakeBrace"
    os.system(command_A + command_B)