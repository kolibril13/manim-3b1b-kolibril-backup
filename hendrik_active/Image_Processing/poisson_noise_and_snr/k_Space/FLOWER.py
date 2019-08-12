from manimlib.imports import *


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
            knosp.shift(OUT*0.00001)
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
            bloss.shift(OUT*0.00002)#
            nekta.shift(OUT*0.00003)
            # bloss.shift(OUT * 0.2)#
            # nekta.shift(OUT * 0.4)
            #bloss.set_shade_in_3d(True)
            #nekta.set_shade_in_3d(True)
            self.add( bloss,nekta)
        if 270 <= self.a_deg:
            if self.a_deg < 315:
                self.scale_fac = (self.a_deg -270)/ 45
            else:
                self.scale_fac = 1
            bloss.set_color(interpolate_color(self.color3, self.col_spare,self.scale_fac))
            knosp.set_color(interpolate_color(self.color1, "#0c7027",self.scale_fac))

        if 315 <= self.a_deg:
            last_param= (self.a_deg -315)/ 40
            knosp.set_color(interpolate_color("#0c7027", self.color4,last_param))
            nekta.set_color(interpolate_color(self.color2, self.color4,last_param))
           # [i.scale(1-last_param) for i in self.submobjects]
            #[i.set_style(stroke_width=1) for i in self.submobjects]
            if 340 <= self.a_deg:
                last_last_param=  (self.a_deg-340)/20
                bloss.set_style(fill_opacity=1-last_last_param)
                [i.scale(1 - last_last_param) for i in self.submobjects]

                #[i.set_style(stroke_width=1) for i in self.submobjects]
                # [i.set_style(fill_opacity=1-last_last_param) for i in self.submobjects]

    def __str__(self):
        return f'FLOWER({self.a_deg})'