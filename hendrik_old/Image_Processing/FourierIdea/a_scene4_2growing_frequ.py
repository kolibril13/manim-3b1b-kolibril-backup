from hendrik_old.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7

scene = "Scene5RealImageGownOneFreq"
class Scene5RealImageGownOneFreq(ThreeDScene):
    def construct(self):
        self.add(Image_coordinate_system(zoomed=True))
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
        img_kamp, img_kph = k_math.get_amp_and_ph_ZOOMED() # here we have a cut_off_the_top, e.g. 2
        pixels_ZOOMED = k_math.get_pixels_ZOOMED()
        k_disp = KSpace(pixel_len=pixels_ZOOMED)
        k_disp.overshoot_factor=1.8
        k_disp.fill_k_space_updater(img_kamp, new_amp_max=True)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)

        img_out_real = k_math.get_real_out()
        real_out=ImageMobject(np.uint8(img_out_real)).scale(1.5)
        real_out.to_edge(UR)
        real_text = TextMobject("Real-Space").next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)


        pos = (300, 298)
        val0 = k_math.img_k_space[pos]
        def amp_tansformer(mob):
            k_math.img_k_space[pos] = val0 * (1+40*queenstracker.get_value())
            img_kamp, img_kph = k_math.get_amp_and_ph_ZOOMED()
            k_disp.fill_k_space_updater(img_kamp)
            print("animating")
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out()
            real_out.become(ImageMobject(np.uint8(img_real)).scale(1.5).to_edge(UR))
            return mob
        queenstracker = ValueTracker(0)
        end_val=1
        self.play(queenstracker.increment_value, end_val,
                  UpdateFromFunc(k_disp, amp_tansformer),
                  rate_func=lambda t: there_and_back(t),run_time=7 )


        print("end")



if __name__ == "__main__":
    manim_main = Path.home() / "projects/manim/manim.py"
    command_A =   f"{manim_main}   -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = f"{Path(__file__).resolve()}   "
    os.system(command_A + command_B)