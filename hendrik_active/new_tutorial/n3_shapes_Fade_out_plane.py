
from manimlib.imports import *

class Text(Scene):

    def construct(self):
        sq= Square()
        sq2= Square()
        sq2.next_to(sq,LEFT)
        sq3= Square()
        sq3.next_to(sq,RIGHT)
        circ = Circle().next_to(sq,DOWN)
        self.add(sq,sq2, sq3,circ)
        self.wait(1)
        self.play(*[FadeOut(x) for x in self.mobjects if x!= circ])
        self.wait()
        print("######")
        print( self.mobjects)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Text"
    os.system(command_A + command_B)