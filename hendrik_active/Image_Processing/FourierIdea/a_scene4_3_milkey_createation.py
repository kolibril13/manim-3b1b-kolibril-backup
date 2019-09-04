from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7

scene = "Scene5RealImageMilkey"
class Scene5RealImageMilkey(ThreeDScene):
    def construct(self):
        self.add(Image_coordinate_system(zoomed=True))
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        k_math = FourierMathJuggling()
        k_math.k_from_real_image("milkeyway.png") # has a 601x601 resolution
        pos = (296, 300)
        k2= np.ones((601,601))
        k2[pos]= 255*601 ** 2 / 5
        k_math_2 = FourierMathJuggling(k2)

        # val0 = k_math.img_k_space[pos]
        # k_math.img_k_space[pos] = val0*30
        pixels = k_math_2.get_pixels()

        # img_in_real2 = k_math_2.get_real_out()
        img_in_real2=np.fromfunction(lambda i, j: 60*np.sin(i/601), (601, 601))

        real_in = ImageMobject(np.uint8(img_in_real2)).scale(1.5)
        real_in.to_edge(UL)
        real_text_in = TextMobject("Input").next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)
        img_kamp, img_kph = k_math.get_amp_and_ph_ZOOMED() # here we have a cut_off_the_top, e.g. 2
        pixels_ZOOMED = k_math.get_pixels_ZOOMED()
        k_disp = KSpace(pixel_len=pixels_ZOOMED)
        k_disp.overshoot_factor=1.8
        k_disp.fill_k_space_updater(img_kamp, new_amp_max=True)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)

        img_out_real = k_math.get_real_out()
        insg=img_out_real+img_in_real2
        insg[insg<0]=0
        insg[insg>255]=255
        insg=np.uint8(insg)
        real_out=ImageMobject(np.uint8(insg)).scale(1.5)
        real_out.to_edge(UR)
        real_text = TextMobject("Real-Space").next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        from PIL import Image
        result = Image.fromarray((insg).astype(np.uint8))
        result.save('out.png')


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -s  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)