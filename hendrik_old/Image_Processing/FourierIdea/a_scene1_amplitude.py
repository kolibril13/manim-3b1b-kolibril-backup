
from hendrik_old.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7


################################IMPORTANT HERE
scene = "Scene01DifferentAmplitudes"  # FULL ANIMATION SCENE phase with real out
class Scene01_different_amplitudes(ThreeDScene):  # with real plane on the right

    def construct(self):
        self.add(Image_coordinate_system())
        self.camera.frame_center.shift(2 * OUT)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D

        #math_preperation:
        k_math=FourierMathJuggling.k_from_preset_minimal(amplitude=255)
        pixels= k_math.get_pixels()
        k_disp= KSpace(pixel_len=pixels)

        img_kamp,img_kph= k_math.get_amp_and_ph()
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

        ##HERE STARTS THE LOOP:
        Order= [("LEFT",3),("LEFT",1),("UP",1),("UP",3),("DIAG",2),("UP",0)]
        Order= [("LEFT",1),("LEFT",3),("UP",3),("UP",1),("UP",-1),("DIAG",2),("DIAG",1),("UP",0)]
        Order= [("LEFT",1),("UP",0)]
        # Order= [("LEFT",3),("LEFT",1),("DIAG",2)]
        for o_step in range(0, len(Order)):
            postion_setting = {"preset_position":Order[o_step][0] ,"center_dist": Order[o_step][1]}
            #lift the amplitude
            def update_ampli(mob):
                k_math = FourierMathJuggling.k_from_preset_minimal(**postion_setting,amplitude=my_ampli_tracker.get_value())
                mob.fill_k_space_updater(k_math.get_amp_k_only())
                img_real= k_math.get_real_out()
                real_out.fill_real_space(pixels ** 2 * img_real)
                return mob
            start_val=0;end_val=255
            my_ampli_tracker = ValueTracker(start_val)
            self.play(my_ampli_tracker.increment_value, end_val,
                      UpdateFromFunc(k_disp, update_ampli),
                 rate_func=linear,run_time=2.5)
            self.wait(2)
            start_val=255;end_val=0
            my_ampli_tracker = ValueTracker(start_val)
            self.play(my_ampli_tracker.set_value , end_val,
                      UpdateFromFunc(k_disp, update_ampli),
                      rate_func=linear, run_time=1.5 )
            self.wait(0.3)
        self.wait(2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s   -p     -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)