#display options
from manimlib.imports import *
global k_plane_size
k_plane_size=0.7
class Realspace(VMobject):
    CONFIG = {
        "mushroom_heigt": 1.1,
        "magic_offset_z": k_plane_size
    }

    def __init__(self, pixel_len,**kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
        self.term = VGroup()
        self.pixel_len=pixel_len
        PIXELS = pixel_len * pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1 , stroke_width=0) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.move_to((LEFT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.add(self.term)

    def fill_real_space(self, img_real):
        t_objects = [t for t in self.term.submobjects]
        img_real = img_real.flatten()
        #interpolate the colors from array
        for i, el in enumerate(t_objects):
            if img_real[i] < 0:
                el.set_color(BLACK)
            else:
                el.set_color(interpolate_color(BLACK, WHITE, img_real[i] / 255)) #change!!
