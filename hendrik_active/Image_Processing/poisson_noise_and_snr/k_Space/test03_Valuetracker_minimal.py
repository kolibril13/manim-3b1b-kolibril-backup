from manimlib.imports import *

class lllll(Scene):
    def get_dot(self,num):
        print(num)
        return Dot().shift(LEFT*0.01 *num)
    def construct(self):
        dot_tracker= ValueTracker(0)
        dot_disp= self.get_dot(dot_tracker.get_value())
        
        def dot_updater(dot_disp):
            dot_disp.become(self.get_dot(dot_tracker.get_value()))

        dot_disp.add_updater(dot_updater)
        self.add(dot_disp)
        self.play(dot_tracker.set_value, 200, rate_func= linear)
        self.wait()
       
    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lllll"
    os.system(command_A + command_B)