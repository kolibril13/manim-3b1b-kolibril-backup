from manimlib.imports import *

class RadiationX(Scene):
    def construct(self):
        x_exp=np.linspace(0,10000,1000)
        y_exp=np.random.uniform(0,100,(1000,1))
        x_exp= x_exp/10000
        y_exp= y_exp/100
        curve_teo = VMobject()
        curve_teo.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x_exp,y_exp) ] )
        self.play(Write(curve_teo))

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"RadiationX"
    os.system(command_A + command_B)