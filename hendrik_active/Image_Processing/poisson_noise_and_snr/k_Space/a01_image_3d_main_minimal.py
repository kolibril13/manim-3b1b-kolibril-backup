from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FLOWER import FLOWER
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.a01_image_3d_main import K_Space,Realspace
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.K_MATH import ImgFourierSpace
############ ANIMATION START
scene="Minimal"
class Minimal(ThreeDScene):  # with real plane on the right
    def construct(self):
        k_plane_size=1
        pixels=30
        # k_space=ImgFourierSpace.k_from_preset_minimal(pixels,preset_position="DIAG")
        k_space=ImgFourierSpace(1)
        k_space.k_from_real_in()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        k_plane = K_Space(pixel_len=pixels)   # setup the k_plane
        k_plane.set_x(0)
        k_plane.set_y(0)
        img_kamp, img_kph = k_space.get_amp_and_ph()
        k_plane.set_z(0.01) ## why again?
        k_plane.fill_k_space(img_kamp=255*np.log2(img_kamp), dots_lines=True)
        k_plane.set_phase_flowers(img_kamp=255*np.log2(img_kamp), img_kph=img_kph)
        k_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        k_plane.set_shade_in_3d(True)

        real_in = Realspace(pixel_len=pixels)
        img_real_in = k_space.get_real_in()
        real_in.fill_real_space(img_real_in)
        real_in.scale(9 / pixels * k_plane_size * 0.3).to_edge(UL)
        self.add_fixed_in_frame_mobjects(real_in)

        real_out=Realspace(pixel_len=pixels)
        img_real= k_space.get_real_out()
        print(len(img_real))
        real_out.fill_real_space(img_real)
        self.add(k_plane)
        real_out.scale(9 / pixels * k_plane_size *0.3 ).to_edge(UR)
        self.add_fixed_in_frame_mobjects(real_out)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s  -p  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)