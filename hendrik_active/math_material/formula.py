from manimlib.imports import *

class Lock(Scene):
    def construct(self):
        equation = TexMobject(r"\sin(", "3x","+","1","=","10")

        #t_5 = TexMobject(r"\sin(","t",")")
        self.add(equation.shift(DOWN))
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Lock"
    os.system(command_A + command_B)