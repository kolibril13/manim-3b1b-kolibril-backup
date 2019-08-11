from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,FLOWER
from manimlib.imports import *
global s, e, ste
s=0
e=180
ste=8


class artwork(Scene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360
    }

    def get_flower(self, number_flower):
        return FLOWER(number_flower.get_value())


    def construct(self):
        self.pixel_len=18
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [FLOWER((i/PIXELS)*360) for i in range(0, PIXELS)]
        j = 0
        self.term= VGroup()
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.scale(0.4)
            square_to_move.move_to((RIGHT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.term.set_y(0)
        self.term.set_x(0)
        self.term.scale(8/self.pixel_len)
        self.add(self.term)
        self.wait()

        # dot= [FLOWER(i).shift(j*RIGHT*2+LEFT_SIDE*4).scale_about_point(0.2,ORIGIN) for j,i in enumerate(np.arange(s,e,ste)) ]
        # self.add(*dot)
        # dot2 = [FLOWER(i).shift(j * RIGHT * 2 + LEFT_SIDE * 4 + 6*DOWN).scale_about_point(0.2, ORIGIN) for j, i in
        #        enumerate(np.arange(s+180, e+180, ste))]
        # self.add(*dot2)
        # self.wait()

if __name__ == "__main__":
     module_name = os.path.basename(__file__)
     command_A = "manim  -s -p -c '#1C758A' --video_dir ~/Downloads/ " + module_name + " artwork  "
     os.system(command_A )