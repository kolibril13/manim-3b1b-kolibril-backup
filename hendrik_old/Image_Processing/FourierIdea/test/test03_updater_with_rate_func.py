from manimlib.imports import *


class PlanetScene(Scene):
    def construct(self):
        self.t_offset=0
        self.circle_offset=0
        self.counter=0

        orbit=Circle(color=GREEN).scale(2.5)
        planet=Dot()
        planet.move_to(orbit.point_from_proportion(0))
        def rate_func(xi):  # takes ints!
            rate = 2
            xis = xi % rate
            offset = math.floor(xi / rate)
            if xis < 1:
                yi = (xis + offset) / rate
            if xis >= 1:
                yi = (1 + offset) / rate
            return yi
        def update_planet(mob,dt):
            self.circle_offset_old=self.circle_offset
            self.t_offset += dt
            velocity=0.5
            self.circle_offset =rate_func(self.t_offset*velocity)
            mob.move_to(orbit.point_from_proportion(self.circle_offset%1))
            if self.t_offset%1 == 0:
                print(f"\n position:{self.t_offset} and circle_offset:{self.circle_offset}")
        planet.add_updater(update_planet)
        self.add(orbit,planet)  #first half
        self.wait(12)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PlanetScene"
    os.system(command_A + command_B)