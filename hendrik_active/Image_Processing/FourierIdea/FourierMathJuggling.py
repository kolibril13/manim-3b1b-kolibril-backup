from PIL import Image
from PIL import  ImageOps
import numpy as np


class StepFunctions:
    @staticmethod
    def spiral(width, height):
        NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
        turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction
        x, y = width // 2, height // 2  # start near the center
        dx, dy = NORTH  # initial direction
        matrix = [[None] * width for _ in range(height)]
        count = 0
        while True:
            count += 1
            matrix[y][x] = count  # visit
            # try to turn right
            new_dx, new_dy = turn_right[dx, dy]
            new_x, new_y = x + new_dx, y + new_dy
            if (0 <= new_x <= width and 0 <= new_y <= height and
                    matrix[new_y][new_x] is None):  # can turn right
                x, y = new_x, new_y
                dx, dy = new_dx, new_dy
            else:  # try to move straight
                x, y = x + dx, y + dy
                if not (0 <= x < width and 0 <= y < height):
                    return np.array(matrix, dtype=float)  # nowhere to go

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

    @staticmethod
    def step_machine(matrix_counter, order_parameter):
        total_time = 0
        interval_timeA = 25
        matix_max_A = 9
        if 1 <= matrix_counter < matix_max_A:
            p1 = total_time + (matrix_counter - 1) * interval_timeA / matix_max_A
            p2 = total_time + (matrix_counter) * interval_timeA / matix_max_A
            return StepFunctions.linear_step_func(order_parameter, p1, p2)
        total_time += interval_timeA

        interval_timeB = 25
        matix_max_B = 25
        if 4 <= matrix_counter <= matix_max_B:
            p1 = total_time + (matrix_counter - 1) * interval_timeB / matix_max_B
            p2 = total_time + (matrix_counter) * interval_timeB / matix_max_B
            return StepFunctions.linear_step_func(order_parameter, p1, p2)
        total_time += interval_timeB

        interval_timeC = 25
        matix_max_C = 81
        if 4 <= matrix_counter <= matix_max_C:
            p1 = total_time + (matrix_counter - 1) * interval_timeC / matix_max_C
            p2 = total_time + (matrix_counter) * interval_timeC / matix_max_C
            return StepFunctions.linear_step_func(order_parameter, p1, p2)
        total_time += interval_timeC

        interval_timeD = 25
        matix_max_D = 361
        if 4 <= matrix_counter <= matix_max_D:
            p1 = total_time + (matrix_counter - 1) * interval_timeD / matix_max_D
            p2 = total_time + (matrix_counter) * interval_timeD / matix_max_D
            return StepFunctions.linear_step_func(order_parameter, p1, p2)
        total_time += interval_timeD


class Hendriks_star_array():
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
        self.k_from_real_image(name=name)


    def k_from_real_image(self, name="woman2x.png"):  # init  ## set the input
        path = './pictures/'
        img = Image.open(path + name)  ##open
        img_array = np.asarray(img)  # konv PIL Format in numpy format
        self.pixels = min(img_array.shape)
        img_array = img_array[0:self.pixels, 0:self.pixels]
        ##even make forier transform yet:
        f = np.fft.fft2(img_array)
        fshift = np.fft.fftshift(f)

        ## setup for the whole class
        self.img_k_space = fshift
        self.img_real_in = img_array
        self.img_k_space_original = self.img_k_space.copy()
        self.pixels = len(self.img_k_space)  # important, because init does not do that -.-

    def k_from_real_in_from_star(self):  # init  ## set the input

        img_array = Hendriks_star_array().star
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
    def k_from_preset_minimal(preset_position="LEFT", center_dist=1, amplitude=255):
        pixels=19
        raster_size = (pixels, pixels)
        img_k_space = np.zeros(raster_size, dtype=complex)
        loc = FourierMathJuggling.pixel_position(raster_size, preset_position, center_dist)
        img_k_space[loc] = amplitude
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

    def get_pixels_ZOOMED(self):
        return self.pixels_ZOOMED

    def get_amp_k_only(self):
        return np.abs(self.img_k_space)

    def get_ph_k_only(self):
        return (np.angle(self.img_k_space, deg=True))


    def get_amp_and_ph(self):
        img_kamp = np.abs(self.img_k_space)
        img_kph = (np.angle(self.img_k_space, deg=True))
        return img_kamp, img_kph

    def get_amp_and_ph_DOWNSAMPLED(self,cut_off_the_top=10):
        center = 301
        width = 298
        step = 27
        temp_ar = np.array(self.img_k_space, copy=True)
        self.img_k_space_downsampled = temp_ar[center - width:center + width:step, center - width:center + width:step]
        img_kamp = np.abs(self.img_k_space_downsampled)
        self.max_cutoff = 259482
        img_kamp[11, 11]= img_kamp[11, 11]/100
        img_kamp[img_kamp > self.max_cutoff] = self.max_cutoff
        img_kph = (np.angle(self.img_k_space_downsampled, deg=True))
        self.pixels_DOWNSAMPLED = len(self.img_k_space_downsampled)
        return img_kamp, img_kph

    def get_amp_and_ph_ZOOMED(self, cut_off_the_top=2):
        center = 300
        width = 4
        step = 1
        temp_ar = np.array(self.img_k_space, copy=True)
        self.img_k_space_downsampled = temp_ar[center - width:center + width+step:step, center - width:center + width+step:step]

        img_kamp = np.abs(self.img_k_space_downsampled)
        max_cutoff = self.img_k_space_downsampled[4,4]/cut_off_the_top
        img_kamp[img_kamp>max_cutoff]= max_cutoff
        img_kph = (np.angle(self.img_k_space_downsampled, deg=True))
        self.pixels_ZOOMED = len(self.img_k_space_downsampled)
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
        out = real_out_ar.real
        out[out < 0] = 0
        out[out > 255] = 255

        return out

    @staticmethod
    def Imstretch(a):
        m = a.min();
        M = a.max();
        return np.uint8((256 - 1) / (M - m) * (a - m))

    def get_real_out_strectched(self):
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(self.img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)  ####
        out = real_out_ar.real
        out[out < 0] = 0
        out[out > 255] = 255
        out= self.Imstretch(out)
        return out


    def setup_order(self, order):
        self.order = order

    def make_mask(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
        mask = np.full(raster, (step, 1, 1.2))
        num_of_orders = len(self.order)
        for number, (position_s, center_s) in enumerate(self.order):
            pos = self.pixel_position(raster, position_s, center_s)
            start_p = number / num_of_orders
            end_p = (number + 1) / num_of_orders
            # print(number / num_of_orders, "bis", (number + 1) / num_of_orders, position_s, center_s)
            mask[pos] = StepFunctions.linear_step_func(step, start_p, end_p)
        return mask

    def apply_mask(self, t):
        mask = self.make_mask(t)
        self.img_k_space = self.img_k_space_original * mask

    def apply_spiral_mask(self, t):
        spirale = StepFunctions.spiral(19, 19)
        final_func_vectorised = np.vectorize(StepFunctions.step_machine, otypes=[np.float])
        spiral_mask = final_func_vectorised(spirale, t)
        self.img_k_space = self.img_k_space_original * spiral_mask

    ### gaussian filtering:

    def param_gauss_low_juggling(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
        x, y = np.meshgrid(np.linspace(-1, 1, self.pixels), np.linspace(-1, 1, self.pixels))
        d = np.sqrt(x * x + y * y)
        mu = 0
        sigma = self.sigma
        g_mask = 1 - (1 - np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))) * step
        return g_mask

    def param_gauss_high_juggling(self, step):  # step goes from 0 to 1
        raster = (self.pixels, self.pixels)
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
    pix = (19, 19)
    array = np.ones(pix) * 4
    mama = FourierMathJuggling(array)
    mama.k_from_real_in_from_star()
    mama.apply_spiral_mask(10)
    # mama.apply_transformations(1, sigma=0.2 , mode= "lowpass")
    x = mama.get_amp_k_only()
    plt.rcParams['figure.dpi'] = 100
    plt.figure(figsize=(16, 9))
    sns.heatmap(x, annot=True, fmt=".2f")