from manimlib.imports import *
from hendrik_active.Image_Processing.poisson_noise_and_snr.k_Space.FLOWER import FLOWER

global k_plane_size
k_plane_size=0.7

class KSpace(VMobject):
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
        self.term.set_z(0.00001)  ## Important, because otherwise dots are visible ...
        self.term.scale_about_point(9 / self.pixel_len * k_plane_size, ORIGIN)
        # self.term.set_shade_in_3d(True)
        self.add(self.term) ## better return term???
        self.add(self.flows)
        self.add(self.lines_and_dots)
        # lastly the middle point
        # ORI_POINT = Dot(fill_color=ORANGE).shift(OUT * 0.1).scale(1.5)
        # ORI_POINT.set_shade_in_3d(True)
        ORI_POINT = Dot(fill_color=ORANGE).scale(1.5)
        ORI_POINT.set_z(0.0001)
        self.add(ORI_POINT)

    def fill_k_space_updater(self, img_kamp): #empty it first, then refill
        t_objects = [t for t in self.term.submobjects]
        img_kamp = img_kamp.flatten()
        # create dots array
        self.dots = VGroup()
        self.lines = VGroup()
        for i, el in enumerate(t_objects):
            # interpol_col
            wanted_color = interpolate_color(BLACK, WHITE, img_kamp[i] / 255)
            el.set_color(wanted_color)

            wanted_height = img_kamp[i] / 255 * self.mushroom_heigt
            if wanted_height != 0:
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

        self.new_lines_and_dots=VGroup(self.dots,self.lines)#.set_shade_in_3d(True)
        self.lines_and_dots.become(self.new_lines_and_dots)


    def set_phase_flowers_updater(self,img_kamp, img_kph):
        self.new_flows= VGroup()
        t_objects = [t for t in self.dots.submobjects]
        img_kph = img_kph.flatten()
        # create dots array
        for i, el in enumerate(t_objects):
            if img_kph[i] is not 0:  # do not call FLOWER when phase is even 0
                # set height
                flo = FLOWER(img_kph[i]).scale(0.31)  # when a lot of flowers ar in the game
                # flo = FLOWER(img_kph[i]).scale(0.51)  # for minimal example
                flo.move_to(el.get_center()+ OUT*0.0001)
                flo.set_shade_in_3d(True)
                # append the pixels
                self.new_flows.add(flo)
        self.flows.become(self.new_flows)
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
        self.add(magic_gauss)

    def gauss_array_2d(self,sigma=1 , mu=0):
        x, y = np.meshgrid(np.linspace(-1, 1, self.pixel_len), np.linspace(-1, 1, self.pixel_len))
        d = np.sqrt(x * x + y * y)
        g = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
        return g