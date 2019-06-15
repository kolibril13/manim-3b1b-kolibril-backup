from manimlib.imports import *

class Screensizes(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait(0.1)
        rectangle = Rectangle(height=8, width=14.2)
        self.play(GrowFromCenter(rectangle))
        self.wait(1)

if __name__ == "__main__":
    import os
    file= os.path.basename(__file__)
    w = str(1920)
    h = str(1080)
    resolution = "--resolution " + h + ","+ w
    command= "python3.7 -m manim -p --leave_progress_bars " + file + " Screensizes -o Lenovo_screen " + resolution
    # command= "python3.7 -m manim -h"
    os.system(command)



