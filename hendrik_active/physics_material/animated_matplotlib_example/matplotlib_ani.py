nfrom manimlib.imports import *
import numpy as np
import matplotlib.pyplot as plt
def make_plot():
    fig, ax = plt.subplots(1, figsize=(16,3))
    x=np.linspace(0,2.0,1001)
    tick_pos= [ 0.25*(i+1) for i in range(0,8)]
    [plt.axhline(i, color= "Gray", alpha=0.4 ) for i in range(-2,3)]
    [plt.axvline(i, color= "Gray", alpha=0.4 ) for i in tick_pos]
    plt.axhline(0, color= "Black")
    plt.ylim(-3,3)
    plt.xlim(0, 2 +  0.15)
    print("hhiii")
    ################
    plt.plot(x, 3*np.sin(-2*np.pi*x/2), lw=3)
    plt.yticks(fontsize=20, alpha=0.6);
    plt.xticks(tick_pos , fontsize=20, alpha=0.6 );
    plt.annotate(r'x in [m]',
                 xy=(1, 0), xycoords='axes fraction',
                 xytext=(-20, 20), textcoords='offset pixels',
                 horizontalalignment='right',
                 verticalalignment='bottom',
                 fontsize=20);
    invTransFig = fig.transFigure.inverted().transform_bbox
    pos = ax.get_position(original=True)
    print(pos)
    tightbbox = ax.get_tightbbox(renderer=fig.canvas.get_renderer())
    bbox = invTransFig(tightbbox)

    plt.savefig("plot01",bbox_inches='tight', pad_inches=0)
    return np.array(bbox)
class Matplotlibtest(Scene):
    def construct(self):
        array_things= make_plot()
        dot = Dot()
        self.add(dot)
        plotbackground= ImageMobject("plot01.png")
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
        self.add(Dot().move_to(plotbackground.get_corner(DL)).set_color(BLACK))
        self.add(Dot().move_to(plotbackground.get_corner(DL)).set_color(BLACK).shift(RIGHT*plotbackground.get_width()))
        self.add(Dot().move_to(plotbackground.get_corner(DL)).set_color(BLACK).shift(RIGHT*plotbackground.get_width()*0.09329861))
        self.add(Dot().move_to(plotbackground.get_corner(DL)).set_color(BLACK).shift(RIGHT*plotbackground.get_width()* 0.9))
        self.add(Dot().move_to(plotbackground.get_corner(DL)).set_color(BLACK).shift(RIGHT*plotbackground.get_width()*0.91666667))

        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Matplotlibtest"
    os.system(command_A + command_B)