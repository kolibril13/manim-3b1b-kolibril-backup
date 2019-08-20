from PIL import Image
import numpy as np  ##here???


class FourierMathJuggling(object):
    def __init__(self, img_k_space=None):
        """
        This will create a k_space object with amplitude, phase and the option of an inverse transformation
        """
        self.img_k_space = img_k_space
        if self.img_k_space is None:
            self.img_k_space = np.array([[1, 1, 2],
                                         [2, 2, 2],
                                         [2, 1, 1]])  # minimal dummy
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)
        self.img_real_in = None  # preset : no real input image

    ############ MAKE INPUT  ########
    def k_from_real_in(self, name="bw_banane.png", small_section: bool = False):  # init  ## set the input
        path = '/home/jan-hendrik/python/projects/tricks_for_python/jupyter/coffe_lecture/'
        img = Image.open(path + name)  ##open
        img_array = np.asarray(img)  # konv PIL Format in numpy format
        if small_section == True:
            img_array = img_array[::4, ::4]
            img_array = img_array[50:80, 100:130]
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)

        ## setup for the whole class
        self.img_k_space = fshift
        self.img_real_in = img_array
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)  # important, because init does not do that -.-

    def k_from_real_in_from_star(self):  # init  ## set the input
        star = np.uint8([[255, 254, 254, 255, 255, 255, 255, 255, 248, 191, 248, 255, 255,
                          255, 255, 255, 255, 255, 255],
                         [254, 255, 255, 255, 254, 255, 253, 255, 230, 109, 229, 254, 255,
                          255, 255, 255, 255, 254, 255],
                         [255, 255, 255, 255, 255, 255, 255, 255, 191, 56, 189, 255, 255,
                          255, 255, 255, 255, 255, 255],
                         [255, 255, 254, 255, 255, 255, 255, 255, 137, 47, 135, 254, 255,
                          255, 255, 255, 255, 255, 254],
                         [254, 255, 255, 255, 253, 255, 255, 239, 87, 47, 86, 237, 255,
                          255, 254, 255, 255, 255, 255],
                         [254, 255, 255, 255, 255, 255, 255, 202, 56, 47, 56, 200, 255,
                          255, 255, 255, 255, 254, 255],
                         [248, 249, 250, 250, 250, 250, 254, 149, 47, 47, 47, 146, 253,
                          250, 250, 251, 250, 249, 248],
                         [179, 113, 106, 108, 108, 108, 108, 69, 47, 47, 47, 69, 109,
                          108, 108, 108, 106, 113, 178],
                         [243, 162, 63, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47,
                          46, 47, 47, 63, 162, 243],
                         [255, 254, 200, 88, 47, 46, 46, 47, 47, 47, 47, 47, 47,
                          47, 47, 88, 200, 254, 255],
                         [255, 255, 255, 228, 122, 51, 47, 47, 47, 47, 47, 46, 47,
                          51, 120, 227, 254, 254, 255],
                         [255, 255, 254, 255, 246, 148, 49, 47, 47, 47, 47, 47, 48,
                          145, 245, 255, 254, 255, 255],
                         [254, 255, 255, 255, 254, 175, 48, 47, 48, 47, 47, 47, 47,
                          174, 255, 255, 255, 255, 255],
                         [255, 255, 255, 255, 253, 122, 47, 47, 47, 47, 47, 47, 47,
                          119, 252, 255, 255, 255, 255],
                         [254, 255, 255, 255, 230, 76, 47, 47, 60, 107, 60, 47, 47,
                          74, 228, 255, 255, 255, 255],
                         [255, 255, 255, 255, 187, 51, 47, 76, 184, 248, 186, 77, 47,
                          50, 185, 255, 255, 254, 255],
                         [255, 255, 254, 255, 133, 47, 104, 216, 255, 255, 255, 216, 106,
                          47, 130, 254, 255, 255, 255],
                         [255, 255, 255, 236, 93, 138, 236, 255, 255, 255, 255, 253, 239,
                          140, 93, 236, 255, 255, 255],
                         [255, 255, 255, 216, 174, 248, 255, 255, 255, 255, 255, 255, 254,
                          249, 175, 215, 255, 255, 255]])
        img_array = star
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)

        ## setup for the whole class
        self.img_k_space = fshift
        self.img_real_in = img_array
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)  # important, because init does not do that -.-

    def k_from_real_in_from_3x3(self):  # init  ## set the input
        star = np.uint8([[216, 174, 248],
                         [0, 10, 100],
                         [255, 255, 255]])
        img_array = star
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)

        ## setup for the whole class
        self.img_k_space = fshift
        self.img_real_in = img_array
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)  # important, because init does not do that -.-

    # make some presets for the k_space (no real in)
    @staticmethod  # init
    def k_from_preset_uniform(pixels=7):
        raster_size = (pixels, pixels)
        phi_rad = np.random.uniform(0, 2 * np.pi, raster_size)
        img_k_space_amp = np.random.uniform(0, 255, raster_size)
        img_k_space = img_k_space_amp * np.exp(1j * phi_rad)
        return FourierMathJuggling(img_k_space)
        # t = FourierMathJuggling(img_k_space) #nice idea!
        # t.pixels = pixels
        # return t

    @staticmethod
    def pixel_position(raster_size, preset_position, center_dist=1):
        pixely, pixelx = raster_size
        if preset_position == "LEFT":
            return (pixely // 2, pixelx // 2 + center_dist)
        if preset_position == "RIGHT":
            return (pixely // 2, pixelx // 2 - center_dist)
        if preset_position == "UP":
            return (pixely // 2 - center_dist, pixelx // 2)
        if preset_position == "DOWN":
            return (pixely // 2 + center_dist, pixelx // 2)
        if preset_position == "DIAG":
            return (pixely // 2 - center_dist, pixelx // 2 + center_dist)

    @staticmethod  # init
    def k_from_preset_minimal(pixels=7, preset_position="LEFT", center_dist=1, amplitude=255):
        raster_size = (pixels, pixels)
        img_k_space = np.zeros(raster_size, dtype=complex)
        loc = FourierMathJuggling.pixel_position(raster_size, preset_position, center_dist)
        img_k_space[loc] = amplitude  # but not for the center

        # if center_dist is not 0: #give it a small phase shift for nicer visualisation
        #     img_k_space[loc] = amplitude*np.exp(1j*np.pi/2)
        # else:
        #     img_k_space[loc] = amplitude # but not for the center

        return FourierMathJuggling(img_k_space)

    ############ MAKE MAGIC  ########
    def phase_shift_single(self, angle_deg, preset_position="LEFT", center_dist=1):
        pixels = self.pixels
        raster_size = (pixels, pixels)
        loc = FourierMathJuggling.pixel_position(raster_size, preset_position, center_dist)
        self.img_k_space[loc] = self.img_k_space_original[loc] * np.exp(1j * np.deg2rad(angle_deg))

    def phase_shift_all(self, angle_deg):
        self.img_k_space = self.img_k_space_original * np.exp(1j * np.deg2rad(angle_deg))

    ############ GET OUTPUT  ########
    def get_pixels(self):
        return self.pixels

    def get_amp_k_only(self):
        return np.abs(self.img_k_space)

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
        if self.img_real_in is not None:
            return self.img_real_in
        else:
            raise Exception('There is no input image actually, sorry!')

    def get_real_out(self):
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(self.img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)  ####
        # out=real_out_ar.real ##???? right???
        out = real_out_ar.real
        return out

    ### mask section
    @staticmethod
    def linear_step_func(x, x0, x1):
        y = np.piecewise(x, [
            x < x0,
            (x >= x0) & (x <= x1),
            x > x1],
                         [0.,
                          lambda x: x / (x1 - x0) + x0 / (x0 - x1),
                          1.]
                         )
        return y

    def setup_order(self, order):
        self.order = order

    def make_mask(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
        mask = np.full(raster, self.linear_step_func(step, 1, 1.2))
        num_of_orders = len(self.order)
        for number, (position_s, center_s) in enumerate(self.order):
            pos = self.pixel_position(raster, position_s, center_s)
            start_p = number / num_of_orders
            end_p = (number + 1) / num_of_orders
            # print(number / num_of_orders, "bis", (number + 1) / num_of_orders, position_s, center_s)
            mask[pos] = self.linear_step_func(step, start_p, end_p)
        return mask

    def apply_mask(self, t):
        mask = self.make_mask(t)
        self.img_k_space = self.img_k_space_original * mask

    ### gaussian filtering:

    def make_gauss(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
        mask = np.full(raster, self.linear_step_func(step, 1, 1.2))
        x, y = np.meshgrid(np.linspace(-1, 1, self.pixels), np.linspace(-1, 1, self.pixels))
        d = np.sqrt(x * x + y * y)
        sigma, mu = 1.0, 0.0
        g_mask = 1 - step * np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
        return g_mask

    def apply_transformations(self, t):
        g_mask = self.make_gauss(t)
        self.img_k_space = self.img_k_space_original * g_mask

    from PIL import Image


import numpy as np  ##here???


class FourierMathJuggling(object):
    def __init__(self, img_k_space=None):
        """
        This will create a k_space object with amplitude, phase and the option of an inverse transformation
        """
        self.img_k_space = img_k_space
        if self.img_k_space is None:
            self.img_k_space = np.array([[1, 1, 2],
                                         [2, 2, 2],
                                         [2, 1, 1]])  # minimal dummy
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)
        self.img_real_in = None  # preset : no real input image

    ############ MAKE INPUT  ########
    def k_from_real_in_old_woman(self):
        name = "woman2x.png"
        self.k_from_real_in(name=name)
    def k_from_real_in(self, name="woman2x.png", small_section: bool = False):  # init  ## set the input
        path = './pictures/'
        img = Image.open(path + name)  ##open
        img_array = np.asarray(img)  # konv PIL Format in numpy format
        self.pixels= min(img_array.shape)
        img_array= img_array[0:self.pixels, 0:self.pixels]
        if small_section == True:
            img_array = img_array[::4, ::4]
            img_array = img_array[50:80, 100:130]
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)

        ## setup for the whole class
        self.img_k_space = fshift
        self.img_real_in = img_array
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)  # important, because init does not do that -.-

    def k_from_real_in_from_star(self):  # init  ## set the input
        star = np.uint8([[255, 254, 254, 255, 255, 255, 255, 255, 248, 191, 248, 255, 255,
                          255, 255, 255, 255, 255, 255],
                         [254, 255, 255, 255, 254, 255, 253, 255, 230, 109, 229, 254, 255,
                          255, 255, 255, 255, 254, 255],
                         [255, 255, 255, 255, 255, 255, 255, 255, 191, 56, 189, 255, 255,
                          255, 255, 255, 255, 255, 255],
                         [255, 255, 254, 255, 255, 255, 255, 255, 137, 47, 135, 254, 255,
                          255, 255, 255, 255, 255, 254],
                         [254, 255, 255, 255, 253, 255, 255, 239, 87, 47, 86, 237, 255,
                          255, 254, 255, 255, 255, 255],
                         [254, 255, 255, 255, 255, 255, 255, 202, 56, 47, 56, 200, 255,
                          255, 255, 255, 255, 254, 255],
                         [248, 249, 250, 250, 250, 250, 254, 149, 47, 47, 47, 146, 253,
                          250, 250, 251, 250, 249, 248],
                         [179, 113, 106, 108, 108, 108, 108, 69, 47, 47, 47, 69, 109,
                          108, 108, 108, 106, 113, 178],
                         [243, 162, 63, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47,
                          46, 47, 47, 63, 162, 243],
                         [255, 254, 200, 88, 47, 46, 46, 47, 47, 47, 47, 47, 47,
                          47, 47, 88, 200, 254, 255],
                         [255, 255, 255, 228, 122, 51, 47, 47, 47, 47, 47, 46, 47,
                          51, 120, 227, 254, 254, 255],
                         [255, 255, 254, 255, 246, 148, 49, 47, 47, 47, 47, 47, 48,
                          145, 245, 255, 254, 255, 255],
                         [254, 255, 255, 255, 254, 175, 48, 47, 48, 47, 47, 47, 47,
                          174, 255, 255, 255, 255, 255],
                         [255, 255, 255, 255, 253, 122, 47, 47, 47, 47, 47, 47, 47,
                          119, 252, 255, 255, 255, 255],
                         [254, 255, 255, 255, 230, 76, 47, 47, 60, 107, 60, 47, 47,
                          74, 228, 255, 255, 255, 255],
                         [255, 255, 255, 255, 187, 51, 47, 76, 184, 248, 186, 77, 47,
                          50, 185, 255, 255, 254, 255],
                         [255, 255, 254, 255, 133, 47, 104, 216, 255, 255, 255, 216, 106,
                          47, 130, 254, 255, 255, 255],
                         [255, 255, 255, 236, 93, 138, 236, 255, 255, 255, 255, 253, 239,
                          140, 93, 236, 255, 255, 255],
                         [255, 255, 255, 216, 174, 248, 255, 255, 255, 255, 255, 255, 254,
                          249, 175, 215, 255, 255, 255]])
        img_array = star
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)

        ## setup for the whole class
        self.img_k_space = fshift
        self.img_real_in = img_array
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)  # important, because init does not do that -.-

    def k_from_real_in_from_3x3(self):  # init  ## set the input
        star = np.uint8([[216, 174, 248],
                         [0, 10, 100],
                         [255, 255, 255]])
        img_array = star
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)

        ## setup for the whole class
        self.img_k_space = fshift
        self.img_real_in = img_array
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)  # important, because init does not do that -.-

    # make some presets for the k_space (no real in)
    @staticmethod  # init
    def k_from_preset_uniform(pixels=7):
        raster_size = (pixels, pixels)
        phi_rad = np.random.uniform(0, 2 * np.pi, raster_size)
        img_k_space_amp = np.random.uniform(0, 255, raster_size)
        img_k_space = img_k_space_amp * np.exp(1j * phi_rad)
        return FourierMathJuggling(img_k_space)
        # t = FourierMathJuggling(img_k_space) #nice idea!
        # t.pixels = pixels
        # return t

    @staticmethod
    def pixel_position(raster_size, preset_position, center_dist=1):
        pixely, pixelx = raster_size
        if preset_position == "LEFT":
            return (pixely // 2, pixelx // 2 + center_dist)
        if preset_position == "RIGHT":
            return (pixely // 2, pixelx // 2 - center_dist)
        if preset_position == "UP":
            return (pixely // 2 - center_dist, pixelx // 2)
        if preset_position == "DOWN":
            return (pixely // 2 + center_dist, pixelx // 2)
        if preset_position == "DIAG":
            return (pixely // 2 - center_dist, pixelx // 2 + center_dist)

    @staticmethod  # init
    def k_from_preset_minimal(pixels=7, preset_position="LEFT", center_dist=1, amplitude=255):
        raster_size = (pixels, pixels)
        img_k_space = np.zeros(raster_size, dtype=complex)
        loc = FourierMathJuggling.pixel_position(raster_size, preset_position, center_dist)
        img_k_space[loc] = amplitude  # but not for the center

        # if center_dist is not 0: #give it a small phase shift for nicer visualisation
        #     img_k_space[loc] = amplitude*np.exp(1j*np.pi/2)
        # else:
        #     img_k_space[loc] = amplitude # but not for the center

        return FourierMathJuggling(img_k_space)

    ############ MAKE MAGIC  ########
    def phase_shift_single(self, angle_deg, preset_position="LEFT", center_dist=1):
        pixels = self.pixels
        raster_size = (pixels, pixels)
        loc = FourierMathJuggling.pixel_position(raster_size, preset_position, center_dist)
        self.img_k_space[loc] = self.img_k_space_original[loc] * np.exp(1j * np.deg2rad(angle_deg))

    def phase_shift_all(self, angle_deg):
        self.img_k_space = self.img_k_space_original * np.exp(1j * np.deg2rad(angle_deg))

    ############ GET OUTPUT  ########
    def get_pixels(self):
        return self.pixels
    def get_pixels_DOWNSAMPLED(self):
        return self.pixels_DOWNSAMPLED

    def get_amp_k_only(self):
        return np.abs(self.img_k_space)

    def get_amp_and_ph(self):
        img_kamp = np.abs(self.img_k_space)
        img_kph = (np.angle(self.img_k_space, deg=True))
        return img_kamp, img_kph

    def get_amp_and_ph_DOWNSAMPLED(self, sample_fac):
        self.img_k_space_downsampled = self.img_k_space[0::sample_fac, 0::sample_fac]
        img_kamp = np.abs(self.img_k_space_downsampled)
        img_kph = (np.angle(self.img_k_space_downsampled, deg=True))
        self.pixels_DOWNSAMPLED= len(self.img_k_space_downsampled)
        return img_kamp, img_kph

    def get_real_in(self):  ## get the input
        if self.img_real_in is not None:
            return self.img_real_in
        else:
            raise Exception('There is no input image actually, sorry!')

    def get_real_out(self):
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(self.img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)  ####
        # out=real_out_ar.real ##???? right???
        out = real_out_ar.real
        return out

    ### mask section
    @staticmethod
    def linear_step_func(x, x0, x1):
        y = np.piecewise(x, [
            x < x0,
            (x >= x0) & (x <= x1),
            x > x1],
                         [0.,
                          lambda x: x / (x1 - x0) + x0 / (x0 - x1),
                          1.]
                         )
        return y

    def setup_order(self, order):
        self.order = order

    def make_mask(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
        mask = np.full(raster, self.linear_step_func(step, 1, 1.2))
        num_of_orders = len(self.order)
        for number, (position_s, center_s) in enumerate(self.order):
            pos = self.pixel_position(raster, position_s, center_s)
            start_p = number / num_of_orders
            end_p = (number + 1) / num_of_orders
            # print(number / num_of_orders, "bis", (number + 1) / num_of_orders, position_s, center_s)
            mask[pos] = self.linear_step_func(step, start_p, end_p)
        return mask

    def apply_mask(self, t):
        mask = self.make_mask(t)
        self.img_k_space = self.img_k_space_original * mask

    ### gaussian filtering:

    def param_gauss_low_juggling(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
        mask = np.full(raster, self.linear_step_func(step, 1, 1.2))
        x, y = np.meshgrid(np.linspace(-1, 1, self.pixels), np.linspace(-1, 1, self.pixels))
        d = np.sqrt(x * x + y * y)
        mu = 0
        sigma = self.sigma
        g_mask = 1 - (1 - np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))) * step
        return g_mask

    def param_gauss_high_juggling(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
        mask = np.full(raster, self.linear_step_func(step, 1, 1.2))
        x, y = np.meshgrid(np.linspace(-1, 1, self.pixels), np.linspace(-1, 1, self.pixels))
        d = np.sqrt(x * x + y * y)
        mu = 0
        sigma = self.sigma
        g_mask = 1 - step * np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
        return g_mask

    def apply_transformations(self, t, sigma, mode: str):
        self.sigma = sigma
        if mode == "lowpass":
            self.plane_func = self.param_gauss_low_juggling
        if mode == "highpass":
            self.plane_func = self.param_gauss_high_juggling
        g_mask = self.plane_func(t)
        self.img_k_space = self.img_k_space_original * g_mask

    def __str__(self):
        return f"The image of the k space looks like this \n {self.img_k_space}"


if __name__ == "__main__":
    pix = (7, 7)
    Order = [("LEFT", 1), ("UP", 3), ("UP", 1), ("UP", -1), ("DIAG", 2), ("DIAG", 1), ("UP", 0)]
    array = np.ones(pix) * 4
    mama = FourierMathJuggling(array)
    mama.apply_transformations(1, sigma=0.2, mode="highpass")
    # mama.apply_transformations(1, sigma=0.2 , mode= "lowpass")

    x = mama.get_amp_k_only()
    plt.rcParams['figure.dpi'] = 100
    sns.heatmap(x, annot=True)