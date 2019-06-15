from manimlib.imports import *

class Parametric_Function(Scene):
    CONFIG ={
        "color": BLUE,
        "run_time" :6
    }
    def construct(self):
        print("Start")
        dot = Dot()
        dot2 = Dot()

        moving_dot= Dot(color=RED)
        self.add(dot)
        for order in range(1,2):
            self.para_func= lambda t: np.array((np.sin(order * t), np.cos((order) * t), 0))
            func=ParametricFunction(self.para_func, t_max=TAU)
            func.scale(1+0.2*order)
            func.shift(LEFT)
            self.play(Transform(dot,func))
            self.para_func2 = lambda t: np.array((np.sin(5*order * t), np.sin((4*order) * t), 0))
            func2 = ParametricFunction(self.para_func2, t_max=TAU)
            func2.scale(1 + 0.2 * order)
            func2.shift(RIGHT)
            self.play(Transform(dot2, func2))
            self.play(MoveAlongPath(moving_dot,dot), run_time=self.run_time)
            self.play(MoveAlongPath(moving_dot,dot2), run_time=self.run_time)



        self.wait(1)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p   -a --leave_progress_bars " + module_name
    os.system(command)
