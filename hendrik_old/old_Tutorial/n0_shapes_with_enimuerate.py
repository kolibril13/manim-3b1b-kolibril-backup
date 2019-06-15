from manimlib.imports import *

class Shapes(Scene):
    CONFIG = {"radius" : np.arange(2,5,1),
              "symbols": [r"\mars", r"\earth", r"\mercury"]}

    def construct(self):
        print("Start")
        ALLCIRCS = [Circle(radius=num_rad)for num_rad in self.radius]
        ALLSYMBOLS= [TexMobject(stin).scale(6) for stin in self.symbols]
        dot = Dot()
        dot2 = Dot()
        self.add(dot,dot2)
        for n, shape in enumerate(ALLCIRCS):
            self.play(Transform(dot,ALLCIRCS[n]),Transform(dot2,ALLSYMBOLS[n]), run_time=1)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -pl  -o earth_sofi  --leave_progress_bars " + module_name + " Shapes "
    os.system(command)



