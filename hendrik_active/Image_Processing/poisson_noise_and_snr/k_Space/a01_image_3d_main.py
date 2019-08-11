from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.ImProImports import \
    FourierMathJuggling,Image_coordinate_system, KSpace, Realspace
from manimlib.imports import *

global k_plane_size
k_plane_size=0.7



############ ANIMATION START


#scene="Minimal_save"  #newest and best version with only k_space
class Minimal(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        pixels = 30

        # make the math:
        k_math=FourierMathJuggling.k_from_preset_minimal(pixels,preset_position="DIAG")
        img_kamp, img_kph = k_math.get_amp_and_ph()

        # make the disply part:
        k_disp = KSpace(pixel_len=pixels)  # setup the k_disp
        k_disp.fill_k_space_updater(img_kamp=img_kamp)
        # k_disp.set_phase_flowers(img_kamp=(img_kamp), img_kph=img_kph)

        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(1000*abs(img_real)) ## why???
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)

        self.add(k_disp)
        self.add_fixed_in_frame_mobjects(real_out)

#scene="Scene0_setup"  #FULL ANIMATION SCENE amplitude
class Scene0_setup(ThreeDScene):  # with real plane on the right
    def MAKE_MATH_AND_DISP(self, pixels, num_tracker, phase_tracker= None,pos_ALL=("UP",1) ):
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
        k_disp.fill_k_space_updater(img_kamp=img_kamp, dots_lines=False)
        if phase_tracker is not None: # in case for phase shifting
            k_disp.set_phase_flowers(img_kamp=(img_kamp), img_kph=img_kph)

        real_out = Realspace(pixel_len=pixels)
        img_real = k_math.get_real_out()
        real_out.fill_real_space(pixels**2*abs(img_real)) ## why??? something with norm
        real_out.scale(9 / pixels * k_plane_size * 0.3).to_edge(UR)
        return k_disp,real_out

    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        #yess
        UP_arrow= SVGMobject("arrow.svg",fill_color= ORANGE).shift(UP*4.5)
        UP_arrow.set_shade_in_3d(True)
        k_text = TextMobject("K-Space", fill_color=ORANGE).shift(DOWN * 4).scale(2)
        #k_text.set_shade_in_3d(True)
        pixels = 19
        ##blog 1
        tick_start_amp = 0; tick_end_amp = 255
        val_tracker = ValueTracker(tick_start_amp)
        k_disp,real_out =  self.MAKE_MATH_AND_DISP(pixels, num_tracker=val_tracker)
        real_text = TextMobject("Real-Space").scale(0.75).next_to(real_out,DOWN)
        self.play(Write(k_disp),FadeIn(k_text) ,run_time=5)
        self.play(FadeIn(UP_arrow))
        self.wait()
        self.add_fixed_in_frame_mobjects(real_out,real_text)
        self.wait(3)

        ## LET'S MOVE IT!###



#scene="Fourier_In_k_Out"  #newest and best version with image+ fourier+ new image
class Fourier_In_k_Out(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        pixels=30

        #make the math:
        #k_math=FourierMathJuggling.k_from_preset_minimal(pixels,preset_position="DIAG")
        k_math=FourierMathJuggling(1)
        k_math.k_from_real_in()
        img_real_in = k_math.get_real_in()
        img_kamp, img_kph = k_math.get_amp_and_ph()
        if img_real_in is not None:
            img_kamp = 20*np.log2(img_kamp)
        # make the disply part:
        k_disp = KSpace(pixel_len=pixels)   # setup the k_disp
        k_disp.fill_k_space_updater(img_kamp=(img_kamp))
        #k_disp.set_phase_flowers(img_kamp=(img_kamp), img_kph=img_kph)

        real_in = Realspace(pixel_len=pixels)
        if img_real_in is not None:
            real_in.fill_real_space(img_real_in)
            real_in.scale(9 / pixels * k_plane_size * 0.3).to_edge(UL)
            self.add_fixed_in_frame_mobjects(real_in)

        real_out=Realspace(pixel_len=pixels)
        img_real= k_math.get_real_out()

        real_out.fill_real_space(img_real)
        real_out.scale(9 / pixels * k_plane_size *0.3 ).to_edge(UR)

        self.add(k_disp)
        self.add_fixed_in_frame_mobjects(real_out)

class MovingScene(ThreeDScene):
    pass
# still great value!
class FilterkScene(ThreeDScene): #TODO : make updated!
    def construct(self):
        # axes:
        pixels = 9
        # img= np.uint8(np.random.randint(1, 255, (pixels,pixels)))
        img = np.uint8(np.fromfunction(lambda i, j: 255 / 2 * (np.sin(i) + 1), (pixels, pixels), dtype=int))
        # img = np.uint8([[i+j for i in range(0,pixels)]for j in range(0,pixels)])
        mg = np.uint8(np.fromfunction(lambda i, j: 255 + i * 0, (pixels, pixels), dtype=int))
        # img = np.uint8(np.fromfunction(lambda u, v: (np.sin(u) + np.cos(v)), (pixels, pixels)))
        fourier = np.fft.fft2(img)
        fourier_s = np.fft.fftshift(fourier)
        fourier_s = np.uint8(abs(fourier_s))


        # breakpoint()
        # # camera settings
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        # self.set_camera_orientation(phi=0 * DEGREES, theta=-45 * DEGREES) #TOP
        # self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES) #side
        self.camera.frame_center.shift(2 * OUT)
        self.begin_ambient_camera_rotation(rate=0.1)  # Start move camera

        # make the realspace
        UPFACTOR = 0.5
        r = Realspace(pixel_len=pixels)
        r.fill_real_space(img_real=img)
        r.scale(9 / pixels * k_plane_size * UPFACTOR).to_edge(UL)
        self.add_fixed_in_frame_mobjects(r)

        my_plane = KSpace(pixel_len=pixels)

        # middle the plane
        my_plane.set_x(0) ##not needed anymore
        my_plane.set_y(0)
        my_plane.set_z(0)
        my_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        my_plane.fill_k_space_updater(img_kamp=fourier_s)
        #my_plane.set_phase_flowers(fourier_s, fourier_s)
        my_plane.set_shade_in_3d(True)
        # self.play(TransformFromCopy(r,my_plane))
        self.add(my_plane)
        self.wait()
        magic_plane = my_plane.set__magic_plane()
        magic_gauss=my_plane.set_magic_gauss()
        #first part
        self.play(Write(magic_plane), run_time=1)
        # #make the filtering:
        img2=np.uint8(img*(1-my_plane.gauss_array_2d()))
        self.wait(10)
        my_plane2= KSpace(pixel_len=pixels)
        my_plane2.set_x(0) #not needed anymore
        my_plane2.set_y(0)
        my_plane2.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        my_plane2.fill_k_space_updater(img_kamp=img2)
        self.play(Transform(magic_plane,magic_gauss),
                   Transform(my_plane,my_plane2),run_time=1)
        # # self.wait(10)

class spare_things(ThreeDScene): ### often used camera positions, etc.
    def construct(self):
        pass
        ##idea with compact updater:

        def Compact_updater():
            comp_updater = UpdateFromFunc(
                VGroup(k_disp, real_out),
                lambda mob: mob.become(VGroup(
                    *self.perperation_math_and_disp_scene1(pixels, val_tracker, pos_ALL=pos_ALL)
                ))
            )
            return comp_updater

        self.play(Compact_updater(), val_tracker.set_value, tick_end_amp, rate_func=linear, run_time=1)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim    -p -l     -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)