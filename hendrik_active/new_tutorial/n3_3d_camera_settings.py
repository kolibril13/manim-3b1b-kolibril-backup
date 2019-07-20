from manimlib.imports import *

class K_Space(VMobject):
    CONFIG = {
        "Pixel":2,
        "pixel_len":23,
        "mushroom_heigt":1.1,
        "magic_offset_z":1

    }
    def __init__(self, size , **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)


    def generate_points(self):
        self.term= VGroup()
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [Square(fill_opacity=1, side_length=1) for i in range(0, PIXELS)]
        j = 0
        for i, square_to_move in enumerate(square_ALL):
            if i % np.sqrt(PIXELS) == 0:
                j += 1
            k = i - j * np.sqrt(PIXELS)
            square_to_move.move_to((LEFT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.add(self.term)

    def fill_k_space(self, img_array, dots_lines=False):
        t_objects = [t for t in self.term.submobjects]
        # create color gradient
        colors = [BLACK, WHITE]
        colors = color_gradient(colors, 256)
        img_array = img_array.flatten()
        # create dots array
        self.dots = VGroup()
        self.lines = VGroup()
        for i, el in enumerate(t_objects):
            wanted_color = colors[img_array[i]]
            el.set_color(wanted_color)

            if dots_lines == True:
                wanted_height = img_array[i]/255*self.mushroom_heigt

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

    def set_magic_gauss(self):
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

class lala(ThreeDScene):
    def construct(self):

        #axes:
        pixels= 33
        # # camera settings
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES,distance=100) #2.5D
        #self.set_camera_orientation(phi=0 * DEGREES, theta=-45 * DEGREES) #TOP
        #self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES) #side

        self.begin_ambient_camera_rotation(rate=0.1)  # Start move camera
        my_plane= K_Space(2,pixel_len=pixels)
        # img= np.uint8(np.random.randint(1, 255, (pixels,pixels)))
        img = np.uint8(np.fromfunction(lambda i, j: 255 / 2 * (np.sin(0.9 * j) + 1), (pixels, pixels), dtype=int))

        #middle the plane
        my_plane.set_x(0)
        my_plane.set_y(0)
        self.add(my_plane)
        my_plane.fill_k_space(img_array=img)
        my_plane.scale_about_point(9 / pixels, ORIGIN)
        # my_plane.shift(LEFT*4)
        self.move_camera(frame_center=LEFT*4)
        self.wait()






if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -l -s -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lala"
    os.system(command_A + command_B)