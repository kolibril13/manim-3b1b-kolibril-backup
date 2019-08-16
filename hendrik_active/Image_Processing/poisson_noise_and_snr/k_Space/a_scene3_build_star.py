from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace,Comp_axis
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7


scene = "Scene3_build_star"  # FULL ANIMATION SCENE phase with real out
class Scene3_build_star(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        k_math = FourierMathJuggling()
        #k_math.k_from_real_in_from_3x3()
        k_math.k_from_real_in_from_star()
        pixels = k_math.get_pixels()
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp,new_amp_max= True,logview=False,
                                    overshoot_factor=20,mushroom_heigth=1) #init wit new_amp_max ture
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)

        compare_Axis = Comp_axis(height=3).set_shade_in_3d()
        compare_Axis.set_opacity(0.1)
        self.add(compare_Axis)

        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space( img_real)
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)

        real_in = Realspace(pixel_len=pixels)
        img_in_real = k_math.get_real_in()
        real_in.fill_real_space(img_in_real)
        real_in.scale(9 / pixels * k_plane_size * 0.3).to_edge(UL)
        real_text_in = TextMobject("Input").scale(0.75).next_to(real_in, DOWN)
        self.add_fixed_in_frame_mobjects(real_in, real_text_in)
#        self.wait(2)

        # ##HERE STARTS THE LOOP:
        # ####change the phase
        def amp_grower(mob):
            val= queenstracker.get_value()
            k_math.apply_transformations(val)
            img_kamp, img_kph =k_math.get_amp_and_ph()
            k_disp.fill_k_space_updater(img_kamp,overshoot_factor =20)
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out()
            real_out.fill_real_space(img_real)
            return mob
        queenstracker = ValueTracker(0)
        end_val=1
        self.play(queenstracker.increment_value, end_val,
                  UpdateFromFunc(k_disp, amp_grower),
                  rate_func=linear,run_time=4 )
        print("ye")
        self.wait(1)
        k_disp.set_phase_
        flowers_updater(img_kph)
        self.wait(1)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)