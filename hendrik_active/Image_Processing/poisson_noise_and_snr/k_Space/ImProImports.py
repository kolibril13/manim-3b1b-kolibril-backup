from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.KSpace import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FourierMathJuggling import FourierMathJuggling
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.Realspace import Realspace

class Image_coordinate_system(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        UP_arrow = SVGMobject("arrow.svg", fill_color=ORANGE).shift(UP * 4.5)
        UP_arrow.set_shade_in_3d(True)
        k_text = TextMobject("K-Space", fill_color=ORANGE).shift(DOWN * 4).scale(2)
        # k_text.set_shade_in_3d(True)
        self.add(k_text)
        self.add(UP_arrow)

