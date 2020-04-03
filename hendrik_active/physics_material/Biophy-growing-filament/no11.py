from manimlib.imports import *

class No11(Scene):
    def construct(self):
        N=2000
        concentration = 0*N
        num_wd_left_plus= 10
        blue_dot = Dot(radius= 0.3, color= BLUE)
        white_dots = [Dot(point=LEFT) for i in range(0,num_wd_left_plus)]
        self.add(blue_dot)
        [dot.rotate(np.random.uniform(-PI,PI) ,about_point= blue_dot.get_center()) for dot in white_dots]
        for i, dot in enumerate(white_dots):
            dot.time= 0.1*i
        self.add(*white_dots)
        def update_red_dot(mob,dt):
            mob.shift(RIGHT*dt*1) #### CHANGE A
        def update_white_dot(mob,dt):
            if mob.time > 1:
                mob.time=0
                mob.move_to(blue_dot.get_center()+RIGHT)
                mob.rotate(np.random.uniform(-PI,PI) ,about_point= blue_dot.get_center())
            mob.shift(RIGHT*dt*1) #### CHANGE B

            point= mob.get_center() + (blue_dot.get_center()- mob.get_center())*mob.time
            mob.move_to(point)
            mob.time += 1/60

        blue_dot.add_updater(update_red_dot)
        [white_dot.add_updater(update_white_dot) for white_dot in white_dots]
        self.wait(5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No11"
    os.system(command_A + command_B)
