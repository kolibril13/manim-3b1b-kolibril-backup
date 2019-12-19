from manimlib.imports import *

from manimlib.imports import *

def Folderscanner(interval):
    import glob
    filenames = [img for img in glob.glob(f"sk_img/{interval}*")]




    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinaljpg(Scene):

    def construct(self):
        def get_image(imgs_list,image_number):
            return ImageMobject(imgs_list[int(image_number)]).scale(3.2).to_corner(DL)
        imgs=Folderscanner("A")
        print(imgs)
        dot = get_image(imgs,0)
        self.add(dot)
        tick_start=0; tick_end=300
        val_tracker= ValueTracker(tick_start)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                val= int(val_trackerX.get_value())
                print(val)
                mob.become(get_image(imgs, val))
                return mob
            return UpdateFromFunc(dots, small_change2)
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= linear, run_time=2.5)
        self.wait()



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p   -c '#e6eaff' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoSceneFinaljpg"
    os.system(command_A + command_B)
