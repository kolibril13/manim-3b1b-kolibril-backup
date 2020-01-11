from manimlib.imports import *

class No11(Scene):
    def construct(self):
        kP_on = 11.6
        kP_off = 1.4

        def dnP(concentration):
            return kP_on*concentration- kP_off

        N=2000
        concentration = 0
        num_particles = concentration*N
        num_wd_left_plus= 10
        sq= Rectangle(width=0.45*FRAME_WIDTH*2,height= 0.15*FRAME_HEIGHT*2)
        blue_dot = Dot(radius= 0.3, color= BLUE)
        self.add(sq)
        tubel= Line(sq.get_corner(LEFT), blue_dot.get_center(), stroke_width= 20)
        self.add(tubel)
        self.add(blue_dot)
        def update_line(mob):
            mob.become(Line(sq.get_corner(LEFT),blue_dot.get_center(), stroke_width= 20))
        def update_moving_dot(mob,dt):
            mob.shift(RIGHT*dt*dnP(concentration)) #### CHANGE A

        blue_dot.add_updater(update_moving_dot)
        tubel.add_updater(update_line)

        self.wait(5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No11"
    os.system(command_A + command_B)
