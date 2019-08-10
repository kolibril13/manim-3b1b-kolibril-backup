from manimlib.imports import *

class K_Space(VMobject):
    def __init__(self,**kwargs):
        VMobject.__init__(self, **kwargs)
        self.center= Dot(fill_color=GREEN)
        self.add(self.center)

    def set_new_position(self,orbit,value):
        self.planet = Dot()
        self.planet.move_to(orbit.point_from_proportion(value))
        self.add(self.planet)

    def set_new_position_updater(self,orbit,value):
        self.planet.become(self.planet.move_to(orbit.point_from_proportion(value)))


class PlanetScene(Scene):
    def construct(self):
        proportion_position_planet=ValueTracker(0)
        orbit=Circle().scale(2.5)
        system= K_Space()
        system.set_new_position(orbit,0)
        def update_planet(mob):
            mob.set_new_position_updater(orbit, proportion_position_planet.get_value())
            return mob.become(mob)
        self.add(system)
        self.wait()
        for i in range(4):
            self.play(
                proportion_position_planet.increment_value,0.25,  #<- "Master" update first
                UpdateFromFunc(system,update_planet),
                rate_func=linear)
            self.wait(0.5)





if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PlanetScene"
    os.system(command_A + command_B)