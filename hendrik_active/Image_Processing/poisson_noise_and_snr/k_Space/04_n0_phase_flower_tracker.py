from manimlib.imports import *


class FLOWER(VGroup):
    CONFIG = {
        "color1": "#37a113",  # green
        "color2": YELLOW,  # Yellow
        "color3": "#ff0000",  # nice red
        "color4": GREY_BROWN,
        "col_spare": "#2c0c3d"  # purple
    }

    def __init__(self, a_deg, **kwargs):
        self.a_deg = a_deg % 360
        VGroup.__init__(self, **kwargs)

        if self.a_deg > 0:
            self.scale_fac = 0
            if self.a_deg < 90:
                self.scale_fac = self.a_deg / 90
            else:
                self.scale_fac = 1
            knosp = VGroup(
                Ellipse(height=0.7),
                Ellipse(height=0.7).rotate(PI / 3),
                Ellipse(height=0.7).rotate(2 * PI / 3)
            ).set_style(fill_opacity=1, fill_color=self.color1, stroke_width=0).rotate(PI / 6)  # green
            knosp.scale(self.scale_fac)
            self.add(knosp)

        # blossom_grow
        if self.a_deg > 90:
            self.scale_fac = 0
            if self.a_deg < 180:
                self.scale_fac = (self.a_deg - 90) / 90
            else:
                self.scale_fac = 1
            # color interpolation for blossom
            self.col_fac = 0
            if 90 < self.a_deg < 270:
                self.col_fac = (self.a_deg - 90) / 180
                bloss_col = interpolate_color(self.color2, self.color3, alpha=self.col_fac)  # bright red
            else:
                bloss_col = self.color3
            bloss = VGroup(
                Ellipse(height=0.7),
                Ellipse(height=0.7).rotate(PI / 3),
                Ellipse(height=0.7).rotate(2 * PI / 3)
            ).set_style(fill_opacity=1, fill_color=bloss_col, stroke_width=0).scale(self.scale_fac * 0.9)
            nekta = Dot(fill_color=YELLOW).scale(self.scale_fac * 2)
            self.add(bloss, nekta)
        if 270 < self.a_deg:
            last_param = (self.a_deg - 270) / 90
            self.submobjects[0].set_color(interpolate_color(self.color1, self.color4, last_param))
            self.submobjects[1].set_color(interpolate_color(self.color3, self.color4, last_param))
            self.submobjects[2].set_color(interpolate_color(self.color2, self.color4, last_param))
            [i.set_style(fill_opacity=(1 - last_param)) for i in self.submobjects]
            [i.set_style(stroke_width=1) for i in self.submobjects]


class FlowerScene(Scene):
    CONFIG = {
        "flower_value_start": 100,
        "flower_value_end": 200
    }

    def get_flower(self, number_flower):
        return FLOWER(number_flower.get_value())

    def construct(self):
        flow_tracker = ValueTracker(self.flower_value_start)
        flow = self.get_flower(flow_tracker)

        def flower_updater(flower):
            flower.become(self.get_flower(flow_tracker))

        self.play(GrowFromCenter(flow))

        flow.add_updater(flower_updater)
        self.add(flow)

        self.play(flow_tracker.set_value, self.flower_value_end)

        self.wait()
