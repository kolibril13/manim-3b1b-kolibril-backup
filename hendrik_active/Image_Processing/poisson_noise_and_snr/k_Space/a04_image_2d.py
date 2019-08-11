from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.a01_image_3d_main import Realspace
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.KSpace import KSpace


class Image2dTesting(Scene):
    def construct(self):
        pixels = 7  # setup the sizes
        raster_size = (pixels, pixels)
        r = np.random.uniform(0, 255, raster_size)  # setup function
        phi_rad = np.full(raster_size, 5)
        phi_rad= np.linspace(0,2*np.pi-0.01,pixels*pixels).reshape(raster_size)
        img_k_space = r * np.exp(1j * phi_rad)
        img_kamp = np.abs(img_k_space)
        img_kph = (np.angle(img_k_space, deg=True))
        my_plane= KSpace(pixel_len=pixels)
        my_plane.set_phase_flowers(img_kamp,img_kph )
        my_plane.move_to(ORIGIN)
        my_plane.fill_k_space(img_kamp)
        self.add(my_plane)

class ImgFourierSpace:
    def __init__(self,preset=None,pixels = 7  ):
        self.pixels=pixels
        raster_size = (pixels, pixels)
        if preset == "uniform":
            phi_rad = np.random.uniform(0, 2 * np.pi, raster_size)
            self.img_k_space = np.ones(raster_size, dtype=complex)
            self.img_k_space=self.img_k_space* np.exp(1j *phi_rad)
        if preset == "minimal":
            self.img_k_space = np.zeros(raster_size, dtype=complex)
            self.img_k_space[pixels//2, pixels//2+1] = 255 * np.exp(1j * 2 / 3 * np.pi)

        else:
            pass

    def get_amp_and_ph(self):
        img_kamp = np.abs(self.img_k_space)
        img_kph = (np.angle(self.img_k_space, deg=True))
        return img_kamp, img_kph

    def phase_shift(self,angle_deg):
        pixels=self.pixels
        # self.img_k_space[pixels // 2, pixels // 2 + 1] = \
        # self.img_k_space[pixels // 2, pixels // 2 + 1] *np.exp(1j * np.deg2rad(angle_deg))

        self.img_k_space= self.img_k_space* np.exp(1j*np.deg2rad(angle_deg))

    def get_real_out(self):
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(self.img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)
        return real_out_ar.real

class Image2dFourierScene(Scene):
    def construct(self):
        pixels = 21  # setup the sizes
        imp_fourier_instance = ImgFourierSpace(preset="minimal",pixels=pixels)
        # imp_fourier_instance.phase_shift(190)
        print("ss")
        img_kamp,img_kph= imp_fourier_instance.get_amp_and_ph()
        my_plane = KSpace(pixel_len=pixels) ###
        my_plane.set_phase_flowers(img_kamp, img_kph)
        my_plane.move_to(ORIGIN)
        my_plane.scale(6/pixels)
        my_plane.fill_k_space(img_kamp)
        self.add(my_plane)

        img_real=imp_fourier_instance.get_real_out()
        real_out_plane = Realspace(pixel_len=pixels)###
        real_out_plane.fill_real_space(img_real)
        real_out_plane.scale(9 / pixels  * 0.4).to_edge(UR)
        all2 = real_out_plane
        self.add(all2)

class Image2dFourierSceneEX(Scene):
    def construct(self):
        pixels = 21  # setup the sizes

        gu = ImgFourierSpace(preset="minimal",pixels=pixels)
        img_realUR= gu.get_real_out()

        realUR = Realspace(pixel_len=pixels)###
        realUR.fill_real_space(img_realUR)
        realUR.scale(9 / pixels  * 0.4).to_edge(UR)
        self.add(realUR)

        gu.phase_shift(180)
        print("ss")
        img_kamp,img_kph= gu.get_amp_and_ph()
        my_plane = KSpace(pixel_len=pixels) ###
        my_plane.set_phase_flowers(img_kamp, img_kph)
        my_plane.move_to(ORIGIN)
        my_plane.scale(6/pixels)
        my_plane.fill_k_space(img_kamp)
        self.add(my_plane)

        img_real=gu.get_real_out()
        realM = Realspace(pixel_len=pixels)###
        realM.fill_real_space(img_real)
        realM.scale(9 / pixels  * 0.4).next_to(realUR,DOWN)
        self.add(realM)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s     -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Image2dFourierSceneEX"
    os.system(command_A + command_B)