from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis
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
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        #self.set_camera_orientation(phi=40 * DEGREES, theta=-60 * DEGREES) #TODO NO!
        k_math = FourierMathJuggling()
        FourierMathJuggling.k_from_preset_uniform(7)
        k_math.k_from_real_in_old_woman() # has a 600x600 resolution

        pixels = k_math.get_pixels()
        print("yes",pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph_DOWNSAMPLED(self.down_sample_factor)
        pixels_DOWNSAMPLED = k_math.get_pixels_DOWNSAMPLED()
        k_disp = KSpace(pixel_len=pixels_DOWNSAMPLED)
        k_disp.overshoot_factor=1
        k_disp.log10view=self.log10view
        k_disp.fill_k_space_updater(img_kamp,new_amp_max=True) #init wit new_amp_max ture
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        print("yes",pixels_DOWNSAMPLED)

        compare_Axis = Comp_axis(height=3).set_shade_in_3d()
        compare_Axis.set_opacity(0.1)
        self.add(compare_Axis)

        img_out_real = k_math.get_real_out()
        real_out=ImageMobject(np.uint8(img_out_real)).scale(1.5)
        real_out.to_edge(UR)
        real_text = TextMobject("Real-Space").next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)

        img_in_real = k_math.get_real_in()
        real_in = ImageMobject(np.uint8(img_in_real)).scale(1.5)
        real_in.to_edge(UL)
        real_text_in = TextMobject("Input").next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)


        #HERE STARTS THE LOOP:
        ####change the phase
        def amp_tansformer(mob):
            val= queenstracker.get_value()
            #k_math.apply_transformations(val,sigma=0.05,mode="lowpass")
            #k_disp.set_magic_gauss(val,sigma=0.9, mode="lowpass")
            k_math.apply_transformations(val,sigma=0.9,mode="highpass")
            k_disp.set_magic_gauss(val,sigma=0.9, mode=234)
            img_kamp, img_kph =k_math.get_amp_and_ph_DOWNSAMPLED(self.down_sample_factor)
            k_disp.fill_k_space_updater(img_kamp)
            print("animating")
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out()
            real_out.become(ImageMobject(np.uint8(img_real)).scale(1.5).to_edge(UR))
            return mob
        queenstracker = ValueTracker(0)
        end_val=1
        self.play(queenstracker.increment_value, end_val,
                  UpdateFromFunc(k_disp, amp_tansformer),
                  rate_func=linear,run_time=3)
        print("end")
        self.wait(2)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)