

from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.KSpace import KSpace
from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FourierMathJuggling import FourierMathJuggling
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.Realspace import Realspace

global k_plane_size
k_plane_size=0.7



############ ANIMATION START


scene="Minimal"  #newest and best version with only k_space
class Minimal(ThreeDScene):  # with real plane on the right
    def construct(self):
        run_setting = {"run_time": 1, "rate_func": linear}
        # GENERAL:
        postion_setting = {"preset_position": "LEFT", "center_dist": 1}
        UP_arrow = SVGMobject("arrow.svg", fill_color=ORANGE).shift(UP * 4.5)
        UP_arrow.set_shade_in_3d(True)
        self.add(UP_arrow)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        pixels = 19  # this is how it shoud be
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        k_disp.set_phase_flowers(img_kamp , img_kph)

        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels ** 2 * img_real)  ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)

        self.add(k_disp)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        self.wait()
        


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim    -p -l  -s   -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)