from manimlib.imports import *

class Radiation1(Scene):
    def construct(self):
        offset=3*LEFT
        earth =  Circle().set_style(fill_color=BLUE, stroke_color= BLUE_B ,fill_opacity=1).shift(offset)
        eart2= ImageMobject("/hendrik_active/physics_material/climate/earth.png")
        self.add(earth,eart2.shift(offset).scale(1.3))
        N=400
        R= np.random.uniform(1.4,1.7, (N,1))
        PHI= np.random.uniform(1,2*np.pi+1, (N,1))
        Co2s= np.array([[float(r*np.sin(phi)), float(r*np.cos(phi)) ,0] for r,phi in zip(R,PHI)])
        dots=VGroup(*[Dot(point=co2+offset, fill_opacity=0.4,radius=0.05) for co2 in Co2s ])
        dots0=dots.copy().scale(0.6).set_style(fill_opacity=0)
        self.add(dots0)
        self.play(Transform(dots0,dots),lag_ratio=0.01, run_time=2)
        text1= TextMobject("More CO2 means:")
        text2= TextMobject("-less heat radiation").next_to(text1,RIGHT)
        text3= TextMobject("-warmer earth surface").next_to(text2,DOWN)
        text4= TextMobject("-collaps of ecosystems").next_to(text3,DOWN)
        text3.align_to(text2, LEFT)
        text4.align_to(text3, LEFT)

        textfin= VGroup(text1,text2,text3,text4).scale(0.8).to_edge(DOWN)
        self.add(textfin)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Radiation1"
    os.system(command_A + command_B)