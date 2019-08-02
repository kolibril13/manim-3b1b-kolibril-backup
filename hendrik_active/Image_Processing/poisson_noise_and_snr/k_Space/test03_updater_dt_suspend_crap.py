from manimlib.imports import *

class PlanetScene(Scene):
    def construct(self):
        self.t_offset=0
        orbit=Circle(color=GREEN).scale(2.5)
        planet=Dot()
        planet.move_to(orbit.point_from_proportion(0))
        def update_planet(mob,dt):
            print(dt)
            rate=dt*0.5
            mob.move_to(orbit.point_from_proportion(((self.t_offset + rate))%1))
            self.t_offset += rate
            print(self.t_offset)
        planet.add_updater(update_planet)
        self.add(orbit,planet)  #first half
        self.wait(1)
        planet.suspend_updating() #waiting
        self.wait()
        planet.resume_updating() #second half
        self.wait(1)
        planet.suspend_updating()
        self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PlanetScene"
    os.system(command_A + command_B)