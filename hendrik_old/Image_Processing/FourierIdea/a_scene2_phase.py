from hendrik_old.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7



scene = "Scene2PhaseCompareLots"  # FULL ANIMATION SCENE phase with real out
class Scene2PhaseCompareLots(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        #Order = [("LEFT", 1), ("LEFT", 7), ("DIAG",-3), ("UP", 0)]
        Order= ["LEFT",1]
        for o_step in range(0, len(Order)):
            self.clear()
            self.add(Image_coordinate_system())
            postion_setting = {"preset_position": Order[o_step][0], "center_dist": Order[o_step][1]}
           # math_preperation:
            k_math = FourierMathJuggling.k_from_preset_minimal(**postion_setting, amplitude=255)
            pixels = k_math.get_pixels()
            print(pixels)
            k_disp = KSpace(pixel_len=19)
            img_kamp, img_kph = k_math.get_amp_and_ph()
            k_disp.amp_max=255
            k_disp.fill_k_space_updater(img_kamp)
            k_disp.set_shade_in_3d(True)
            self.add(k_disp)
            real_out = Realspace(pixel_len=pixels)
            img_real = k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 * img_real)  ## why??? something with norm
            real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
            real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
            self.add_fixed_in_frame_mobjects(real_out, real_text)
            self.wait(1)

            real_out_compare = Realspace(pixel_len=pixels)
            img_real_compare = deepcopy(img_real)
            real_out_compare.fill_real_space(pixels ** 2 * img_real_compare)
            real_out_compare.scale(9 / pixels * k_plane_size * 0.3).next_to(real_text,DOWN)
            self.add_fixed_in_frame_mobjects(real_out_compare)
            self.wait(1)

            # ##HERE STARTS THE LOOP:
            # ####change the phase
            def update_phase(mob):
                val= my_phase_tracker.get_value()
                k_math.phase_shift_single(val, **postion_setting)
                img_kamp, img_kph=k_math.get_amp_and_ph()
                mob.set_phase_flowers_updater (img_kph)
                mob.set_shade_in_3d(True)
                img_real = k_math.get_real_out()
                real_out.fill_real_space(pixels ** 2 * img_real)
                return mob
            my_phase_tracker = ValueTracker(0)
            for i in range(0,4):
                self.play(my_phase_tracker.increment_value, 90,
                          UpdateFromFunc(k_disp, update_phase),
                          rate_func=linear)
                print("ye")
                self.wait(1)
            # self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -l  -p -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)