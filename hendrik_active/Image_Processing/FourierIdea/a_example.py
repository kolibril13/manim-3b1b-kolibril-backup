from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis
from manimlib.imports import *


scene = "Example"
class Example(ThreeDScene):
    def construct(self):
        self.add(Image_coordinate_system(downsampled=True))
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        k_math = FourierMathJuggling()
        k_math.k_from_real_in_old_woman() # has a 601x601 resolution

        img_in_real = k_math.get_real_in()
        real_in = ImageMobject(np.uint8(img_in_real)).scale(1.5)
        real_in.to_edge(UL)
        real_text_in = TextMobject("Input").next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)
        self.cut_off_the_top=170
        img_kamp, img_kph = k_math.get_amp_and_ph_DOWNSAMPLED(cut_off_the_top=self.cut_off_the_top) # here we have a cut_off_the_top, e.g. 2
        pixels_DOWNSAMPLED = k_math.get_pixels_DOWNSAMPLED()
        k_disp = KSpace(pixel_len=pixels_DOWNSAMPLED)
        k_disp.overshoot_factor=1.8
        k_disp.fill_k_space_updater(img_kamp, new_amp_max=True)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        img_out_real = k_math.get_real_out()
        real_out=ImageMobject(np.uint8(img_out_real)).scale(1.5)
        real_out.to_edge(UR)
        real_text = TextMobject("Real-Space").next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        val=0.8
        k_math.apply_transformations(val,sigma=0.05,mode="lowpass")
        k_disp.set_magic_gauss(val,sigma=0.9, mode="lowpass")
        img_kamp, img_kph = k_math.get_amp_and_ph_DOWNSAMPLED(cut_off_the_top=self.cut_off_the_top)
        k_disp.fill_k_space_updater(img_kamp)
        img_real = k_math.get_real_out()
        real_out.become(ImageMobject(np.uint8(img_real)).scale(1.5).to_edge(UR))

## this is done for pycharm
# if __name__ == "__main__":
#     module_name = os.path.basename(__file__)
#     command_A = "manim   -p  -s  -c '#1C758A' --video_dir ~/Downloads/  "
#     command_B = module_name +" " + scene
#     os.system(command_A + command_B)