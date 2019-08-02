from manimlib.imports import *

class PlanetScene(Scene):
    def construct(self):
        self.t_offset=0
        orbit=Circle(color=GREEN).scale(2.5)
        planet=Dot()
        planet.move_to(orbit.point_from_proportion(0))
        self.add(orbit,planet)

        def Tiny_Updater(dots, val_trackerX):
            def small_change2(mob):
                mob.move_to(orbit.point_from_proportion(val_trackerX.get_value()))
                return mob
            return UpdateFromFunc(dots, small_change2)

        tick_start = 0; tick_end = 0.5
        val_tracker = ValueTracker(tick_start)
        self.play(Tiny_Updater(planet, val_tracker), val_tracker.set_value, tick_end, rate_func=linear)
        self.wait(2)

        tick_start = 0.5; tick_end = 1
        val_tracker = ValueTracker(tick_start)
        self.play(Tiny_Updater(planet, val_tracker), val_tracker.set_value, tick_end, rate_func=linear)
        self.wait(2)





if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l  -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"PlanetScene"
    os.system(command_A + command_B)