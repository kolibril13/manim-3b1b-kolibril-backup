from manimlib.imports import *

class TinyUpdater(Scene): #Two Options to update a scene one more nested, one more explicit

    def construct(self):
        run_setting = {"run_time": 4, "rate_func": linear}
        tick_start=0
        tick_end=100
        val_tracker= ValueTracker(tick_start)
        dot_disp= Dot()
        self.add(dot_disp)
        val_tracker= ValueTracker(tick_start)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                mob.shift(DOWN * 0.001 * val_trackerX.get_value())
                return mob
            return UpdateFromFunc(dots, small_change2)
        self.play(Tiny_Updater(dot_disp,val_tracker),val_tracker.set_value,tick_end,**run_setting)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"TinyUpdater"
    os.system(command_A + command_B)