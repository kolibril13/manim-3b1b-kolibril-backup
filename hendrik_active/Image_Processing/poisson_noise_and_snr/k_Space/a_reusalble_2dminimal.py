from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

scene="Image2dTesting"
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
        my_plane.fill_k_space_updater(img_kamp)
        # my_plane.set_phase_flowers_updater(img_kamp+1,img_kph )
        my_plane.move_to(ORIGIN)
        self.add(my_plane)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s  -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)