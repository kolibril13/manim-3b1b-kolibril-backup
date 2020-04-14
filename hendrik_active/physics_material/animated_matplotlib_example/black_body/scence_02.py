from manimlib.imports import *

import scipy.special

class BlackBody0(GraphScene):
    def construct(self):
        img1 = ImageMobject("sun_no0.png").scale(4)
        self.add(img1)
        img2 = ImageMobject("sun_no1.png").scale(4)
        self.wait(2)
        self.play(FadeIn(img2))
        self.wait(4)







if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name + " " + "BlackBody0"
    os.system(command_A + command_B)
