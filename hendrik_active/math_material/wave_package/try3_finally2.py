from manimlib.imports import *

from manimlib.imports import *

def Folderscanner(interval):
    import glob
    filenames = [img for img in glob.glob(f"img_sk/{interval}*")]




    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinal2(Scene):

    def construct(self):
        def get_image(imgs_list,image_number):
            return ImageMobject(imgs_list[int(image_number)]).scale(3.4).to_edge(UP)
        imgsA=Folderscanner("A")
        imgsB=Folderscanner("B")
        imgsC=Folderscanner("C")
        imgsD=Folderscanner("D")
        print(imgsA)
        dot = get_image(imgsB,14)
        self.add(dot)
        dot3 = get_image(imgsC,1)
        t3=TextMobject("3. Regression").set_color(BLACK).scale(0.5).next_to(dot,direction=DOWN,aligned_edge=RIGHT,buff=0.1)
        self.add(t3)
        self.play(FadeIn(dot3),run_time=2)
        self.wait()
        def Tiny_Updater(dots,val_trackerX):
                def small_change2(mob):
                    val= int(val_trackerX.get_value())
                    print(val)
                    mob.become(get_image(imgs, val))
                    return mob
                return UpdateFromFunc(dots, small_change2)
        tick_start=0; tick_end=len(imgsC)
        val_tracker= ValueTracker(tick_start)
        imgs=imgsC
        self.play(Tiny_Updater(dot3,val_tracker),val_tracker.set_value,tick_end,rate_func= linear, run_time=2.5)





if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -l -c '#e6eaff' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoSceneFinal2"
    os.system(command_A + command_B)
