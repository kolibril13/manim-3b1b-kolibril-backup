from manimlib.imports import *

class PlanetScene(Scene):
    def construct(self):
        #Se objects
        self.t_offset=0
        orbit=Ellipse(color=GREEN).scale(2.5)
        planet=Dot()
        text=TextMobject("Update function")

        planet.move_to(orbit.point_from_proportion(0))

        def update_planet(mob,dt):
            rate=dt*0.1
            mob.move_to(orbit.point_from_proportion(((self.t_offset + rate))%1))
            self.t_offset += rate

        planet.add_updater(update_planet)
        self.add(orbit,planet)
        self.wait(3)
        self.play(Write(text))
        self.wait(3)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PlanetScene"
    os.system(command_A + command_B)