from manimlib.imports import *

from manimlib.imports import *

def Folderscanner():
    import glob
    filenames = [img for img in glob.glob("*.png")]
    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinal(Scene):
    def construct(self):
        imgs=Folderscanner()
        print(imgs)
        title=TextMobject("K-means clustering  and Logistic Regression").set_color(BLACK)

        self.add(title.to_edge(UP))
        Img1= ImageMobject(imgs[0]).scale(3.2).to_corner(DL)
        self.add(Img1)
        t1=TextMobject("1. Measuring").set_color(BLACK).next_to(Img1,direction=RIGHT,aligned_edge=UP)

        t2=TextMobject("2. Clustering").set_color(BLACK)
        t2.next_to(t1,direction=DOWN,aligned_edge=LEFT)
        t3=TextMobject("3. Regression").set_color(BLACK)
        t3.next_to(t2,direction=DOWN,aligned_edge=LEFT)
        t4=TextMobject("4. Prediction").set_color(BLACK)
        t4.next_to(t3,direction=DOWN,aligned_edge=LEFT)
        x=VGroup(t1,t2,t3,t4).scale_in_place(0.7)
        self.add(x)
        # for i in imgs:
        #     self.wait(1)
        #     self.play(FadeIn(ImageMobject(i).scale(2.5).to_edge(UP)))
        #     self.wait(1)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -s  -c '#e6eaff' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoSceneFinal"
    os.system(command_A + command_B)
