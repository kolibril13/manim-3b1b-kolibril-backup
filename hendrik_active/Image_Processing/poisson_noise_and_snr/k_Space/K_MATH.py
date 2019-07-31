from PIL import Image
import numpy as np ##here???
class ImgFourierSpace:
    def __init__(self, img_k_space, pixels=7):
        """
        This will create a k_space object with amplitude, phase and the option of an inverse transformation
        """
        self.pixels = pixels
        self.img_k_space = img_k_space

    ############ MAKE INPUT  ########
    def k_from_real_in(self):  # init  ## set the input
        path = '/home/jan-hendrik/python/projects/tricks_for_python/jupyter/coffe_lecture/'
        name = "bw_banane.png"
        img = Image.open(path + name)  ##open
        img_array = np.asarray(img)  # konv PIL Format in numpy format
        print(img_array)
        img_array = img_array[::4,::4]
        img_array= img_array[50:80,100:130]
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)
        ## setup for the whole class
        self.img_k_space = fshift
        self.img_realin = img_array

    # make some presets for the k_space (no real in)
    @staticmethod  # init
    def k_from_preset_uniform(pixels=7):
        raster_size = (pixels, pixels)
        phi_rad = np.random.uniform(0, 2 * np.pi, raster_size)
        img_k_space_amp = np.random.uniform(0,255,raster_size)
        img_k_space = img_k_space_amp * np.exp(1j * phi_rad)
        return ImgFourierSpace(img_k_space, pixels)

    @staticmethod
    def pixel_position(raster_size, preset_position, center_dist=1):
        pixely, pixelx = raster_size
        if preset_position == "LEFT":
            return (pixelx // 2, pixely // 2 - center_dist)
        if preset_position == "RIGHT":
            return (pixelx // 2, pixely // 2 + center_dist)
        if preset_position == "UP":
            return (pixelx // 2 - center_dist, pixely // 2)
        if preset_position == "DOWN":
            return (pixelx // 2 + center_dist, pixely // 2)
        if preset_position == "DIAG":
            return (pixelx // 2 + center_dist, pixely // 2 + center_dist)

    @staticmethod  # init
    def k_from_preset_minimal(pixels=7, preset_position="LEFT", center_dist=1):
        raster_size = (pixels, pixels)
        img_k_space = np.zeros(raster_size, dtype=complex)
        loc = ImgFourierSpace.pixel_position(raster_size, preset_position, center_dist)
        img_k_space[loc] = 255
        return ImgFourierSpace(img_k_space, pixels)

    ############ MAKE MAGIC  ########

    def phase_shift_all(self, angle_deg):
        pixels = self.pixels
        # self.img_k_space[pixels // 2, pixels // 2 + 1] = \
        # self.img_k_space[pixels // 2, pixels // 2 + 1] *np.exp(1j * np.deg2rad(angle_deg))
        self.img_k_space = self.img_k_space * np.exp(1j * np.deg2rad(angle_deg))

    def phase_shift_single(self, angle_deg):
        pixels = self.pixels
        self.img_k_space[pixels // 2, pixels // 2 + 1] = \
            self.img_k_space[pixels // 2, pixels // 2 + 1] * np.exp(1j * np.deg2rad(angle_deg))

    ############ GET OUTPUT  ########

    def get_amp_and_ph(self):
        img_kamp = np.abs(self.img_k_space)
        img_kph = (np.angle(self.img_k_space, deg=True))
        return img_kamp, img_kph

    def get_amp_and_ph_DOWNSAMPLED(self, sample_fac):
        self.img_k_space_downsampled = self.img_k_space[0::sample_fac, 0::sample_fac]
        img_kamp = np.abs(self.img_k_space_downsampled)
        img_kph = (np.angle(self.img_k_space_downsampled, deg=True))
        return img_kamp, img_kph

    def get_real_in(self):  ## get the input
        return self.img_realin

    def get_real_out(self):
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(self.img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)
        return real_out_ar.real

    def __str__(self):
        return f"The image of the k space looks like this \n {self.img_k_space}"