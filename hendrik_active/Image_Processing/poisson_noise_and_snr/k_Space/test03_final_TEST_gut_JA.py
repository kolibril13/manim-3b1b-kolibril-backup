from manimlib.imports import *

class K_Space(VMobject):
    def __init__(self,**kwargs):
        VMobject.__init__(self, **kwargs)
        self.term = VGroup()
        self.flows = VGroup()
        self.term.add(Dot()) #center
        self.add(self.term)
        self.set_new_position(kwargs[0],kwargs[1])
        self.add()

    def set_new_position(self,orbit,value):
        self.remove(self.flows)
        self.flows= VGroup()
        planet = Dot()
        planet.move_to(orbit.point_from_proportion(value))


        # m1, m2 = mirrors
        # center = self.get_center()
        # theta = self.get_theta()
        # m1.move_to(center, DL)
        # m2.become(m1)
        # m2.rotate(theta, about_point=center)

class PlanetScene(Scene):
    def construct(self):
        proportion_position_planet=ValueTracker(0)
        orbit=Circle(color=GREEN).scale(2.5)
        system= K_Space()
        system.set_new_position(orbit,0)
        def update_planet(mob):
            mob.set_new_position(orbit, proportion_position_planet.get_value())
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