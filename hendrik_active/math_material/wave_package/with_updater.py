from manimlib.imports import *


def Folderscanner():
    import glob, os
    # os.chdir("temp/")
    filenames = [img for img in glob.glob("temp/*")]
    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinal_try2(Scene):
    def construct(self):
        def get_image(imgs_list,image_number):
            return ImageMobject(imgs_list[int(image_number)])
        imgs=Folderscanner()
        dot = get_image(imgs,0)
        self.add(dot)
        tick_start=0; tick_end=59
        val_tracker= ValueTracker(tick_start)
        def Tiny_Updater(dots,val_trackerX):
                def small_change2(mob):
                    val= int(val_trackerX.get_value())
                    print(val)
                    mob.become(get_image(imgs, val))
                    return mob
                return UpdateFromFunc(dots, small_change2)
        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= linear)
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"VideoSceneFinal_try2"
    os.system(command_A + command_B)