from hendrik_old.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7

scene = "Scene5RealImageTransformHeighpass"
class Scene5RealImageTransformHeighpass(ThreeDScene):
    def construct(self):
        self.add(Image_coordinate_system(downsampled=True))
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        k_math = FourierMathJuggling()
        k_math.k_from_real_in_old_woman() # has a 601x601 resolution
        pixels = k_math.get_pixels()

        img_in_real = k_math.get_real_in()
        real_in = ImageMobject(np.uint8(img_in_real)).scale(1.5)
        real_in.to_edge(UL)
        real_text_in = TextMobject("Input").next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)
        img_kamp, img_kph = k_math.get_amp_and_ph_DOWNSAMPLED() # here we have a cut_off_the_top, e.g. 2
        pixels_DOWNSAMPLED = k_math.get_pixels_DOWNSAMPLED()
        k_disp = KSpace(pixel_len=pixels_DOWNSAMPLED)
        k_disp.overshoot_factor=1.8
        k_disp.fill_k_space_updater(img_kamp, new_amp_max=True)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        print(pixels_DOWNSAMPLED)
        img_out_real = k_math.get_real_out()
        real_out=ImageMobject(np.uint8(img_out_real)).scale(1.5)
        real_out.to_edge(UR)
        real_text = TextMobject("Real-Space").next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)

        def apply_filter(mob):
            val = queenstracker.get_value()
            #k_math.apply_transformations(val,sigma=0.05,mode="lowpass")
            #k_disp.set_magic_gauss(val,sigma=0.9, mode="lowpass")
            k_math.apply_transformations(val, sigma=0.2, mode="highpass")
            k_disp.set_magic_gauss(val, sigma=0.6, mode="highpass")
            img_kamp, img_kph = k_math.get_amp_and_ph_DOWNSAMPLED()
            k_disp.fill_k_space_updater(img_kamp)
            print("animating")
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out_strectched()
            real_out.become(ImageMobject(np.uint8(img_real)).scale(1.5).to_edge(UR))
            return mob

        queenstracker = ValueTracker(0)
        end_val = 0.999
        self.play(queenstracker.increment_value, end_val,
                  UpdateFromFunc(k_disp, apply_filter),
                  rate_func=lambda t: there_and_back(t), run_time=12)
        # self.play(queenstracker.increment_value, end_val,
        #          UpdateFromFunc(k_disp, apply_filter),rate_func=linear)




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p   -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)