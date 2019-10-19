from manimlib.imports import *

class ParamFunc(Scene):

    def func(self,t):
        return np.array((np.sin(2*t), np.sin(3*t),0))

    def construct(self):
        func=ParametricFunction(self.func, t_max=TAU, fill_opacity=0)
        print(len(func.points))
        # dot = Dot()
        # self.add(dot)
        print(dir(func))
        #breakpoint()
        func.set_color_by_gradient(BLUE, RED)

        self.add(func.scale(3))
        # self.wait(3)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "manim  -p -s  " + module_name + " ParamFunc "
    os.system(command)

