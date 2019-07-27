from manimlib.imports import *

class lllll(Scene):
    def get_dot(self,num):
        print(num)
        return Dot().shift(LEFT*num)
    def construct(self):
        dot = Dot()
        self.add(dot)
        val_track=ValueTracker(0)
        do= self.get_dot(val_track.get_value())
        # do.add_updater(
        #     lambda x: x.become(self.get_dot(val_track.get_value()))
        # )



        self.play(val_track.set_value,1000)
        
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lllll"
    os.system(command_A + command_B)