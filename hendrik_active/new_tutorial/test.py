from manimlib.imports import *

class MyDotGrid(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        col = [GREEN, BLUE]
        colors = color_gradient(col, 20)
        dots=[Dot(fill_color=co).shift(LEFT*0.5*i) for i,co in enumerate(colors) ]
        self.dotgrid= VGroup(*dots)
        self.dotgrid.move_to(ORIGIN)
        self.add(self.dotgrid)

    def update_dot(self,val):
        self.dotgrid.become(self.dotgrid.move_to(UP*0.01*val))

class Example_Scene(Scene):
    def construct(self):
        dot = MyDotGrid()
        self.add(dot)
        self.wait(1)
        tr=ValueTracker(0)
        def updater(mob):
            mob.update_dot(tr.get_value())
            return mob

        self.play(tr.increment_value,90, UpdateFromFunc(dot,updater))

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Example_Scene"
    os.system(command_A + command_B)