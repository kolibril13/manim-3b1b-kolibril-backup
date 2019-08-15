from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis


class se(Scene):
    def construct(self):
        x=Comp_axis()
        self.add(x)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -s  -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"se"
    os.system(command_A + command_B)