from manimlib.imports import *
from hendrik_active.Image_Processing.FourierIdea.KSpace import *
from hendrik_active.Image_Processing.FourierIdea.Realspace import *
from hendrik_active.Image_Processing.FourierIdea.FourierMathJuggling import *


class Image_coordinate_system(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        UP_arrow = SVGMobject("arrow.svg", fill_color=ORANGE).shift(UP * 4.5)
        UP_arrow.set_shade_in_3d(True)
        k_text = TextMobject("K-Space", fill_color=ORANGE).shift(DOWN * 4).scale(2)
        # k_text.set_shade_in_3d(True)
        self.add(k_text)
        self.add(UP_arrow)

class Comp_axis(VMobject):
    def __init__(self,height):
        VMobject.__init__(self)
        ax = Rectangle(height=height, width=1,fill_color=GREEN)
        axt = TextMobject(f"{height}").next_to(ax, UP)
        axis = VGroup(ax, axt)

        axis.rotate(-PI / 2, axis=LEFT)
        axis.next_to(ORIGIN, OUT,buff=0)
        self.add(axis)
