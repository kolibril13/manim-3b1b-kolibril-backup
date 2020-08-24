from manim import *

class BalmerX(Scene):
    def construct(self):
        dot= Dot()
        self.add(dot)
        x = np.linspace(0,2,100)
        def f(x):
            return np.sin(x)
        y = f(x)
        curve = VMobject()
        curve_teo = VMobject()
        self.add(curve_teo)
        curve_teo.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        self.wait()
        y = f(x+10)
        curve_teo.set_points_smoothly([[xi,yi,0]
                               for xi, yi in zip(x,y) ] )
        self.wait()
    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l  --video_dir ~/Downloads/  "
    command_B = module_name +" " +"BalmerX"
    os.system(command_A + command_B)