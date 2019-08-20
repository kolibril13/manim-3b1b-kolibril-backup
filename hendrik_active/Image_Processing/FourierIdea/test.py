from manimlib.imports import *
from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis


from manimlib.imports import *

class ImageScene(Scene):
    def construct(self):
        k_math = FourierMathJuggling()
        k_math.k_from_real_in_old_woman()
        img_in_real = k_math.get_real_in()
        print(img_in_real.shape)
        real_in = ImageMobject(np.uint8(img_in_real)).scale(1.5)
        real_in.to_edge(UL)
        real_text_in = TextMobject("Input").next_to(real_in, DOWN)
        self.add(real_in, real_text_in)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"ImageScene"
    os.system(command_A + command_B)