from manimlib.imports import *

class Shapes(Scene):
    CONFIG ={
        "color": BLUE,
    }
    def construct(self):
        print("Start")
        dot = Dot()
        func=ParametricFunction(self.f23, t_max=TAU)
        self.add(dot)
        self.add(func)
        self.wait(3)

    def f23(self,t):
        return np.array((np.sin(2*t), np.sin(3*t),0))


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p -s -o earth_sofi  --leave_progress_bars " + module_name + " Shapes "
    os.system(command)

