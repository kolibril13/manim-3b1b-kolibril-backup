from manimlib.imports import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from skimage import io

class tomo_sino(Scene):
    def construct(self):
        imgs = io.imread('proj_MBA-1.tif')
        print(imgs.shape)
        imgs= [ imgs[:,:,i] for i in range(824) ]
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
        tick_start=500; tick_end=650
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= smooth, run_time=5)
        tick_start=650; tick_end=800
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= smooth, run_time=5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"tomo_sino"
    os.system(command_A + command_B)