from hendrik_old.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7

scene = "Scene5RealImageTransformGridMaker"
class Scene5RealImageTransformGridMaker(ThreeDScene):
    def construct(self):
        self.add(Image_coordinate_system(downsampled=True))
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        k_math = FourierMathJuggling()
        k_math.k_from_real_in_old_woman() # has a 601x601 resolution
        pixels = k_math.get_pixels()

        img_in_real = k_math.get_real_in()

        self.cut_off_the_top=170
        img_kamp, img_kph = k_math.get_amp_and_ph_DOWNSAMPLED(cut_off_the_top=self.cut_off_the_top) # here we have a cut_off_the_top, e.g. 2
        pixels_DOWNSAMPLED = k_math.get_pixels_DOWNSAMPLED()
        k_disp = KSpace(pixel_len=pixels_DOWNSAMPLED)
        k_disp.overshoot_factor=1.8
        k_disp.fill_k_space_updater(img_kamp, new_amp_max=True)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        k_disp.set_magic_gauss(0, sigma=0.9, mode="lowpass")

        real_in = ImageMobject(np.uint8(img_in_real)).scale(1.5)
        real_in.to_edge(UL)
        real_text_in = TextMobject("Input").next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)

        img_out_real = k_math.get_real_out()
        real_out=ImageMobject(np.uint8(img_out_real)).scale(1.5)
        real_out.to_edge(UR)
        real_text = TextMobject("Real-Space").next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        self.play(Write(k_disp.magic_plane),rate_func=linear,run_time=2.5)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p   -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)