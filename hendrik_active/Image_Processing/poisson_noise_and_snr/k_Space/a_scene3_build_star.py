from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7


scene = "Scene3_build_star"  # FULL ANIMATION SCENE phase with real out
class Scene3_build_star(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        pixels = 19  # this is how it shoud be

        k_math = FourierMathJuggling(None,pixels=12)
        k_math.k_from_real_in_from_star()
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        print(img_kamp)
        k_disp.fill_k_space_updater((img_kamp/img_kamp.max())*10000)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space( img_real)
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)

        real_in = Realspace(pixel_len=pixels)
        img_in_real = k_math.get_real_in()
        real_in.fill_real_space(img_in_real)
        real_in.scale(9 / pixels * k_plane_size * 0.3).to_edge(UL)
        real_text_in = TextMobject("Input").scale(0.75).next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)

        self.wait(2)

        # ##HERE STARTS THE LOOP:
        # ####change the phase
        # postion_setting = {"preset_position": "LEFT", "center_dist":2}
        # def update_phase(mob):
        #     val= my_phase_tracker.get_value()
        #     k_math.phase_shift_single(val, **postion_setting)
        #     img_kamp, img_kph=k_math.get_amp_and_ph()
        #     mob.set_phase_flowers_updater (img_kamp, img_kph)
        #     mob.set_shade_in_3d(True)
        #     img_real = k_math.get_real_out()
        #     real_out.fill_real_space(pixels ** 2 * img_real)
        #     return mob
        # my_phase_tracker = ValueTracker(0)
        # for i in range(0,4):
        #     self.play(my_phase_tracker.increment_value, 90,
        #               UpdateFromFunc(k_disp, update_phase),
        #               rate_func=linear)
        #     print("ye")
        #     self.wait(1)
        # self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s   -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)