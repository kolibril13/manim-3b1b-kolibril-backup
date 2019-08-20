from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7


scene = "RealImage"
class RealImage(ThreeDScene):  # with real plane on the right

    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        k_math = FourierMathJuggling()
        k_math.k_from_real_in_from_star()
        pixels = k_math.get_pixels()
        img_kamp= k_math.get_amp_k_only()

        k_disp = KSpace(pixel_len=pixels)
        k_disp.overshoot_factor=1
        k_disp.log10view=True
        k_disp.fill_k_space_updater(img_kamp,new_amp_max=True)
        k_disp.set_shade_in_3d(True)
        o = SVGMobject("./pictures/log_scale.svg")
        o.to_edge(DR).scale(0.7)
        self.add_fixed_in_frame_mobjects(o)
        self.add(k_disp)
        self.wait(2)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -s -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)