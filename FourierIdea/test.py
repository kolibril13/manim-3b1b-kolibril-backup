from hendrik_old.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling, Realspace
from manimlib.imports import *

class laalaa(Scene):
    def construct(self):
        k_math= FourierMathJuggling()
        k_math.k_from_real_in_old_woman()
        pixels=k_math.get_pixels()
        woman=k_math.get_real_in()
        print("yes")

        image_disp=Realspace(pixels)
        image_disp.fill_real_space(woman)
        self.add(image_disp)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"laalaa"
    os.system(command_A + command_B)