from hendrik_old.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling, KSpace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7


scene = "RealImage"
class RealImage(ThreeDScene):  # with real plane on the right
    CONFIG={
        "down_sample_factor":24, # cool!
        # "down_sample_factor": 50,
        "log10view":True
    }
    def construct(self):
        #self.add(Image_coordinate_system(downsampled=True))
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        k_math = FourierMathJuggling()
        k_math.k_from_real_in_from_star()
        k_math.img_k_space[9, 9] = k_math.img_k_space[9, 9] /4
        p = k_math.get_pixels()
        k_disp= KSpace(pixel_len=19)
        k_disp.overshoot_factor=0.09
        k_disp.amp_max=1000
        k_disp.fill_k_space_updater(k_math.get_amp_k_only() )
        k_disp.set_magic_gauss(0.8, sigma=0.9, mode="lowpass")
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        self.wait()



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim    -t -s -c '#1C758A' --video_dir ~/Downloads/ -o 2 "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)