from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FLOWER import FLOWER
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FourierMathJuggling import FourierMathJuggling
from functools import partial

global k_plane_size
k_plane_size=0.7


#display options

class K_Space(VMobject):
    CONFIG = {
        "pixel_len":23,
        "mushroom_heigt":1.1,
        "magic_offset_z":k_plane_size

    }
    def __init__(self , **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
        self.term= VGroup()
        self.flows = VGroup()  ## these will be deleted and filled in subfunctions
        self.lines_and_dots=VGroup() ## these will be deleted and filled in subfunctions
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.move_to((LEFT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.term.set_x(0)
        self.term.set_y(0)
        self.term.set_z(0.01)  ## why again?
        self.term.scale_about_point(9 / self.pixel_len * k_plane_size, ORIGIN)
        self.term.set_shade_in_3d(True)
        self.add(self.term) ## better return term???

    def fill_k_space(self, img_kamp, dots_lines=True): #empty it first, then refill
        self.remove(self.lines_and_dots)
        t_objects = [t for t in self.term.submobjects]
        img_kamp = img_kamp.flatten()
        # create dots array
        self.dots = VGroup()
        self.lines = VGroup()
        for i, el in enumerate(t_objects):
            # interpol_col
            wanted_color = interpolate_color(BLACK, WHITE, img_kamp[i] / 255)
            el.set_color(wanted_color)

            if dots_lines == True:
                wanted_height = img_kamp[i] / 255 * self.mushroom_heigt

                # set height
                dot = Dot()
                dot.move_to(el.get_center())
                dot.set_z(wanted_height)
                # set color
                dot.set_color(wanted_color)

                # make line
                line = Line(dot.get_center(),
                            [dot.get_x(), dot.get_y(), 0],
                            color=wanted_color)
                # append the pixels
                self.dots.add(dot)
                self.lines.add(line)

        if dots_lines == True:
            self.lines_and_dots=VGroup(self.dots,self.lines).set_shade_in_3d(True)
            self.add(self.lines_and_dots)
        #lastly the middle point
        ORI_POINT = Dot(fill_color=ORANGE).shift(OUT * 0.01).scale(1.5)
        ORI_POINT.set_shade_in_3d(True)
        self.add(ORI_POINT)

    def clear_k_space(self):
        self.remove(self.lines_and_dots)

    def set_phase_flowers(self, img_kamp, img_kph):
        self.remove(self.flows)
        self.flows = VGroup()
        t_objects = [t for t in self.term.submobjects]
        img_kamp = img_kamp.flatten()
        img_kph = img_kph.flatten()
        # create dots array
        for i, el in enumerate(t_objects):
            if img_kph[i] is not 0: # do not call FLOWER when phase is even 0
                wanted_heightx = img_kamp[i] / 255 * self.mushroom_heigt
                # set height
                # dot = FLOWER(img_kph[i]).scale(0.21)
                dot = FLOWER(img_kph[i]).scale(0.51) # for special cases
                dot.move_to(el.get_center()+OUT*wanted_heightx)
                # append the pixels
                self.flows.add(dot)
        self.add(self.flows)
    def clear_phase_flowers(self):
        self.remove(self.flows)
    def set_subobject_opacity(self, img_array,offset):
        x, y = np.meshgrid(np.linspace(-1, 1, self.pixel_len), np.linspace(-1, 1, self.pixel_len))
        d = np.sqrt(x * x + y * y)
        sigma, mu = 1, 0.0
        g = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
        img_array = img_array.flatten()
        g=g.flatten()
        for i, (el,dot,line) in enumerate(zip(self.term, self.dots, self.lines)):

            # wanted_opacity = img_array[i] / 255 * g[i]
            wanted_opacity = g[i]
            # set opacity
            el.set_opacity(1)
            dot.set_opacity(wanted_opacity)
            line.set_opacity(wanted_opacity)

    def set__magic_plane(self):
        def param_plane(u, v):
            x = u
            y = v
            z = self.mushroom_heigt + self.magic_offset_z
            return np.array([x, y, z])
        magic_plane = ParametricSurface((param_plane), resolution=(self.pixel_len, self.pixel_len),
                                        v_min=self.get_corner(UL)[0],
                                        v_max=self.get_corner(UL)[1],
                                        u_min=self.get_corner(UL)[0],
                                        u_max=self.get_corner(UL)[1])
        magic_plane.set_style(stroke_color=BLUE_A)
        magic_plane.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.1)
        return magic_plane

    def set_magic_gauss(self,**kwargs):
        resolution_fa = self.pixel_len
        def param_gauss(u,v):
            x=u
            y=v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 1, 0.0
            z= (1-np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2))))*self.mushroom_heigt+self.magic_offset_z
            return np.array([x,y,z])



        magic_gauss= ParametricSurface((param_gauss),resolution=(resolution_fa, resolution_fa),
                                  v_min=self.get_corner(UL)[0],
                                  v_max=self.get_corner(UL)[1],
                                  u_min=self.get_corner(UL)[0],
                                  u_max=self.get_corner(UL)[1])
        magic_gauss.set_style(stroke_color=BLUE_A)
        magic_gauss.set_fill_by_checkerboard(GREEN,BLUE,opacity=0.1)
        return magic_gauss

    def gauss_array_2d(self,sigma=1 , mu=0):
        x, y = np.meshgrid(np.linspace(-1, 1, self.pixel_len), np.linspace(-1, 1, self.pixel_len))
        d = np.sqrt(x * x + y * y)
        g = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
        return g

class Realspace(VMobject):
    CONFIG = {
        "mushroom_heigt": 1.1,
        "magic_offset_z": k_plane_size
    }

    def __init__(self, pixel_len,**kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
        self.term = VGroup()
        self.pixel_len=pixel_len
        PIXELS = pixel_len * pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1 , stroke_width=0) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.move_to((LEFT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.add(self.term)

    def fill_real_space(self, img_real):
        t_objects = [t for t in self.term.submobjects]
        img_real = img_real.flatten()
        #interpolate the colors from array
        for i, el in enumerate(t_objects):
            el.set_color(interpolate_color(BLACK, WHITE, img_real[i] / 255)) #change!!

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
        k_disp = K_Space(pixel_len=pixels)  # setup the k_disp
        k_disp.fill_k_space(img_kamp=img_kamp, dots_lines=True)
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
        k_disp = K_Space(pixel_len=pixels)  # setup the k_disp
        k_disp.fill_k_space(img_kamp=img_kamp, dots_lines=False)
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

################################IMPORTANT HERE
#scene="Scene1_amplitude"  #FULL ANIMATION SCENE amplitude
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
        k_disp = K_Space(pixel_len=pixels)  # setup the k_disp
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

#scene="Scene2_with_phase_change_crap"  #FULL ANIMATION SCENE phase but no real_out
class Scene2_with_phase_change_crap(ThreeDScene):  # with real plane on the right
    def perperation_math_and_disp_scene2(self, pixels, num_tracker, phase_tracker= None, preset_position="UP"):
        amp= (num_tracker.get_value())
        k_math=FourierMathJuggling.k_from_preset_minimal(pixels,preset_position=preset_position,amplitude=amp)
        if phase_tracker is not None: # in case for phase shifting
            k_math.phase_shift_single(phase_tracker.get_value(),preset_position=preset_position)

        img_kamp, img_kph = k_math.get_amp_and_ph()
        # make the display part:
        k_disp = K_Space(pixel_len=pixels)  # setup the k_disp
        k_disp.fill_k_space(img_kamp=img_kamp, dots_lines=True)
        if phase_tracker is not None: # in case for phase shifting
            k_disp.set_phase_flowers(img_kamp=(img_kamp), img_kph=img_kph)
        return k_disp, k_math

    def construct(self):
        UP_arrow= SVGMobject("arrow.svg",fill_color= ORANGE).shift(UP*4.5)
        UP_arrow.set_shade_in_3d(True)
        self.add(UP_arrow)
        #self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        pixels = 19

        ##blog 1
        tick_start_amp = 0; tick_end_amp = 255
        val_tracker = ValueTracker(tick_start_amp)
        k_disp =  self.perperation_math_and_disp_scene2(pixels, num_tracker=val_tracker, preset_position="UP")
        self.add(k_disp)
        ## LET'S MOVE IT!###
        self.play(  #lift the amplitude up
            UpdateFromFunc(
                VGroup(k_disp),
                lambda mob: mob.become(VGroup(
                    self.perperation_math_and_disp_scene2(pixels, val_tracker, preset_position="UP")
                ))
            ),
            val_tracker.set_value, tick_end_amp, rate_func=linear, run_time=1
        )
        self.wait()
        #four times the phase moulation
        # for i in [0,90,180,270]:
        print("yesss")
        ii=0
        tick_start_ph=0+ii; tick_end_ph=90+ii
        phase_tracker= ValueTracker(tick_start_ph)
        ## blog2 #start the phase modulation
        def small_change(k,number):
            print(number)
            k_math.phase_shift_single
            k.phase_shift_all(number)
            k.set_phase_flowers()
            return k

        self.play(
            UpdateFromFunc(
                k_disp,
                lambda mob: mob.become(small_change(k_disp, phase_tracker.get_value())
                )
            ),
            phase_tracker.set_value, tick_end_ph, rate_func=linear, run_time=1
        )
        print("hell3")
        self.wait()

        #blog3 :
        tick_next_amp = 0 # set again back down to 0
        self.play(
            UpdateFromFunc(
                VGroup(k_disp),
                lambda mob: mob.become(VGroup(
                    self.perperation_math_and_disp_scene2(pixels, val_tracker, preset_position="UP")
                ))
            ),
            val_tracker.set_value, tick_next_amp, rate_func=linear, run_time=1
        )

scene="Scene2_with_phase_change"  #FULL ANIMATION SCENE phase but no real_out
class Scene2_with_phase_change(ThreeDScene):  # with real plane on the right

    def construct(self):
        run_setting = {"run_time": 2  , "rate_func": linear}
        # GENERAL:
        postion_setting={"preset_position":"LEFT","center_dist": 1}
        UP_arrow= SVGMobject("arrow.svg",fill_color= ORANGE).shift(UP*4.5)
        UP_arrow.set_shade_in_3d(True)
        self.add(UP_arrow)
        #self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        #pixels = 19 #this is how it shoud be
        pixels=5 # only shortly
        #math_preperation:
        value=0
        k_math=FourierMathJuggling.k_from_preset_minimal(pixels,**postion_setting)
        k_disp=K_Space(pixel_len=pixels)
        img_kamp,img_kph= k_math.get_amp_and_ph()
        k_disp.fill_k_space(img_kamp)
        self.add(k_disp)
        ##blog 1
        # tick_start_amp = 0; tick_end_amp = 255
        # val_tracker = ValueTracker(tick_start_amp)
        # def Tiny_UpdaterA(my_object, val_trackerX):
        #     def modify_amp(my_object):
        #         k_math = FourierMathJuggling.k_from_preset_minimal(pixels, **postion_setting,
        #                                                            amplitude=val_trackerX.get_value())
        #         my_object.fill_k_space(k_math.get_amp_and_ph()[0])
        #         return my_object
        #     return UpdateFromFunc(my_object, modify_amp)
        # self.play(Tiny_UpdaterA(k_disp, val_tracker), val_tracker.set_value, tick_end_amp,**run_setting)

        self.wait()  ##here starts the phase change
        k_disp.val=0
        val=0
        def update_planet(mob,dt):
            mob.val=int(mob.val + dt*100)+val
            print(int(mob.val))
            k_math.phase_shift_single(mob.val, **postion_setting)
            mob.set_phase_flowers(*k_math.get_amp_and_ph())
        k_disp.add_updater(update_planet)
        self.wait(5)

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
        k_disp = K_Space(pixel_len=pixels)   # setup the k_disp
        k_disp.fill_k_space(img_kamp=(img_kamp), dots_lines=True)
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

        my_plane = K_Space(pixel_len=pixels)

        # middle the plane
        my_plane.set_x(0) ##not needed anymore
        my_plane.set_y(0)
        my_plane.set_z(0)
        my_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        my_plane.fill_k_space(img_kamp=fourier_s, dots_lines=True)
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
        print(img2)
        self.wait(10)
        my_plane2= K_Space(pixel_len=pixels)
        my_plane2.set_x(0) #not needed anymore
        my_plane2.set_y(0)
        my_plane2.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        my_plane2.fill_k_space(img_kamp=img2, dots_lines=True)
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
    command_A = "manim   -l -p    -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)