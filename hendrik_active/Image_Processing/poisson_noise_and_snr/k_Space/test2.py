from manimlib.imports import *

class ImgFourierSpace:
    def __init__(self,img_k_space,pixels = 7  ):
        """
        This will create a k_space object with amplitude, phase and the option of an inverse transformation
        """
        self.pixels=pixels
        self.img_k_space = img_k_space

    @staticmethod
    def from_preset_uniform(pixels=7):
        raster_size = (pixels, pixels)
        phi_rad = np.random.uniform(0, 2 * np.pi, raster_size)
        img_k_space = np.ones(raster_size, dtype=complex)
        img_k_space = img_k_space * np.exp(1j * phi_rad)
        return ImgFourierSpace(img_k_space,pixels)

    @staticmethod
    def from_preset_minimal(pixels = 7):
        raster_size = (pixels, pixels)
        img_k_space = np.zeros(raster_size, dtype=complex)
        img_k_space[pixels//2, pixels//2+1] = 255 * np.exp(1j * 2 / 3 * np.pi)
        return ImgFourierSpace(img_k_space,pixels)


    def get_amp_and_ph(self):
        img_kamp = np.abs(self.img_k_space)
        img_kph = (np.angle(self.img_k_space, deg=True))
        return img_kamp, img_kph
    def get_low_resolution(self):
        pass

    def phase_shift_all(self,angle_deg):
        pixels=self.pixels
        # self.img_k_space[pixels // 2, pixels // 2 + 1] = \
        # self.img_k_space[pixels // 2, pixels // 2 + 1] *np.exp(1j * np.deg2rad(angle_deg))
        self.img_k_space= self.img_k_space* np.exp(1j*np.deg2rad(angle_deg))

    def phase_shift_single(self,angle_deg):
        pixels = self.pixels
        self.img_k_space[pixels // 2, pixels // 2 + 1] = \
        self.img_k_space[pixels // 2, pixels // 2 + 1] *np.exp(1j * np.deg2rad(angle_deg))

    def get_real_out(self):
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(self.img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)
        return real_out_ar.real

    def __str__(self):
        return f"The image of the k space looks like this \n {self.img_k_space}"

k=ImgFourierSpace.from_preset_minimal()
print(k)

k2= k.get_real_out()
print(k2)

