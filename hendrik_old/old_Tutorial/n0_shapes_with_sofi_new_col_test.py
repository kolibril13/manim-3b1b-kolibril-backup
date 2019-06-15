from manimlib.imports import *

# "DRAC_GREY": "#2B2B2B",
# "DRAC_GREY_LIGHT": "#808080",
# "DRAC_YELLOW": "#FFC66D",
# "DRAC_YELLOW_GREEN": "#A5C261",
# "DRAC_ORANGE": "#CC7832",
# "DRAC_GREEN": "#6A8759",
# "DRAC_LILA": "#9876AA",
class Shapes(Scene):
    def construct(self):
        ###
        circle0=Circle(radius= 2 ,  color= DRAC_ORANGE ,      arc_center=np.array((0,0,0)))
        circle1=Circle(radius= 0.5 ,color=DRAC_GREEN,         arc_center=np.array((1,2,0)))
        circle2=Circle(radius= 1 ,  color=DRAC_YELLOW,       arc_center=np.array((2,1,0)))
        planet= TexMobject(r"\sun",color=DRAC_GREY_LIGHT)
        planet.scale(scale_factor=6)
        self.add(circle0)
        self.add(circle1)
        self.add(circle2)
        self.add(planet)
        self.wait(3)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p -s    -c '#2B2B2B' -a --leave_progress_bars " + module_name
    os.system(command)
