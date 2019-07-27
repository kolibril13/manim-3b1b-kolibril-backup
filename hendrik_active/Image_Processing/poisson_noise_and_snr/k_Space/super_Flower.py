from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FLOWER import FLOWER

class MAIN(Scene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360
    }
    print("hello")
    def get_flower(self, number_flower):
        return FLOWER(number_flower.get_value())


    def construct(self):
        self.pixel_len = 18
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [FLOWER((i / PIXELS) * 360) for i in range(0, PIXELS)]
        j = 0
        self.term = VGroup()
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.scale(0.4)
            square_to_move.move_to((RIGHT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.term.set_y(0)
        self.term.set_x(0)
        self.term.scale(8 / self.pixel_len)
        self.add(self.term)
        self.wait()

        # flow_tracker = ValueTracker(self.flower_value_start)
        # flow = self.get_flower(flow_tracker)
        # print(flow)
        # self.add(flow)

        # self.play(UpdateFromFunc(flow, lambda mob: mob.become(self.get_flower(flow_tracker))),
        # flow_tracker.set_value, self.flower_value_end,run_time=4 , rate_func=linear )


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " +"MAIN"
    os.system(command_A + command_B)