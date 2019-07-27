from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FLOWER import FLOWER

scenes= ["MiniFixedKScene","FixedKScene", "MovingKScene", "FilterkScene" ]
global k_plane_size
k_plane_size=0.7
class K_Space(VMobject):
    CONFIG = {
        "Pixel":2,
        "pixel_len":23,
        "mushroom_heigt":1.1,
        "magic_offset_z":k_plane_size

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

    def fill_k_space(self, img_kamp, dots_lines=False):
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

            self.add(self.dots)
            self.add(self.lines)

    def set_phase_flowers(self, img_kamp, img_kph):
        t_objects = [t for t in self.term.submobjects]
        img_kamp = img_kamp.flatten()
        img_kph = img_kph.flatten()
        # create dots array
        self.flows = VGroup()
        for i, el in enumerate(t_objects):
            wanted_heightx = img_kamp[i] / 255 * self.mushroom_heigt
            # set height
            # dot = FLOWER(img_kph[i]).scale(0.21)
            dot = FLOWER(img_kph[i]).scale(0.51) # for special cases
            dot.move_to(el.get_center()+OUT*wanted_heightx)
            # append the pixels
            self.flows.add(dot)
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
        "magic_offset_z": k_plane_size

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

    def fill_real_space(self, img_real):
        t_objects = [t for t in self.term.submobjects]
        img_real = img_real.flatten()
        #interpolate the colors from array
        for i, el in enumerate(t_objects):
            el.set_color(interpolate_color(BLACK, WHITE, img_real[i] / img_real.max()))


############ ANIMATION START
scene="MiniFixedK_scene"
class MiniFixedK_scene(ThreeDScene):  # with real plane on the right
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)

        pixels = 7  # setup the sizes
        raster_size= (pixels,pixels)
        r = np.random.uniform(0, 255, raster_size) # setup function
        phi_rad= np.full(raster_size, 5)
        img_k_space = r * np.exp(1j * phi_rad) # phi_rad must be in radians!
        img_kamp = np.abs(img_k_space)
        img_kph = (np.angle(img_k_space, deg=True))

        k_plane = K_Space(pixel_len=pixels)   # setup the k_plane
        k_plane.set_x(0)
        k_plane.set_y(0)
        # k_plane.set_z(0.01) ## why again?
        k_plane.fill_k_space(img_kamp=img_kamp, dots_lines=True)
        k_plane.set_phase_flowers(img_kamp=img_kamp, img_kph=img_kph)
        k_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        k_plane.set_shade_in_3d(True)
        self.add(k_plane)

class FixedKScene_OUT(ThreeDScene):  # with real plane on the right (forier transform)
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        pixels = 7  # setup the sizes
        raster_size = (pixels, pixels)
        r= np.zeros(raster_size, dtype=complex)
        # phi_rad = np.random.uniform(0, 2 * np.pi, (pixels, pixels))
        img_k_space = r
        img_k_space[2,5]= 255*np.exp(1j*2/3*np.pi)
        print(img_k_space)
        img_kamp = np.abs(img_k_space)
        img_kph = (np.angle(img_k_space, deg=True))
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)
        print(abs(real_out_ar.real))

        # setup the k_plane
        k_plane = K_Space(pixel_len=pixels)
        k_plane.set_x(0)
        k_plane.set_y(0)
        k_plane.set_z(0.01)
        k_plane.fill_k_space(img_kamp=img_kamp, dots_lines=True)
        k_plane.set_phase_flowers(img_kamp=img_kamp, img_kph=img_kph)
        k_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        k_plane.set_shade_in_3d(True)
        self.add(k_plane)

        # setup the real_out_plane
        real_out_plane = Realspace(pixel_len=pixels)
        real_out_plane.fill_real_space(img_real=abs(real_out_ar))
        real_out_plane.scale(9 / pixels * k_plane_size * 0.4).to_edge(UR)
        all2 = real_out_plane
        self.add_fixed_in_frame_mobjects(all2)

class FixedKScene_OUT_random(ThreeDScene):  # with real plane on the right (forier transform)
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)  # 2.5D
        self.camera.frame_center.shift(2 * OUT)
        #self.begin_ambient_camera_rotation(rate=0.01)  # Start move camera
        # setup the sizes
        pixels = 7
        # setup function
        r = np.random.uniform(0, 255, (pixels, pixels))
        phi_rad = np.random.uniform(0, 2 * np.pi, (pixels, pixels))
        img_k_space = r * np.exp(1j * phi_rad)
        img_kamp = np.abs(img_k_space)
        img_kph = (np.angle(img_k_space, deg=True))
        # calculate realspace
        k_space_ar_shift = np.fft.ifftshift(img_k_space)
        real_out_ar = np.fft.ifft2(k_space_ar_shift)
        print(abs(real_out_ar))

        # setup the k_plane
        k_plane = K_Space(pixel_len=pixels)
        k_plane.set_x(0)
        k_plane.set_y(0)
        k_plane.set_z(0.01)
        k_plane.fill_k_space(img_kamp=img_kamp, dots_lines=True)
        k_plane.set_phase_flowers(img_kamp=img_kamp, img_kph=img_kph)
        k_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        k_plane.set_shade_in_3d(True)
        self.add(k_plane)

        # setup the real_out_plane
        real_out_plane = Realspace(pixel_len=pixels)
        real_out_plane.fill_real_space(img_real=abs(real_out_ar))
        real_out_plane.scale(9 / pixels * k_plane_size * 0.4).to_edge(UR)
        all2 = real_out_plane
        self.add_fixed_in_frame_mobjects(all2)



class FixedKScene(ThreeDScene): # with real plane on the left
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
        print(img)

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
        my_plane.set_x(0)
        my_plane.set_y(0)
        my_plane.set_z(0)
        my_plane.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        my_plane.fill_k_space(img_kamp=fourier_s, dots_lines=True)
        my_plane.set_phase_flowers(fourier_s,fourier_s)
        my_plane.set_shade_in_3d(True)
        # self.play(TransformFromCopy(r,my_plane))
        self.add(my_plane)
        self.wait()


class MovingScene(ThreeDScene):
    pass


class FilterkScene(ThreeDScene):
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
        print(img)

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
        my_plane.set_x(0)
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
        my_plane2.set_x(0)
        my_plane2.set_y(0)
        my_plane2.scale_about_point(9 / pixels * k_plane_size, ORIGIN)
        my_plane2.fill_k_space(img_kamp=img2, dots_lines=True)
        self.play(Transform(magic_plane,magic_gauss),
                   Transform(my_plane,my_plane2),run_time=1)
        # # self.wait(10)





class spare_things(ThreeDScene): ### often used camera positions, etc.

    def construct(self):
        pass


scene="FixedKScene_OUT"
# if scene == scenes[0] or scenes[1]:
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s   -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " + scene
    os.system(command_A + command_B)