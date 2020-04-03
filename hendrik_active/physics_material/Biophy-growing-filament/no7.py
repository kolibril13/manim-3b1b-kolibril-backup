from manimlib.imports import *

class No7(Scene):
    def construct(self):
        red_dot = Dot(radius= 0.3, color= RED)
        white_dot = Dot(point=LEFT)
        self.add(red_dot)
        white_dot.move_to(red_dot.get_center()+RIGHT)
        def update_red_dot(mob,dt):
            #mob.rotate(angle= -0.01,about_point= ORIGIN)
            mob.shift(RIGHT*dt*1) #### CHANGE A
        def update_white_dot(mob,dt):
            if mob.time > 1:
                mob.time=0
                mob.move_to(red_dot.get_center()+RIGHT)
                mob.rotate(np.random.uniform(-PI,PI) ,about_point= red_dot.get_center())
            mob.shift(RIGHT*dt*1) #### CHANGE B
            point= mob.get_center() + (red_dot.get_center()- mob.get_center())*mob.time
            mob.move_to(point)
            mob.time += 0.1
        white_dot.time=0
        red_dot.add_updater(update_red_dot)
        white_dot.add_updater(update_white_dot)
        self.add(red_dot)
        self.add(white_dot)
        self.wait(5)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -m  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No7"
    os.system(command_A + command_B)
