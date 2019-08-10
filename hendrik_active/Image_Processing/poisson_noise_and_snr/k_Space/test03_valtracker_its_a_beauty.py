from manimlib.imports import *

class PlanetScene(Scene):
    def construct(self):
        proportion_position_planet=ValueTracker(0)
        orbit=Circle(color=GREEN).scale(2.5)
        planet=Dot()
        planet.move_to(orbit.point_from_proportion(0))
        def update_planet(mob):
            mob.move_to(orbit.point_from_proportion(proportion_position_planet.get_value()%1))
            return mob

        planet.add_updater(update_planet)
        self.add(orbit,planet)
        for i in range(4):
            self.play(proportion_position_planet.increment_value,0.5,rate_func=linear)
            self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PlanetScene"
    os.system(command_A + command_B)