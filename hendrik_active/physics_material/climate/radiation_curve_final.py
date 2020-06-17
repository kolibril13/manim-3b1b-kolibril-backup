from manimlib.imports import *

class Radiation(Scene):
    def construct(self):
        offset=3.5*LEFT
        earth= ImageMobject("earth.png")
        heading= TextMobject(r"Earth radiation spectrum").to_edge(UP).scale(2)
        self.play(FadeInFromDown(heading))
        earth.shift(offset).scale(1.3)
        self.play(FadeIn(earth))
        self.play(FadeOut(earth))
        y_text= TextMobject("Heat radiation from earth")
        y_text.rotate(np.pi/2)
        x_text= TextMobject("wavelength")
        x_teo=np.loadtxt("teoX.csv")/100000*3
        y_teo=np.loadtxt("teoY.csv")/1000*3
        x_exp=np.loadtxt("messX.csv")/100000*3
        y_exp=np.loadtxt("messY.csv")/1000*3
        curve_teo = VMobject()
        point=Dot([x_exp[119], y_exp[119],0])
        co2ar=Arrow(point.get_center()+1.2*DOWN, point.get_center(), color=DRAC_ORANGE)
        co2_text= TexMobject(r"\text{Caused by CO}_2",color=DRAC_ORANGE).next_to(co2ar,DOWN)
        curve_teo.set_points_smoothly([[xi,yi,0]
        for xi, yi in zip(x_teo,y_teo) ] )
        curve_exp = VMobject()
        curve_exp.set_points_smoothly([[xi,yi,0]
                                   for xi, yi in zip(x_exp,y_exp) ] )
        curve_teo.set_style(stroke_width=4)
        curve_teo2= curve_teo.copy().set_style(stroke_opacity=0.5)
        text_teo= TextMobject("theory").scale(0.8)
        text_exp= TextMobject("Nasa measurement").scale(0.8)
        x_text.scale(0.4).next_to(curve_teo,DOWN)
        x_text.align_to(curve_teo,LEFT)
        text_teo.next_to(curve_teo,UP)
        text_teo.align_to(curve_teo,RIGHT)
        y_text.scale(0.4).next_to(curve_teo, LEFT)
        y_text.align_to(curve_teo,DOWN)
        text_exp.next_to(curve_teo,UP)
        text_exp.align_to(curve_teo,RIGHT)
        self.play(FadeIn(y_text), FadeIn(text_teo), FadeIn(x_text))
        self.play(Write(curve_teo),run_time=1.4)
        self.add(curve_teo2)
        self.wait(2)
        # # earth =  Circle().set_style(fill_color=BLUE, stroke_color= BLUE_B ,fill_opacity=1).shift(offset)
        # # self.add(earth)
        # N=400
        # R= np.random.uniform(1.4,1.7, (N,1))
        # PHI= np.random.uniform(1,2*np.pi+1, (N,1))
        # Co2s= np.array([[float(r*np.sin(phi)), float(r*np.cos(phi)) ,0] for r,phi in zip(R,PHI)])
        # dots=VGroup(*[Dot(point=co2+offset, fill_opacity=0.4,radius=0.05) for co2 in Co2s ])
        # dots0=dots.copy().scale(0.6).set_style(fill_opacity=0)
        # self.add(dots0)
        # self.play(FadeOut(text_teo), FadeInFromDown(text_exp))
        # self.play(Transform(dots0,dots,lag_ratio=0.01), Transform(curve_teo,curve_exp), run_time=10)
        # self.play(FadeIn(co2ar), FadeIn(co2_text))
        #
        # self.wait(3)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Radiation"
    os.system(command_A + command_B)