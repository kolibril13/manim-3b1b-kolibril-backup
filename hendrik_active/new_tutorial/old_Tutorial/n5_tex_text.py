from manimlib.imports import *

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        Transform.CONFIG.update({
            "replace_mobject_with_target_in_scene": True
        })
        t_1=TexMobject(r"\frac{\partial \rho}{\partial t}+ \frac{\partial(\rho u_{i})}{\partial x_{i}} = 0")
        self.add(t_1)
        self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p -s   --leave_progress_bars -a " + module_name
    os.system(command)
