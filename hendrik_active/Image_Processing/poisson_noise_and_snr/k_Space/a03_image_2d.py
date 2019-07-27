from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.super_Flower import FLOWER
class K_Space(VMobject):
    CONFIG = {
        "Pixel":2,
        "pixel_len":23

    }
    def __init__(self, size , **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)


    def init_colors(self):
        self.term= VGroup()
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1) for i in range(0, PIXELS)]
        flower_all= [FLOWER(np.random.randint(1, 360)) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % np.sqrt(PIXELS) == 0:
                j += 1
            k = i - j * np.sqrt(PIXELS)
            square_to_move.move_to((LEFT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.add(self.term)
        self.term2 = VGroup()
        j = 0
        for i, square_to_move in enumerate(flower_all):
            if i % np.sqrt(PIXELS) == 0:
                j += 1
            k = i - j * np.sqrt(PIXELS)
            square_to_move.move_to((LEFT * k + j * DOWN)).scale(0.2)
        self.term2.add(*flower_all)
        self.add(self.term2)

    def fill_k_space(self):
        img_array= np.uint8(np.random.randint(1, 255, (self.pixel_len, self.pixel_len)))
        t_objects = [t for t in self.term.submobjects]
        # create color gradient
        colors = [BLACK, WHITE]
        colors = color_gradient(colors, 256)
        img_array = img_array.flatten()
        # create dots array
        dots = []
        vert_line = []
        for i, el in enumerate(t_objects):
            wanted_color = colors[img_array[i]]
            el.set_color(wanted_color)
    def get_lower_left_point(self):
        return self.term.get_center()

    def color_plane(self):
        self.term.set_color(GREEN)

class lala(Scene):
    def construct(self):
        my_plane= K_Space(2,pixel_len=10).scale(0.3)
        my_plane.move_to(ORIGIN)
        my_plane.fill_k_space()
        self.add(my_plane)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -s   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lala"
    os.system(command_A + command_B)