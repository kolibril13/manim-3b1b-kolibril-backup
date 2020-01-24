from manimlib.imports import *

class Radiation1(Scene):
    def construct(self):
        earth =  Circle().set_style(fill_color=BLUE, stroke_color= BLUE_B ,fill_opacity=1)
        self.add(earth)
        N=300
        R= np.random.uniform(1.4,1.7, (N,1))
        PHI= np.random.uniform(1,2*np.pi+1, (N,1))
        Co2s= np.array([[float(r*np.sin(phi)), float(r*np.cos(phi)) ,0] for r,phi in zip(R,PHI)])
        dots=VGroup(*[Dot(point=co2, fill_opacity=0.4,radius=0.005) for co2 in Co2s ])
        self.play(Write(dots), run_time=4)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Radiation1"
    os.system(command_A + command_B)