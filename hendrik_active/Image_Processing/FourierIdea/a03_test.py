
from hendrik_active.Image_Processing.FourierIdea.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace, StepFunctions
from manimlib.imports import *
linear_step_func=StepFunctions.linear_step_func
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
        k_disp.amp_max=255

        k_math.phase_shift_single(180,preset_position="LEFT", center_dist=1)
        img_kamp,img_kph= k_math.get_amp_and_ph()
        k_disp.fill_k_space_updater(img_kamp)
        k_disp.set_shade_in_3d(True)
        k_disp.set_phase_flowers_updater(img_kph)
        self.add(k_disp)


        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels ** 2 * img_real)
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out, DOWN)
        self.add_fixed_in_frame_mobjects(real_out, real_text)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l -s -p     -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)