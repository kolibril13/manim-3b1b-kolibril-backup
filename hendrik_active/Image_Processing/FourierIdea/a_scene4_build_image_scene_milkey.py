from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7


scene = "RealImageBuild"
class RealImageBuild(ThreeDScene):  # with real plane on the right
    CONFIG={
        "down_sample_factor":24, # cool! take every 24th pixel
        # "down_sample_factor": 50,
        "log10view":True
    }
    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        #self.set_camera_orientation(phi=40 * DEGREES, theta=-60 * DEGREES) #TODO NO!
        k_math = FourierMathJuggling()
        FourierMathJuggling.k_from_preset_uniform(7)
        #k_math.k_from_real_in_old_woman() # has a 601x601 resolution
        k_math.k_from_real_image("milkeyway.png")
        pixels = k_math.get_pixels()
        print("yes",pixels)


        img_in_real = k_math.get_real_in()
        real_in = ImageMobject(np.uint8(img_in_real)).scale(1.5)
        real_in.to_edge(UL)
        real_text_in = TextMobject("Input").next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)

        k_math.img_k_space[300+27*1,300]= 259482*50
        img_kamp, img_kph = k_math.get_amp_and_ph_DOWNSAMPLED(mute_peak_fac=170)
        pixels_DOWNSAMPLED = k_math.get_pixels_DOWNSAMPLED()
        k_disp = KSpace(pixel_len=pixels_DOWNSAMPLED)
        k_disp.overshoot_factor=1.8
        # k_disp.amp_max= 259482
        # k_disp.fill_k_space_updater(img_kamp) #init wit new_amp_max ture
        # print(k_disp.amp_max)

        k_disp.fill_k_space_updater(img_kamp, new_amp_max=True)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        print("yes",pixels_DOWNSAMPLED)


        img_out_real = k_math.get_real_out()
        img_out_real[img_out_real<0]=0
        img_out_real[img_out_real>255]=255

        real_out=ImageMobject(np.uint8(img_out_real)).scale(1.5)
        real_out.to_edge(UR)
        real_text = TextMobject("Real-Space").next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)





if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -s -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)