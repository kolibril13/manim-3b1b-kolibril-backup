from manimlib.imports import *

class lllll(Scene):
    def get_dot(self,num):
        print(num)
        return Dot().shift(LEFT*0.01 *num)
    def construct(self):
        tick_start=0
        tick_end=100
        val_tracker= ValueTracker(tick_start)
        dot_disp= self.get_dot(val_tracker.get_value())

        dot_disp.add_updater(lambda x: x.become(self.get_dot(val_tracker.get_value())))
        self.add(dot_disp)
        self.play(val_tracker.set_value, tick_end, rate_func= linear)
        self.wait()
       
    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lllll"
    os.system(command_A + command_B)