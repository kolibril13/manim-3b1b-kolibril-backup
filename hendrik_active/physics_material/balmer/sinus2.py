from manim import *

class BalmerX(Scene):

    def construct(self):
        dotphoton= Dot().scale(4).set_color("#2800ff")
        self.add(dotphoton)
        x = np.linspace(-PI,PI,100)
        y = 2*np.sin(2*x)
        sin_curve = VMobject()
        self.add(sin_curve)
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.scale(0.06)
        VGroup(sin_curve,dotphoton)
        self.wait()

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s --video_dir ~/Downloads/  "
    command_B = module_name +" " +"BalmerX"
    os.system(command_A + command_B)