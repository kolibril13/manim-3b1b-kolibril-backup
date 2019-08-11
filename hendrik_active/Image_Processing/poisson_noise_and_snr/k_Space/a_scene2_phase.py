from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7



scene = "Scene2_with_phase_change_with_real_out"  # FULL ANIMATION SCENE phase with real out
class Scene2_with_phase_change_with_real_out(ThreeDScene):  # with real plane on the right

    def construct(self):
        run_setting = {"run_time": 1  , "rate_func": linear}
        postion_setting={"preset_position":"LEFT","center_dist": 1}
        # GENERAL:
        #self.add(Image_coordinate_system())
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        # pixels = 19 #this is how it shoud be
        pixels=7 # only shortly
        #math_preperation:
        #change the phase
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        self.add(k_disp)
        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels  ** 2 * img_real)  ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.phase_shift_single(val, **postion_setting)
            img_kamp, img_kph=k_math.get_amp_and_ph()
            img_real = k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 *img_real)
            mob.set_phase_flowers_updater (img_kamp, img_kph)
            mob.set_shade_in_3d(True)
            return mob

        my_phase_tracker = ValueTracker(0)
        for i in range(0,4):
            self.play(my_phase_tracker.increment_value, 90,
                      UpdateFromFunc(k_disp, update_phase),
                      rate_func=linear)
            self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p     -l  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)