

from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.KSpace import KSpace
from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FourierMathJuggling import FourierMathJuggling
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.Realspace import Realspace

global k_plane_size
k_plane_size=0.7


################################IMPORTANT HERE
scene="Scene1_amplitude"  #FULL ANIMATION SCENE amplitude
class Scene1_amplitude(ThreeDScene):  # with real plane on the right
    def perperation_math_and_disp_scene1(self, pixels, num_tracker, phase_tracker= None, pos_ALL=("UP", 1)):
        preset_position = pos_ALL[0]
        center_dist = pos_ALL[1]
        amp= (num_tracker.get_value())
        k_math=FourierMathJuggling.k_from_preset_minimal(
            pixels,preset_position=preset_position,amplitude=amp,center_dist=center_dist)
        if phase_tracker is not None: # in case for phase shifting
            k_math.phase_shift_single(phase_tracker.get_value(),preset_position=preset_position,center_dist=center_dist)

        img_kamp, img_kph = k_math.get_amp_and_ph()
        # make the disply part:
        k_disp = KSpace(pixel_len=pixels)  # setup the k_disp
        k_disp.fill_k_space(img_kamp=img_kamp, dots_lines=True)
        if phase_tracker is not None: # in case for phase shifting
            k_disp.set_phase_flowers(img_kamp=(img_kamp), img_kph=img_kph)

        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels**2*abs(img_real)) ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        return k_disp,real_out

    def construct(self):
        Order= [("LEFT",3),("LEFT",1),("UP",1),("UP",3),("DIAG",2),("UP",0)]
        Order= [("LEFT",3)]
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        #yess
        for o_step in range(0,len(Order)):
            pos_ALL= Order[o_step]
            UP_arrow= SVGMobject("arrow.svg",fill_color= ORANGE).shift(UP*4.5)
            UP_arrow.set_shade_in_3d(True)
            self.add(UP_arrow)
            k_text = TextMobject("K-Space", fill_color=ORANGE).shift(DOWN * 4).scale(2)
            #k_text.set_shade_in_3d(True)
            self.add(k_text)

            pixels = 19
            ##blog 1
            tick_start_amp = 0; tick_end_amp = 255
            val_tracker = ValueTracker(tick_start_amp)
            k_disp,real_out =  self.perperation_math_and_disp_scene1(pixels, num_tracker=val_tracker, pos_ALL=pos_ALL)
            real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out,DOWN)
            self.add_fixed_in_frame_mobjects(real_out,real_text)
            self.add(k_disp)
            ## LET'S MOVE IT!###
            def Compact_updater():
                comp_updater=UpdateFromFunc(
                    VGroup(k_disp, real_out),
                    lambda mob: mob.become(VGroup(
                        *self.perperation_math_and_disp_scene1(pixels, val_tracker, pos_ALL=pos_ALL)
                    ))
                )
                return comp_updater
            self.play(Compact_updater(),val_tracker.set_value, tick_end_amp, rate_func=linear, run_time=1)
            self.wait(2)
            ## blog2
            tick_next_amp = 0
            self.play(
                UpdateFromFunc(
                    VGroup(k_disp, real_out),
                    lambda mob: mob.become(VGroup(
                        *self.perperation_math_and_disp_scene1(pixels, val_tracker, pos_ALL=pos_ALL)
                    ))
                ),
                val_tracker.set_value, tick_next_amp, rate_func=linear, run_time=1
            )




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim    -p -l     -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)