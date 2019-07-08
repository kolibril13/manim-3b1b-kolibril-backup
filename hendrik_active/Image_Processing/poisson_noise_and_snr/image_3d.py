from manimlib.imports import *

class K_Space(VMobject):
    CONFIG = {
        "Pixel":2,
        "pixel_len":23

    }
    def __init__(self, size , **kwargs):
        digest_config(self, kwargs)
        VMobject.__init__(self, **kwargs)


    def init_colors(self):
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
                wanted_opacity = img_array[i] / 255
                wanted_height = wanted_opacity * 3

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
        sigma, mu = 0.4, 0.0
        g = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
        print(g)
        img_array = img_array.flatten()
        g=g.flatten()
        for i, (el,dot,line) in enumerate(zip(self.term, self.dots, self.lines)):

            # wanted_opacity = img_array[i] / 255 * g[i]
            wanted_opacity = g[i]
            # set opacity
            el.set_opacity(1)
            dot.set_opacity(wanted_opacity)
            line.set_opacity(wanted_opacity)



class lala(ThreeDScene):
    def construct(self):
        pixels= 19
        # camera settings
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        #self.set_camera_orientation(phi=90 * DEGREES, theta=0 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)  # Start move camera
        my_plane= K_Space(2,pixel_len=pixels)
        img= np.uint8(np.random.randint(1, 255, (pixels,pixels)))

        my_plane.move_to(ORIGIN)
        my_plane.fill_k_space(img_array=img, dots_lines=True)
        my_plane.set_shade_in_3d(True)
        my_plane.set_z(0)
        self.add(my_plane.scale(9/pixels))
        #opacity_test
        self.index_text= None
        a=[1,1,1]
        b=[0,1,0]
        c=[0,0,1]
        d= [1,0,0]
        list=[a]
        for i, opa in enumerate(list):
            if i>0:
                print("true")
                self.remove(self.mobjects[self.index_text])
            text = f"Opacity plane:{opa[0]}, dot:{opa[1]}, line:{opa[2]}"
            te = TextMobject(text).scale(2)
            te.to_corner(UL)
            self.add_fixed_in_frame_mobjects(te)
            self.index_text = len(self.mobjects) - 1
            my_plane.set_subobject_opacity(img,opa)
            self.wait(2)






if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -s  -c '#1C758A' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lala"
    os.system(command_A + command_B)