from manimlib.imports import *
import os
import pyclbr

class Shapes_mandala(Scene):
    def construct(self):
            print("heellooo")
            dot = Dot()
            dot_end = Dot()

            square = Square()
            self.wait(0.1)
            self.add(dot)
            self.wait(0.1)
            print("heellooo2")
            for k in range(1,4):
                triangle = Polygon(k*np.array([1, 0, 0]),
                                   k*np.array([0, 1, 0]),
                                   k*np.array([1, 1, 0]))
                self.play(Transform(dot, triangle))
                self.add(triangle)
                triangle = Polygon(k * np.array([0, -1, 0]),
                                   k * np.array([1, 0, 0]),
                                   k * np.array([1, -1, 0]))
                self.play(Transform(dot, triangle))
                self.add(triangle)
                triangle = Polygon(k*np.array([-1, 0, 0]),
                                   k*np.array([0, -1, 0]),
                                   k*np.array([-1, -1, 0]))
                self.play(Transform(dot, triangle))
                self.add(triangle)
                triangle = Polygon(k*np.array([0, 1, 0]),
                                   k*np.array([-1, 0, 0]),
                                   k*np.array([-1, 1, 0]))
                self.play(Transform(dot, triangle))
                self.add(triangle)
                self.wait(0.2)
                print("Hello " + str(k))

            for k in range(1,4):
                circle = Circle(radius=k)
                circle.set_fill(GREEN, opacity=0.2)
                self.play(Transform(dot, circle))
                self.add(circle)
                self.play(Transform(dot, dot_end))
                self.wait(0.2)
            self.wait(0.2)
            circle = Circle(radius=4, opacity=0, color= BLACK)
            circle.set_fill(BLACK, opacity=1)
            dot = Dot()
            self.add(dot)
            self.play(FadeIn(circle))
            my_first_text = TextMobject("Goodnight")
            second_line = TextMobject("Sleep Tight!")
            second_line.next_to(my_first_text, DOWN)
            third_line = TextMobject(r"And have Sweet Dreams")
            third_line.next_to(my_first_text, DOWN)
            self.add(my_first_text, second_line)
            self.wait(2)
            self.play(Transform(second_line, third_line))
            self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -p --leave_progress_bars " + module_name + " -a "
    os.system(command)
