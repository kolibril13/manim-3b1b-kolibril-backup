from manimlib.imports import *

class Shapes(Scene):
    CONFIG ={
        "color": BLUE,
        "run_time" :6
    }
    def construct(self):
        print("Start")
        dot = Dot()
        moving_dot= Dot(color=RED)
        self.add(dot)
        for order in range(3,4):
            self.para_func= lambda t: np.array((np.sin(order * t), np.sin((order+1) * t), 0))
            func=ParametricFunction(self.para_func, t_max=TAU)
            func.scale(1+0.2*order)
            func.shift(LEFT)
            self.play(Transform(dot,func))
            self.play(MoveAlongPath(moving_dot,dot), rate_func=linear, run_time=self.run_time)


        self.wait(1)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p   --leave_progress_bars " + module_name + " Shapes "
    os.system(command)
