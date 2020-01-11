from manimlib.imports import *

class No14(Scene):
    def construct(self):
        km= 1
        def shift_elements_by_rate(element, dt):
            element.shift(RIGHT*dt*km)
        red_dot = Dot(radius= 0.3, color= RED)
        
        wdPoff = Dot(point=LEFT)
        wdPoff.move_to(red_dot.get_center()+DOWN)
        wdPoff.rotate(np.random.uniform( -np.radians(15), np.radians(15)  ) ,about_point= red_dot.get_center())
        wdPoff.set_opacity(0)
        wdPoff.subdot= Dot()
        wdPoff.time=0
        

        def update_red_dot(mob,dt):
            shift_elements_by_rate(mob, dt)
        def updat_wdPoff(mob,dt):
            if mob.time > 1:
                mob.time=0
                mob.move_to(red_dot.get_center()+DOWN)
                mob.rotate(np.random.uniform( -np.radians(15), np.radians(15)  ) ,about_point= red_dot.get_center())
            shift_elements_by_rate(mob, dt)
            point= red_dot.get_center() + (mob.get_center()- red_dot.get_center())*mob.time
            mob.subdot.move_to(point)
            mob.subdot.set_opacity(1-mob.time)
            mob.time += 0.01

        red_dot.add_updater(update_red_dot)
        wdPoff.add_updater(updat_wdPoff)
        self.add(red_dot)
        self.add(wdPoff)
        self.add(wdPoff.subdot)
        self.wait(5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No14"
    os.system(command_A + command_B)
