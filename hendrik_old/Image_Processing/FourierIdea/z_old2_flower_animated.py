from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FLOWER import FLOWER

class MAIN(Scene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360    }

    def get_flower(self, number_flower):
        return FLOWER(number_flower.get_value())

    def construct(self):
        flow_tracker = ValueTracker(0) # is a number
        print(flow_tracker.get_value())
        flow = self.get_flower(flow_tracker)
        print(flow)
        self.add(flow)
        #breakpoint()
        self.play(
            UpdateFromFunc(
                flow, lambda mob: mob.become(
                    self.get_flower(flow_tracker))
            ),
            flow_tracker.set_value, self.flower_value_end  ,
            run_time=4 , rate_func=linear
        )


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " +"MAIN"
    os.system(command_A + command_B)