from hendrik_active.Image_Processing.FourierIdea.ImProImports import *
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7



# scene = "Scene2PhaseMore"  # FULL ANIMATION SCENE phase with real out
class Scene2PhaseMore(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.clear()
        self.add(Image_coordinate_system())
        postion_setting = {"preset_position": "LEFT", "center_dist": 2}
       # math_preperation:
        k_math = FourierMathJuggling.k_from_preset_minimal(**postion_setting, amplitude=0)
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

        def update_ampli(mob):
            val=track.get_value()
            print(val)
            k_math.img_k_space[11,9]=  255*StepFunctions.linear_step_func(track.get_value(),0,1)
            k_math.img_k_space[9,11] = 255*StepFunctions.linear_step_func(track.get_value(),1,2)
            if val >= 2:
                k_math.img_k_space[11, 9] = 255 * (1-0.5*linear_step_func(track.get_value(), 2, 3))
            if val >= 3:
                k_math.img_k_space[9, 11] = 255 * (1-0.3*linear_step_func(track.get_value(), 3, 4))
            mob.fill_k_space_updater(k_math.get_amp_k_only())
            img_real= k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 * img_real)
            return mob
        start_val=0
        track = ValueTracker(start_val)
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=1)
        self.wait()
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=2)
        self.wait(2)
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=1.5)
        self.wait()
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=1.5)
        self.wait(2)
        # # ##HERE STARTS THE LOOP:
        # ####change the phase
        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.img_k_space[9, 11]=255*(0.7*np.exp(1j * np.deg2rad(val)))
            img_kamp, img_kph=k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater (img_kph)
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 * img_real)
            return mob
        my_phase_tracker = ValueTracker(0)
        for _ in range(0,4):
            self.play(my_phase_tracker.increment_value, 90,
                      UpdateFromFunc(k_disp, update_phase),
                      rate_func=linear)
            self.wait(0.2)
        self.wait()
        def update_phase2(mob):
            val = my_phase_tracker.get_value()
            k_math.img_k_space[11, 9] = 255 * (0.5 * np.exp(1j * np.deg2rad(val)))
            img_kamp, img_kph = k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater(img_kph)
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 * img_real)
            return mob

        my_phase_tracker = ValueTracker(0)
        for _ in range(0, 4):
            self.play(my_phase_tracker.increment_value, 90,
                      UpdateFromFunc(k_disp, update_phase2),
                      rate_func=linear)
            self.wait(0.2)

scene = "Scene2PhaseMoreExtend"  # FULL ANIMATION SCENE phase with real out
class Scene2PhaseMoreExtend(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.clear()
        self.add(Image_coordinate_system())
        postion_setting = {"preset_position": "LEFT", "center_dist": 2}
       # math_preperation:
        k_math = FourierMathJuggling.k_from_preset_minimal(**postion_setting, amplitude=0)
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

        def update_ampli(mob):
            val=track.get_value()
            print(val)
            k_math.img_k_space[5,9]=  255/3*StepFunctions.linear_step_func(track.get_value(),0,0.3)
            k_math.img_k_space[11,9]=  255*StepFunctions.linear_step_func(track.get_value(),0.7,1)
            k_math.img_k_space[12,12] = 255*StepFunctions.linear_step_func(track.get_value(),1,2)
            if val >= 2:
                k_math.img_k_space[11, 9] = 255 * (1-0.5*linear_step_func(track.get_value(), 2, 3))
            if val >= 3:
                k_math.img_k_space[12, 12] = 255 * (1-0.3*linear_step_func(track.get_value(), 3, 4))
            mob.fill_k_space_updater(k_math.get_amp_k_only())
            img_real= k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 * img_real)
            return mob
        start_val=0
        track = ValueTracker(start_val)
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=4)
        self.wait()
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=2)
        self.wait(2)
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=1.5)
        self.wait()
        self.play(track.increment_value, 1,UpdateFromFunc(k_disp, update_ampli),rate_func=linear,run_time=1.5)
        self.wait(2)
        # # ##HERE STARTS THE LOOP:
        # ####change the phase
        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.img_k_space[12, 12]=255*(0.7*np.exp(1j * np.deg2rad(val)))
            img_kamp, img_kph=k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater (img_kph)
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 * img_real)
            return mob
        my_phase_tracker = ValueTracker(0)
        for _ in range(0,4):
            self.play(my_phase_tracker.increment_value, 90,
                      UpdateFromFunc(k_disp, update_phase),
                      rate_func=linear)
            self.wait(0.2)
        self.wait()
        def update_phase2(mob):
            val = my_phase_tracker.get_value()
            k_math.img_k_space[11, 9] = 255 * (0.5 * np.exp(1j * np.deg2rad(val)))
            img_kamp, img_kph = k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater(img_kph)
            mob.set_shade_in_3d(True)
            img_real = k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 * img_real)
            return mob

        my_phase_tracker = ValueTracker(0)
        for _ in range(0, 4):
            self.play(my_phase_tracker.increment_value, 90,
                      UpdateFromFunc(k_disp, update_phase2),
                      rate_func=linear)
            self.wait(0.2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim    -p  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)