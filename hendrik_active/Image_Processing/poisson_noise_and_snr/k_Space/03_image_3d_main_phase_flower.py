from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.super_Flower import FLOWER
import cmath

global FACTOR
FACTOR=0.7
class K_Space(VMobject):
    CONFIG = {
        "Pixel":2,
        "pixel_len":23,
        "mushroom_heigt":1.1,
        "magic_offset_z":FACTOR

    }
    def __init__(self , **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
        self.term= VGroup()
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.move_to((LEFT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.add(self.term)

    def fill_k_space(self, k_amp_ar, dots_lines=False):
        t_objects = [t for t in self.term.submobjects]
        k_amp_ar = k_amp_ar.flatten()

        # create dots array
        self.dots = VGroup()
        self.lines = VGroup()
        for i, el in enumerate(t_objects):
            # interpol_col
            wanted_color = interpolate_color(BLACK, WHITE, k_amp_ar[i] / 255)
            el.set_color(wanted_color)

            if dots_lines == True:
                wanted_height = k_amp_ar[i] / 255 * self.mushroom_heigt

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

            self.add(self.dots)
            self.add(self.lines)

    def set_phase_flowers(self,amp_array,phase_array):
        t_objects = [t for t in self.term.submobjects]
        amp_array = amp_array.flatten()
        phase_array=phase_array.flatten()
        # create dots array
        self.flows = VGroup()
        for i, el in enumerate(t_objects):
            wanted_heightx = amp_array[i] / 255 * self.mushroom_heigt
            flow = FLOWER(phase_array[i])
            # flow.scale(0.21)
            flow.scale(0.5)
            flow.move_to(el.get_center()+OUT*wanted_heightx)

            # append the pixels
            self.flows.add(flow)
        self.add(self.flows)



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
        "Pixel": 2,
        "pixel_len": 23,
        "mushroom_heigt": 1.1,
        "magic_offset_z": FACTOR

    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)
        self.term = VGroup()
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1 , stroke_width=0) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.move_to((LEFT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.add(self.term)

    def fill_real_space(self, real_ar):
        t_objects = [t for t in self.term.submobjects]
        real_ar = real_ar.flatten()
        #interpolate the colors from array
        for i, el in enumerate(t_objects):
            el.set_color(interpolate_color(BLACK, WHITE, real_ar[i] / 255))



class lala(ThreeDScene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360*3
    }

    def construct(self):

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES) #2.5D
        self.begin_ambient_camera_rotation(rate=0.01)  # Start move camera

        def get_amp_array(z):
            return abs(z)

        def get_phi_array(z):
            phi=[[cmath.phase(z_row) for z_row in z_col] for z_col in z]
            return np.rad2deg(phi)
        #setup the sizes and arrays
        pixels=7
        k_space_ar= np.zeros((pixels, pixels), dtype=complex)
        ##
        def get_angle_phi(phi_deg):
            all= VGroup()
            r=255
            phi=phi_deg
            z=r * np.exp(1j * np.deg2rad(phi))
            k_space_ar[4,3]=z

            amp_ar=get_amp_array(k_space_ar)
            phi_ar=get_phi_array(k_space_ar)
            # print(phi_ar)
            k_space_ar_shift= np.fft.ifftshift(k_space_ar)
            real_out_ar =  np.fft.ifft2(k_space_ar_shift)

            # setup the k_plane
            k_plane = K_Space(pixel_len=pixels)
            k_plane.set_x(0)
            k_plane.set_y(0)
            k_plane.set_z(-0.01)
            k_plane.fill_k_space(k_amp_ar=amp_ar, dots_lines=True)
            k_plane.set_phase_flowers(amp_array=amp_ar,phase_array=phi_ar)
            k_plane.scale_about_point(9/pixels*FACTOR,ORIGIN)
            k_plane.set_shade_in_3d(True)
            all.add(k_plane)
            # setup the real_out_plane
            real_out_plane = Realspace(pixel_len=pixels)
            real_out_plane.fill_real_space(real_ar=real_out_ar.real)
            real_out_plane.scale(9 / pixels * FACTOR * 0.4).to_edge(UR)
            all2=real_out_plane
            return all,all2
        flow_tracker=ValueTracker(0)

        def flower_updater_a(a1):
            a2,b2=get_angle_phi(flow_tracker.get_value())
            a1.become(a2)

        def flower_updater_b(b1):
            a2,b2=get_angle_phi(flow_tracker.get_value())
            b1.become(b2)

        a1,b1=get_angle_phi(0)
        self.add(a1)
        self.add_fixed_in_frame_mobjects(b1)
        a1.add_updater(flower_updater_a)
        b1.add_updater(flower_updater_b)

        self.play(flow_tracker.set_value, self.flower_value_end ,run_time=50)





if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s  -p  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lala"
    os.system(command_A + command_B)