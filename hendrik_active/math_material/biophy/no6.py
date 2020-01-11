from manimlib.imports import *

class No6(Scene):
    def construct(self):
        red_dot = Dot(radius= 0.3, color= RED)
        white_dot = Dot(point=LEFT)
        self.add(red_dot)
        def update_red_dot(mob,dt):
            mob.shift(RIGHT*dt*1)

        red_dot.add_updater(update_red_dot)
        self.add(red_dot)
        for i in range(0,20):
            wd= white_dot.copy()
            wd.move_to(red_dot.get_center()+RIGHT)
            wd.rotate(np.random.uniform(-PI/2,PI/2) ,about_point= red_dot.get_center())
            self.play(wd.move_to, red_dot.get_center(),run_time=0.2)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -m  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No6"
    os.system(command_A + command_B)
