from manimlib.imports import *

class Parametric_Function(Scene):
    CONFIG ={
        "color": BLUE,
        "run_time" :6
    }
    def construct(self):
        self.para_func= lambda t: np.array((np.sin(t),t, 0))
        func=ParametricFunction(self.para_func,t_min=0, t_max=TAU).shift(DOWN*3)
        func.set_style(stroke_width=9)

        line= Line(3*UP, 3*DOWN, color= BLACK)
        line.set_style(stroke_width=9)
        t=TexMobject("+  -").scale(3)
        t.next_to(line,DOWN,buff=0)
        self.add(line,func,t)
        def hsin(t):
            if np.sin(t) < 0:
                y= np.sin(t)
            else:
                y=0
            return y

        self.wait(3)
        self.para_func2 = lambda t: np.array((hsin(t), t, 0))
        func2 = ParametricFunction(self.para_func2, t_min=0, t_max=TAU).shift(DOWN * 3)
        func2.set_style(stroke_width=9)
        self.play(Transform(func,func2))
        self.wait(3)



        self.wait(1)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -t --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Parametric_Function"
    os.system(command_A + command_B)
