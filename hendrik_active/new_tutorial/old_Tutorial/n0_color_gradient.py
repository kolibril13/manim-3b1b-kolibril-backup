from manimlib.imports import *





class SIN(ParametricFunction):
    CONFIG = {
        "start_color":GREEN,
        "end_color":RED
    }

    def __init__(self,a, **kwargs):
        digest_config(self, kwargs)
        self.a= a
        ParametricFunction.__init__(
            self, self.param_knosp,**kwargs
        )

    def param_knosp(self,u):
        x = u
        y = np.sin(u+self.a)
        z = 0
        return np.array([x, y, z])

class lalaaa(Scene):
    def construct(self):
            # dot= SIN(0)
            # self.add(dot)
            # self.wait(1)
            # dot.become(SIN(1))
            col = [GREEN, BLUE]
            colors = color_gradient(col, 256)
            print(colors)


    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lalaaa"
    os.system(command_A + command_B)