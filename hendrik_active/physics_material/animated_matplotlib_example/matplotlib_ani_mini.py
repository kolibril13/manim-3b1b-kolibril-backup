from manimlib.imports import *
import numpy as np
import matplotlib.pyplot as plt
def make_plot():
    return 1
class Matplotlibtest(Scene):
    def construct(self):
        array_things= make_plot()
        dot = Dot()
        self.add(dot)
        plotbackground= ImageMobject("lalala.png")
        plotbackground.background_rectangle = SurroundingRectangle(plotbackground, buff=0)
        self.add( plotbackground,plotbackground.background_rectangle)
        x = np.linspace(-PI,PI,100)
        y = 2*np.sin(2*x)
        sin_curve = VMobject()
        sin_curve.set_points_smoothly([[xi,yi,0]
                                       for xi, yi in zip(x,y) ] )
        sin_curve.set_color(GREEN)
        print(array_things)
        sin_curve.stretch_to_fit_width(plotbackground.get_width())
        self.add(sin_curve)
        box = np.array([[0.06076388888888889, 0.1111111111111111], [0.8999999999999999, 0.8799999999999999]])
        self.add(Dot().move_to(plotbackground.get_corner(UL)).set_color(BLACK))
        self.add(Dot().move_to(plotbackground.get_corner(UL)).set_color(BLACK)
                 .shift(RIGHT*plotbackground.get_width()*box[0,0]))
        self.add(Dot().move_to(plotbackground.get_corner(UL)).set_color(BLACK)
                 .shift(RIGHT*plotbackground.get_width()*box[1,0]))
        self.add(Dot().move_to(plotbackground.get_corner(UL)).set_color(BLACK)
                 .shift(RIGHT*plotbackground.get_width()*box[1,1]))
        self.add(Dot().move_to(plotbackground.get_corner(UL)).set_color(BLACK)
                 .shift(RIGHT*plotbackground.get_width()*box[0,1]))
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Matplotlibtest"
    os.system(command_A + command_B)