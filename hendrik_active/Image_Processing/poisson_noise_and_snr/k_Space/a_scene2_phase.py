from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7

#scene = "Scene2_phase_no_Real"  # FULL ANIMATION SCENE phase with NO real out
class Scene2_phase_no_Real(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        pixels = 19  # this is how it shoud be
        #pixels=7 # only sh ortly

        # math_preperation:
        global k_math
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels,  amplitude=0)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)

        ###HERE STARTS THE LOOP:
        Order= [("LEFT",2)]
        for o_step in range(0, len(Order)):
            postion_setting = {"preset_position": Order[o_step][0], "center_dist": Order[o_step][1]}

            # lift the amplitude
            def update_ampli(mob):
                global k_math
                k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting,
                                                                   amplitude=my_ampli_tracker.get_value())
                mob.fill_k_space_updater(k_math.get_amp_and_ph()[0])
                return mob

            start_val = 0;end_val = 255
            my_ampli_tracker = ValueTracker(start_val)
            self.play(my_ampli_tracker.increment_value, end_val,
                      UpdateFromFunc(k_disp, update_ampli),
                      rate_func=linear, run_time=2.5)
            print(k_math.get_amp_and_ph()[0])
            #####change the phase
            def update_phase(mob):
                val= my_phase_tracker.get_value()
                k_math.phase_shift_single(val, **postion_setting)
                img_kamp, img_kph=k_math.get_amp_and_ph()
                mob.set_phase_flowers_updater (img_kamp, img_kph)
                mob.set_shade_in_3d(True)
                return mob
            my_phase_tracker = ValueTracker(0)
            for i in range(0,4):
                self.play(my_phase_tracker.increment_value, 90,
                          UpdateFromFunc(k_disp, update_phase),
                          rate_func=linear)
                print("ye")
                self.wait(1)
            self.wait(2)

#scene = "Scene2_phase_Real"  # FULL ANIMATION SCENE phase with real out
class Scene2_phase_Real(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        pixels = 19  # this is how it shoud be
         #pixels=7 # only sh ortly

        # math_preperation:
        global k_math
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, "LEFT",2, amplitude=255)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels ** 2 * img_real)  ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        self.wait(2)



        ###HERE STARTS THE LOOP:
        #####change the phase
        # postion_setting = {"preset_position": "LEFT", "center_dist":2}
        # def update_phase(mob):
        #     val= my_phase_tracker.get_value()
        #     k_math.phase_shift_single(val, **postion_setting)
        #     img_kamp, img_kph=k_math.get_amp_and_ph()
        #     mob.set_phase_flowers_updater (img_kamp, img_kph)
        #     mob.set_shade_in_3d(True)
        #     img_real = k_math.get_real_out()
        #     real_out.fill_real_space(pixels ** 2 * img_real)
        #     return mob
        # my_phase_tracker = ValueTracker(0)
        # for i in range(0,4):
        #     self.play(my_phase_tracker.increment_value, 90,
        #               UpdateFromFunc(k_disp, update_phase),
        #               rate_func=linear)
        #     print("ye")
        #     self.wait(1)
        # self.wait(2)


# scene = "Scene2_phase_compare"  # FULL ANIMATION SCENE phase with real out
class Scene2_phase_compare(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        pixels = 19  # this is how it shoud be
         #pixels=7 # only sh ortly

        # math_preperation:
        global k_math
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, "LEFT",2, amplitude=255)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels ** 2 * img_real)  ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        self.wait(2)

        real_out_compare = Realspace(pixel_len=pixels)
        img_real_compare = deepcopy(img_real)
        real_out_compare.fill_real_space(pixels ** 2 * img_real_compare)
        real_out_compare.scale(9 / pixels * k_plane_size * 0.3).next_to(real_text,DOWN)
        self.add_fixed_in_frame_mobjects(real_out_compare)
        self.wait(2)

        ##HERE STARTS THE LOOP:
        ####change the phase
        postion_setting = {"preset_position": "LEFT", "center_dist":2}
        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.phase_shift_single(val, **postion_setting)
            img_kamp, img_kph=k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater (img_kamp, img_kph)
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
        self.wait(2)

scene = "Scene2_phase_compare_higher"  # FULL ANIMATION SCENE phase with real out #NOT YYET
class Scene2_phase_compare_higher(ThreeDScene):  # with real plane on the right
    def construct(self):
        postion_setting = {"preset_position": "LEFT", "center_dist": 7}
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        pixels = 19  # this is how it shoud be
         #pixels=7 # only sh ortly

        # math_preperation:
        global k_math
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels,**postion_setting, amplitude=255)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        k_disp.set_shade_in_3d(True)
        self.add(k_disp)
        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels ** 2 * img_real)  ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        self.wait(2)

        real_out_compare = Realspace(pixel_len=pixels)
        img_real_compare = deepcopy(img_real)
        real_out_compare.fill_real_space(pixels ** 2 * img_real_compare)
        real_out_compare.scale(9 / pixels * k_plane_size * 0.3).next_to(real_text,DOWN)
        self.add_fixed_in_frame_mobjects(real_out_compare)
        self.wait(2)

        ##HERE STARTS THE LOOP:
        ####change the phase
        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.phase_shift_single(val, **postion_setting)
            img_kamp, img_kph=k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater (img_kamp, img_kph)
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
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim     -p -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)