from manimlib.imports import *

class lllll(Scene):
    def get_dot(self,num_tracker):
        print(num_tracker.get_value())
        return Dot().shift(RIGHT*0.01 *num_tracker.get_value())
    def construct(self):
        tick_start=0
        tick_end=100
        val_tracker= ValueTracker(tick_start)
        dot_disp= self.get_dot(val_tracker)
        self.add(dot_disp)
        self.play(
            UpdateFromFunc(dot_disp, lambda mob: mob.become(self.get_dot(val_tracker))),
            val_tracker.set_value,tick_end
        )
        self.wait()
       
    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lllll"
    os.system(command_A + command_B)