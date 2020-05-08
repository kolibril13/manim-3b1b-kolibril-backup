from manimlib.imports import *

class RandomW(Scene):
    ## important : set FRAME_HEIGHT = 1080 in constants.py
    def construct(self):
        sw= 400
        r= VGroup(Line(UL,DL, stroke_width=sw),
                  Line(DL, DR, stroke_width=sw),
                  Line(DR,UR,stroke_width=sw)).set_color(BLACK).set_stroke(BLACK)
        r.set_height(800, stretch=True).set_width(1500, stretch=True)
        ob2 = BackgroundRectangle(r).set_color(BLUE).set_opacity(0.2)
        ob2.set_height(750, stretch=True)
        ob2.align_to(r, DOWN)
        self.add(r, ob2)
        radi= 20
        partis = []
        np.random.seed(21)
        for i in range(0,10):
            particle1 = Dot(radius = radi).set_color(RED)
            c= Arc(radius= radi, start_angle= 0, angle=TAU, stroke_width=300).set_color(interpolate_color(RED_E, BLACK,0.4))
            part1 = VGroup(particle1,c)
            partis.append(part1)

        [part.move_to([np.random.randint(-700,700),np.random.randint(-300,250),0]) for part in partis]
        self.play(*[FadeIn(part) for part in partis])
        def particle_updater(d,dt):
            d.shift(RIGHT*np.random.choice([-1,1]))
            d.shift(UP*np.random.choice([-1,1]))
        [par.add_updater(particle_updater) for par in partis]
        self.wait(15)
    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name +" " +"RandomW"
    os.system(command_A + command_B)