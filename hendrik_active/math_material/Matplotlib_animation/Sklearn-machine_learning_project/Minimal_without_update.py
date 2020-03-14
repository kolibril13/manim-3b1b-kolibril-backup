from manimlib.imports import *

from manimlib.imports import *

def Folderscanner():
    import glob
    filenames = [img for img in glob.glob("temp/*")]
    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinal(Scene):
    def construct(self):
        imgs=Folderscanner()
        Img1= ImageMobject(imgs[0]).scale(2.5).to_edge(UP)
        self.add(Img1)
        t_5 = TexMobject(r"\Rightarrow \Psi(x, t) = \sum_j C_j \cdot e^{-i( k_j \cdot x -  \frac{k_j}{c(k_j)} \cdot t )}")
        t_5.set_color(BLACK)
        self.add(t_5.next_to(Img1,DOWN))
        for i in imgs:
              Img1.become(ImageMobject(i).scale(2.5).to_edge(UP))
              self.wait(1/60)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p   -c '#e6eaff' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoSceneFinal"
    os.system(command_A + command_B)
