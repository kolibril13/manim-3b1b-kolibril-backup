from manimlib.imports import *
from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis


from manimlib.imports import *

class ImageScene(Scene):
    def construct(self):
        array = np.random.randint(0, 255, size=(200, 200))
        img = ImageMobject(np.uint8(array)).scale(1.5)
        self.add(img)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"ImageScene"
    os.system(command_A + command_B)