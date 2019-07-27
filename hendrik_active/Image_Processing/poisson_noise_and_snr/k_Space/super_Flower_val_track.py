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
            [i.scale(1-last_param) for i in self.submobjects]
            # [i.set_style(stroke_width=1) for i in self.submobjects]
    def __str__(self):
        return f'FLOWER({self.a_deg})'


class MAIN(Scene):
    CONFIG = {
        "flower_value_start": 0,
        "flower_value_end": 360
    }

    def get_flower(self, number_flower):
        return FLOWER(number_flower.get_value())


    def construct(self):


        flow_tracker = ValueTracker(0) # is a number
        print(flow_tracker.get_value())
        flow = self.get_flower(flow_tracker)
        print(flow)
        self.add(flow)
        breakpoint()
        self.play(
            UpdateFromFunc(
                flow, lambda mob: mob.become(
                    self.get_flower(flow_tracker))
            ),
            flow_tracker.set_value, 100  ,
            run_time=4 , rate_func=linear
        )

        # self.wait()



        # dot= [FLOWER(i).shift(j*RIGHT*2+LEFT_SIDE*4).scale_about_point(0.2,ORIGIN) for j,i in enumerate(np.arange(s,e,ste)) ]
        # self.add(*dot)
        # dot2 = [FLOWER(i).shift(j * RIGHT * 2 + LEFT_SIDE * 4 + 6*DOWN).scale_about_point(0.2, ORIGIN) for j, i in
        #        enumerate(np.arange(s+180, e+180, ste))]
        # self.add(*dot2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " +"MAIN"
    os.system(command_A + command_B)