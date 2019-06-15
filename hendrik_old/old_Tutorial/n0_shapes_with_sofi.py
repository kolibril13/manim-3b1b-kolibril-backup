from manimlib.imports import *

class Shapes(Scene):
    def construct(self):
        ###
        print ("yummy")
        circle=Circle(radius=0.5,color=GREEN, arc_center=np.array((1,2,0)))
        self.add(circle)
        self.wait(2)
        circle2=Circle(radius=1,color=PURPLE, arc_center=np.array((2,1,0)))
        self.play(Transform(circle,circle2))
        self.wait(2)
        circle4=Circle(radius=0.5,color=GREEN, arc_center=np.array((1,2,0)))
        self.play(FadeIn(circle4))
        self.wait(2)
        circle3=Circle(radius=2)
        self.play(FadeIn(circle3))
        self.wait(2)
        sss= TexMobject(r"\mars",color=PURPLE)
        sss.scale(scale_factor=6)
        self.play(Transform(circle4,sss))
        self.wait(3)




        ###

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p -s -o earth_sofi  --leave_progress_bars " + module_name + " Shapes "
    os.system(command)

# print("Start")
# dot = Dot()
# circle = Circle( radius = 2)
# self.add(dot)
# self.play(GrowFromCenter(circle))
# self.wait(2)
