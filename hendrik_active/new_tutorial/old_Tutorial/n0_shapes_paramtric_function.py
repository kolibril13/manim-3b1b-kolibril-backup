from manimlib.imports import *

class ParamFunc(Scene):

    def func(self,t):
        return np.array((np.sin(2*t), np.sin(3*t),0))

    def construct(self):
        func=ParametricFunction(self.func, t_max=TAU, fill_opacity=0)
        dot = Dot()
        self.add(dot)
        self.add(func)
        self.wait(3)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "manim  -p -s -o earth_sofi  --leave_progress_bars " + module_name + " ParamFunc "
    os.system(command)

