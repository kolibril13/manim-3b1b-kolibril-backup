from manimlib.imports import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from skimage import io

class tomo2(Scene):
    def construct(self):
        imgs = io.imread('reconstructed_02.tif')
        print(imgs.shape)

        def get_image(imgs_list,image_number):
            return ImageMobject(imgs_list[int(image_number)]).rotate(-PI/2).scale(5)
        dot = get_image(imgs,0)
        self.add(dot)
        tick_start=0; tick_end=301
        val_tracker= ValueTracker(tick_start)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                val= int(val_trackerX.get_value())
                print(val)
                mob.become(get_image(imgs, val))
                return mob
            return UpdateFromFunc(dots, small_change2)
        tick_start=0; tick_end=50
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= smooth, run_time=3)
        tick_start=0; tick_end=100
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= smooth, run_time=3)
        tick_start=0; tick_end=175
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= smooth, run_time=3)
        tick_start=0; tick_end=301
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= smooth, run_time=3)

        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"tomo2"
    os.system(command_A + command_B)