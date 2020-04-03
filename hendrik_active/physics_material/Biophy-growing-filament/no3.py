from manimlib.imports import *

class No3(Scene):
    def construct(self):
        red_dot= Dot(point=LEFT_SIDE+RIGHT,radius= 0.1, color= RED)
        white_dot = Dot(point=UP)
        self.add(red_dot)
        def update_red_dot(mob,dt):
            mob.shift(RIGHT*dt*1)

        def update_white_dot(self):
            self.match_x(red_dot)

        red_dot.add_updater(update_red_dot)
        white_dot.add_updater(update_white_dot)

        self.play(white_dot.copy().shift,DOWN ,rate_func= linear,run_time=0.2)
        for i in range(0,10):
            self.play(FadeOut(self.mobjects[1]),  white_dot.copy().shift,DOWN, rate_func= linear, run_time=0.2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No3"
    os.system(command_A + command_B)
