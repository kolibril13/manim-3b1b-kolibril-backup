print("hello")
from manimlib.imports import *
global s, e, ste
s=0
e=180
ste=8

class FLOWER(VMobject):
    CONFIG = {
        "color1":"#37a113", #green
        "color2":YELLOW, # Yellow
        "color3": "#ff0000",# nice red
        "color4": GREY_BROWN,
        "col_spare": "#2c0c3d"# purple
    }
    def __init__(self,a_deg, **kwargs):
        self.a_deg= a_deg%360
        VMobject.__init__(self, **kwargs)

        # leaf grow
        if self.a_deg >0:
            self.scale_fac = 0
            if self.a_deg < 90:
                self.scale_fac= self.a_deg/90
            else:
                self.scale_fac= 1
            knosp = VGroup(
                Ellipse(height=0.7),
                Ellipse(height=0.7).rotate(PI / 3),
                Ellipse(height=0.7).rotate(2 * PI / 3)
            ).set_style(fill_opacity=1, fill_color=self.color1, stroke_width=0).rotate(PI / 6) #green
            knosp.scale(self.scale_fac)
            self.add(knosp)

        # blossom_grow
        if self.a_deg > 90:
            self.scale_fac = 0
            if self.a_deg < 180:
                self.scale_fac = (self.a_deg -90)/ 90
            else:
                self.scale_fac = 1
            #color interpolation for blossom
            self.col_fac = 0
            if 180 < self.a_deg < 270:
                self.col_fac = (self.a_deg - 180) / 90
                bloss_col = interpolate_color(self.color2,self.color3,alpha=self.col_fac) # bright red
            else:
                bloss_col= self.color2
            bloss = VGroup(
                Ellipse(height=0.7),
                Ellipse(height=0.7).rotate(PI / 3),
                Ellipse(height=0.7).rotate(2 * PI / 3)
            ).set_style(fill_opacity=1, fill_color=bloss_col, stroke_width=0).scale(self.scale_fac*0.9)
            nekta = Dot(fill_color=YELLOW).scale(self.scale_fac*2)
            self.add( bloss,nekta)
        if 270 <= self.a_deg:
            last_param= (self.a_deg-270)/90
            self.submobjects[0].set_color(interpolate_color(self.color1, self.color4,last_param))
            self.submobjects[1].set_color(interpolate_color(self.color3, self.color4,last_param))
            self.submobjects[2].set_color(interpolate_color(self.color2, self.color4,last_param))
            #[i.scale(1-last_param) for i in self.submobjects]
            [i.set_style(stroke_width=1) for i in self.submobjects]
            [i.set_style(fill_opacity=1-last_param) for i in self.submobjects]




class artwork(Scene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360
    }

    def get_flower(self, number_flower):
        return FLOWER(number_flower.get_value())


    def construct(self):
        self.pixel_len=18
        PIXELS = self.pixel_len * self.pixel_len
        square_ALL = [FLOWER((i/PIXELS)*360) for i in range(0, PIXELS)]
        j = 0
        self.term= VGroup()
        for i, square_to_move in enumerate(square_ALL):
            if i % self.pixel_len == 0:
                j += 1
            k = i - j * self.pixel_len
            square_to_move.scale(0.4)
            square_to_move.move_to((RIGHT * k + j * DOWN))
        self.term.add(*square_ALL)
        self.term.set_y(0)
        self.term.set_x(0)
        self.term.scale(8/self.pixel_len)
        self.add(self.term)
        self.wait()

        # dot= [FLOWER(i).shift(j*RIGHT*2+LEFT_SIDE*4).scale_about_point(0.2,ORIGIN) for j,i in enumerate(np.arange(s,e,ste)) ]
        # self.add(*dot)
        # dot2 = [FLOWER(i).shift(j * RIGHT * 2 + LEFT_SIDE * 4 + 6*DOWN).scale_about_point(0.2, ORIGIN) for j, i in
        #        enumerate(np.arange(s+180, e+180, ste))]
        # self.add(*dot2)
        # self.wait()

if __name__ == "__main__":
     module_name = os.path.basename(__file__)
     command_A = "manim  -s -p -c '#2B2B2B' --video_dir ~/Downloads/ " + module_name + " artwork  "
     os.system(command_A )