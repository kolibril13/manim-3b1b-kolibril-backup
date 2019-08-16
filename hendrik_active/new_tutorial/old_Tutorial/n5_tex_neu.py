from manimlib.imports import *
class AddingText(Scene):
    def construct(self):
        t_1=TexMobject(r"\frac{\partial \rho}{\partial t}+ \frac{\partial(\rho u_{i})}{\partial x_{i}} = 0")
        self.add(t_1)
        self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    print(module_name)
    command = "python3.7 -m manim  -p -s   --leave_progress_bars -a " + module_name
    print(command)
    os.system(command)
