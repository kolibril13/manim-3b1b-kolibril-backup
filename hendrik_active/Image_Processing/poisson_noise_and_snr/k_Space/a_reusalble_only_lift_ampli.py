from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

scene="Scene2_phase_no_Real"
class Scene2_phase_no_Real(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        #pixels = 19  # this is how it shoud be
        pixels=7 # only sh ortly

        # math_preperation:
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, amplitude=0)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)

        # real_out = Realspace(pixel_len=pixels)
        # img_real = k_math.get_real_out()
        # real_out.fill_real_space(pixels ** 2 * img_real)  ## why??? something with norm
        # real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        # real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        # self.add_fixed_in_frame_mobjects(real_out, real_text)

        ###HERE STARTS THE LOOP:
        Order= [("LEFT",2)]
        for o_step in range(0, len(Order)):
            postion_setting = {"preset_position": Order[o_step][0], "center_dist": Order[o_step][1]}

            # lift the amplitude
            def update_ampli(mob):
                k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting,
                                                                   amplitude=my_ampli_tracker.get_value())
                mob.fill_k_space_updater(k_math.get_amp_and_ph()[0])
                return mob

            start_val = 0;end_val = 255
            my_ampli_tracker = ValueTracker(start_val)
            self.play(my_ampli_tracker.increment_value, end_val,
                      UpdateFromFunc(k_disp, update_ampli),
                      rate_func=linear, run_time=2.5)
            self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s  -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)