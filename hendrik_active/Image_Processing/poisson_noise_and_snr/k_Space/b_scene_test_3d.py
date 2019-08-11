

from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.KSpace import KSpace
from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FourierMathJuggling import FourierMathJuggling
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.Realspace import Realspace

global k_plane_size
k_plane_size=0.7


scene = "Scene2_with_phase_change_try3"  # FULL ANIMATION SCENE phase but no real_out
class Scene2_with_phase_change_try3(ThreeDScene):  # with real plane on the right

    def construct(self):
        run_setting = {"run_time": 1  , "rate_func": linear}
        postion_setting={"preset_position":"LEFT","center_dist": 1}
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        #pixels = 19 #this is how it shoud be
        pixels=3 # only shortly
        #math_preperation:
        k_math=FourierMathJuggling.k_from_preset_minimal(pixels,**postion_setting)
        k_disp= KSpace(pixel_len=pixels)
        img_kamp,img_kph= k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        self.add(k_disp)

        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        k_disp.set_phase_flowers((img_kamp * 10 / 360), img_kph)
        # k_disp.r()
        self.add(k_disp)

        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.phase_shift_single(val, **postion_setting)
            img_kamp, img_kph=k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater (img_kamp, img_kph)
            mob.set_shade_in_3d(True)
            return mob
        my_phase_tracker = ValueTracker(0)
        for i in range(0,2):
            self.play(my_phase_tracker.increment_value, 90,  # <- "Master" update first
                      UpdateFromFunc(k_disp, update_phase),
                      rate_func=linear)
            self.wait(1)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim    -p      -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)