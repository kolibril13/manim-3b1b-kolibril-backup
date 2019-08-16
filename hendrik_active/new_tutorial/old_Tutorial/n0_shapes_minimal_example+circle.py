from manimlib.imports import *

class Shapes(Scene):
    CONFIG ={
        "color": BLUE
    }
    def construct(self):
        print("Start")
        dot = Dot()
        circle = Circle(radius= 1, color=self.color)
        circle2 = Circle(radius= 1.1)
        circle2.set_color(GREEN)
        self.add(dot)
        self.play(GrowFromCenter(circle),GrowFromCenter(circle2))
        self.wait(2)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -a -pl  " + module_name
    os.system(command)

