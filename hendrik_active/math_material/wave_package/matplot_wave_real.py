from manimlib.imports import *

from manimlib.imports import *

def Folderscanner():
    import glob, os
   # os.chdir("temp/")
    filenames = [img for img in glob.glob("temp/*")]
    filenames.sort() # ADD THIS LINE
    return filenames

class VideoSceneFinal(Scene):
    def construct(self):
        imgs=Folderscanner()
        print(imgs)
        Img1= imgs[3]
        self.add(ImageMobject(Img1).scale(3))
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p -s -c '#e6eaff' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "VideoSceneFinal"
    os.system(command_A + command_B)
