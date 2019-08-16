

from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.KSpace import KSpace
from manimlib.imports import *
from hendrik_active.Image_Processing.FourierIdea.FourierMathJuggling import FourierMathJuggling

global k_plane_size
k_plane_size=0.7



############ ANIMATION START


scene="Minimal"  #newest and best version with only k_space
class Minimal(ThreeDScene):  # with real plane on the right #nice camera twister
    def construct(self):
        self.set_camera_orientation(phi=50 * DEGREES, theta= 0* DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        pixels = 11  # this is how it shoud be
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        self.add(k_disp)
        self.wait()
        self.move_camera(phi=80 * DEGREES, theta=-PI /  2)
        self.wait()
        


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim    -p -l     -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)