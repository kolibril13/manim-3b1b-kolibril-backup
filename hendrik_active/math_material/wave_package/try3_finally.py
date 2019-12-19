from manimlib.imports import *

from manimlib.imports import *

def Folderscanner(interval):
    import glob
    filenames = [img for img in glob.glob(f"img_sk/{interval}*")]




    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinal1(Scene):

    def construct(self):
        def get_image(imgs_list,image_number):
            return ImageMobject(imgs_list[int(image_number)]).scale(3.4).to_edge(UP)
        imgsA=Folderscanner("A")
        imgsB=Folderscanner("B")
        imgsC=Folderscanner("C")
        imgsD=Folderscanner("D")
        print(imgsA)
        dot = get_image(imgsA,0)
        self.add(dot)
        def Tiny_Updater(dots,val_trackerX):
            def small_change2(mob):
                val= int(val_trackerX.get_value())
                print(val)
                mob.become(get_image(imgs, val))
                return mob
            return UpdateFromFunc(dots, small_change2)
        tick_start=0; tick_end=len(imgsA)
        val_tracker= ValueTracker(tick_start)
        imgs=imgsA
        t1=TextMobject("1. Measuring").set_color(BLACK).scale(0.5).next_to(dot,direction=DOWN,aligned_edge=RIGHT,buff=0.1)
        self.add(t1)
        self.wait()

        self.play(Tiny_Updater(dot,val_tracker),val_tracker.set_value,tick_end,rate_func= smooth, run_time=2.5)
        self.wait()
        dot2=get_image(imgsB,0)
        t2=TextMobject("2. Clustering").set_color(BLACK).scale(0.5).next_to(dot,direction=DOWN,aligned_edge=RIGHT,buff=0.1)
        t1.become(t2)
        self.play(FadeIn(dot2))
        dot3=get_image(imgsB,1)
        self.play(FadeIn(dot3))
        self.remove(dot)
        self.remove(dot2)
        tick_start=1; tick_end=len(imgsB)
        imgs=imgsB
        val_tracker= ValueTracker(tick_start)
        self.play(Tiny_Updater(dot2,val_tracker),val_tracker.set_value,tick_end,rate_func= linear, run_time=10)
        self.wait(1)




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p    -c '#e6eaff' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoSceneFinal1"
    os.system(command_A + command_B)
