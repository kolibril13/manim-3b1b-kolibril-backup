from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.KSpace import KSpace
from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FourierMathJuggling import FourierMathJuggling
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.Realspace import Realspace

class Image_coordinate_system(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        UP_arrow = SVGMobject("arrow.svg", fill_color=ORANGE).shift(UP * 4.5)
        UP_arrow.set_shade_in_3d(True)
        k_text = TextMobject("K-Space", fill_color=ORANGE).shift(DOWN * 4).scale(2)
        # k_text.set_shade_in_3d(True)
        self.add(k_text)
        self.add(UP_arrow)

global k_plane_size
k_plane_size=0.7

scene = "lift_ampl"  # FULL ANIMATION SCENE phase with real out
class lift_ampl(ThreeDScene):  # with real plane on the right

    def construct(self):
        Order= [("LEFT",3),("LEFT",1)]
        postion_setting={"preset_position":"LEFT","center_dist": 1}

        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        # pixels = 19 #this is how it shoud be
        pixels=7 # only shortly
        #math_preperation:
        k_math=FourierMathJuggling.k_from_preset_minimal(pixels,**postion_setting,amplitude=0)
        k_disp= KSpace(pixel_len=pixels)
        img_kamp,img_kph= k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        self.add(k_disp)

        #lift the amplitude
        def update_ampli(mob):
            k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting,amplitude=my_ampli_tracker.get_value())
            mob.fill_k_space(k_math.get_amp_and_ph()[0])
            return mob
        start_val=0;end_val=255
        my_ampli_tracker = ValueTracker(start_val)
        self.play(my_ampli_tracker.increment_value, end_val,
                  UpdateFromFunc(k_disp, update_ampli),
             rate_func=linear)
        self.wait()


#scene = "Scene2_with_phase_change"  # FULL ANIMATION SCENE phase but no real_out
class Scene2_with_phase_change(ThreeDScene):  # with real plane on the right

    def construct(self):
        run_setting = {"run_time": 1  , "rate_func": linear}
        # GENERAL:
        postion_setting={"preset_position":"LEFT","center_dist": 1}
        UP_arrow= SVGMobject("arrow.svg",fill_color= ORANGE).shift(UP*4.5)
        UP_arrow.set_shade_in_3d(True)
        self.add(UP_arrow)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        #pixels = 19 #this is how it shoud be
        pixels=7 # only shortly
        #math_preperation:
        k_math=FourierMathJuggling.k_from_preset_minimal(pixels,**postion_setting)
        k_disp= KSpace(pixel_len=pixels)
        img_kamp,img_kph= k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        self.add(k_disp)
        # my_ampli_tracker = ValueTracker(0)
        # def update_ampli(mob):
        #     # mob.shift(my_ampli_tracker.get_value() *UP)
        #     k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting,amplitude=my_ampli_tracker.get_value())
        #     mob.fill_k_space(k_math.get_amp_and_ph()[0])
        #     return mob
        # end_val=255
        # self.play(my_ampli_tracker.increment_value, end_val,  # <- "Master" update first
        #          UpdateFromFunc(k_disp, update_ampli),
        #     rate_func=linear)
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        k_disp.set_phase_flowers((img_kamp * 10 / 360), img_kph)
        self.add(k_disp)

        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.phase_shift_single(val, **postion_setting)
            img_kamp, img_kph=k_math.get_amp_and_ph()
            mob.set_phase_flowers_updater (img_kamp, img_kph)
            mob.set_shade_in_3d(True)
            return mob
        my_phase_tracker = ValueTracker(0)
        for i in range(0,1):
            self.play(my_phase_tracker.increment_value, 90,  # <- "Master" update first
                      UpdateFromFunc(k_disp, update_phase),
                      rate_func=linear)
            self.wait(1)

#scene = "Scene2_with_phase_change_with_real_out"  # FULL ANIMATION SCENE phase with real out
class Scene2_with_phase_change_with_real_out(ThreeDScene):  # with real plane on the right

    def construct(self):
        run_setting = {"run_time": 1  , "rate_func": linear}
        # GENERAL:
        postion_setting={"preset_position":"LEFT","center_dist": 1}
        UP_arrow= SVGMobject("arrow.svg",fill_color= ORANGE).shift(UP*4.5)
        UP_arrow.set_shade_in_3d(True)
        self.add(UP_arrow)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        pixels = 19 #this is how it shoud be
        #pixels=7 # only shortly
        #math_preperation:
        k_math=FourierMathJuggling.k_from_preset_minimal(pixels,**postion_setting)
        k_disp= KSpace(pixel_len=pixels)
        img_kamp,img_kph= k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        self.add(k_disp)

        #lift the amplitude
        my_ampli_tracker = ValueTracker(0)
        def update_ampli(mob):
            k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting,amplitude=my_ampli_tracker.get_value())
            mob.fill_k_space(k_math.get_amp_and_ph()[0])
            return mob
        end_val=255
        self.play(my_ampli_tracker.increment_value, end_val,  # <- "Master" update first
                 UpdateFromFunc(k_disp, update_ampli),
            rate_func=linear)

        #change the phase
        k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting)
        k_disp = KSpace(pixel_len=pixels)
        img_kamp, img_kph = k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        k_disp.set_phase_flowers((img_kamp * 10 / 360), img_kph)
        self.add(k_disp)
        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels ** 2 * img_real)  ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)
        def update_phase(mob):
            val= my_phase_tracker.get_value()
            k_math.phase_shift_single(val, **postion_setting)
            img_kamp, img_kph=k_math.get_amp_and_ph()
            img_real = k_math.get_real_out()
            real_out.fill_real_space(pixels ** 2 *img_real)
            mob.set_phase_flowers_updater (img_kamp, img_kph)
            mob.set_shade_in_3d(True)
            return mob

        my_phase_tracker = ValueTracker(0)
        for i in range(0,1):
            self.play(my_phase_tracker.increment_value, 90,  # <- "Master" update first
                      UpdateFromFunc(k_disp, update_phase),
                      rate_func=linear)
            self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim        -l  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)