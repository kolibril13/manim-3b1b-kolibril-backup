from manimlib.imports import *

## END PARAMETER 0-360*
## Farben
##BLUE- GREEN
##GREEN-RED
##RED-Brown
##Brown-BLUE



class SIN(ParametricFunction):
    CONFIG = {
        "color1":BLUE,
        "color2":GREEN,
        "color3": RED,
        "color4": GREY_BROWN
    }
    def __init__(self,a_deg, **kwargs):
        self.offset = 1 / 4
        a_deg= a_deg*self.offset
        digest_config(self, kwargs)
        self.a_rad= a_deg/360*TAU
        col = [self.color1, self.color2,self.color3, self.color4]
        colors = color_gradient(col, 360+1)
        co_pick=colors[int(a_deg)]
        ParametricFunction.__init__(
            self, self.param_knosp, stroke_color= co_pick ,stroke_width=5 ,  **kwargs
        )

    def param_knosp(self,u):
        x = u
        y = np.sin(u+self.a_rad)
        z = 0
        return np.array([x, y, z])



class FlowerGrow(Animation):
    CONFIG = {
        "axis": OUT,
        "radians": TAU,
        "deg" : 360,
        "run_time": TAU,
        "rate_func": linear,
        "about_point": None,
        "about_edge": None,
    }

    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.become(SIN(alpha * self.deg))

class MAIN(Scene):
    def construct(self):
        dot= SIN(0)
        self.add(dot)
        self.play(FlowerGrow(dot), run_time=2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"MAIN"
    os.system(command_A + command_B)