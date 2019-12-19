from manimlib.imports import *

from manimlib.imports import *

def Folderscanner(interval):
    import glob
    filenames = [img for img in glob.glob(f"img_sk/{interval}*")]




    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinal3(Scene):

    def construct(self):
        def get_image(imgs_list,image_number):
            return ImageMobject(imgs_list[int(image_number)]).scale(3.4).to_edge(UP)
        imgsA=Folderscanner("A")
        imgsB=Folderscanner("B")
        imgsC=Folderscanner("C")
        imgsD=Folderscanner("D")
        print(imgsD)
        dot = get_image(imgsC,15)
        self.add(dot)
        t4=TextMobject("4. Prediction").set_color(BLACK).scale(0.5).next_to(dot,direction=DOWN,aligned_edge=RIGHT,buff=0.1)
        self.add(t4)
        self.wait()
        dot3 = get_image(imgsD,0)
        bg=get_image(imgsC,15)
        dot.become(dot3)

        self.wait(1.5)

        self.play(FadeIn(get_image(imgsD,1)),run_time=1)
        self.play(FadeIn(bg.copy()),run_time=0.7)
        self.wait(0.7)

        self.add(get_image(imgsD,2))
        self.wait(0.7)


        self.play(FadeIn(get_image(imgsD,3)),run_time=1)
        self.play(FadeIn(bg.copy()),run_time=0.7)
        self.wait(0.7)


        self.add(get_image(imgsD,4))
        self.wait(0.7)

        self.play(FadeIn(get_image(imgsD,5)),run_time=1)
        self.play(FadeIn(bg.copy()),run_time=0.7)
        self.wait(0.7)




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -l -c '#e6eaff' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoSceneFinal3"
    os.system(command_A + command_B)
