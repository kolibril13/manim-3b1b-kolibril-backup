from manimlib.imports import *

class Shapes(Scene):
    CONFIG ={
        "color": BLUE
    }

    def construct(self):
        print("Start")

        dot = Dot()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        self.add(line)
        dot2= dot.copy().shift(RIGHT)
        circle = Circle(radius= 1, color=self.color)
        self.add(dot)
        self.play(GrowFromCenter(circle))
        self.play(Transform(dot,dot2))
        self.play(MoveAlongPath(dot,circle), run_time= 3, rate_func=linear)
        self.play(Rotating(dot,about_point= np.array((0, 0, 0.))))
        self.wait(2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -pl -o earth_sofi  --leave_progress_bars " + module_name + " Shapes "
    os.system(command)

