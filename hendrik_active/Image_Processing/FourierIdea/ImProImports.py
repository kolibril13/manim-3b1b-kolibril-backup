from manimlib.imports import *
from hendrik_active.Image_Processing.FourierIdea.KSpace import *
from hendrik_active.Image_Processing.FourierIdea.Realspace import *
from hendrik_active.Image_Processing.FourierIdea.FourierMathJuggling import *
from hendrik_active.Image_Processing.FourierIdea.FLOWER import FLOWER
linear_step_func=StepFunctions.linear_step_func



class Image_coordinate_system(VMobject):
    def __init__(self,zoomed=False, downsampled=False):
        VMobject.__init__(self)
        UP_arrow = SVGMobject("arrow.svg", fill_color=ORANGE).shift(UP * 4.5)
        UP_arrow.set_shade_in_3d(True)
        # k_text.set_shade_in_3d(True)
        self.add(UP_arrow)
        if zoomed == True:
            k_text = TexMobject(r"\text{K-Space}^+", fill_color=ORANGE).shift(DOWN * 4).scale(2)
        elif downsampled == True:
            k_text = TexMobject(r"\text{K-Space}^\circ", fill_color=ORANGE).shift(DOWN * 4).scale(2)
        else:
            k_text = TextMobject("K-Space", fill_color=ORANGE).shift(DOWN * 4).scale(2)

        self.add(k_text)

class Comp_axis(VMobject):
    def __init__(self,height):
        VMobject.__init__(self)
        ax = Rectangle(height=height, width=1,fill_color=GREEN)
        #axt = TextMobject(f"Amplitude").next_to(ax, UP)
        #axis = VGroup(ax, axt)
        axis= VGroup(ax)
        axis.rotate(-PI / 2, axis=LEFT)
        axis.next_to(ORIGIN, OUT,buff=0)
        self.add(axis)
