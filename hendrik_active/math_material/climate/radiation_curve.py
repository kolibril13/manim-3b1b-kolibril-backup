from manimlib.imports import *

class Radiation(Scene):
    def construct(self):
        bolzmann= TexMobject(r"B_\nu(\nu, T) = \frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/kT} - 1}")
        text1= TextMobject("theory")
        text2= TextMobject("experiment")
        self.add(bolzmann.to_edge(UR))
        x_teo=np.loadtxt("teoX.csv")/100000*3
        y_teo=np.loadtxt("teoY.csv")/1000*3
        x_exp=np.loadtxt("messX.csv")/100000*3
        y_exp=np.loadtxt("messY.csv")/1000*3
        curve_teo = VMobject()
        curve_teo.set_points_smoothly([[xi,yi,0]
        for xi, yi in zip(x_teo,y_teo) ] )
        curve_exp = VMobject()
        curve_exp.set_points_smoothly([[xi,yi,0]
                                   for xi, yi in zip(x_exp,y_exp) ] )
        curve_teo.set_style(stroke_width=4)
        curve_teo2= curve_teo.copy().set_style(stroke_opacity=0.5)
        text1.next_to(curve_teo,DOWN)
        text1.align_to(curve_teo,RIGHT)
        self.add(text1)
        text2.next_to(curve_teo,DOWN)
        text2.align_to(curve_teo,RIGHT)
        self.play(Write(curve_teo))
        self.add(curve_teo2)
        self.play(Transform(curve_teo,curve_exp), FadeOut(text1), FadeInFromDown(text2))
        self.wait()




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Radiation"
    os.system(command_A + command_B)