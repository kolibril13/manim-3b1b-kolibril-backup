from manimlib.imports import *


class EasyScence(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        dot2= Dot(RIGHT_SIDE+LEFT)
        self.play(Transform(dot, dot2))
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    folder = "  -o  /home/jan-hendrik/python/projects/tricks_for_python/jupyter/videoC "
    command = "python3.7 -m manim  -pl " + folder + module_name + " EasyScence"
    os.system(command)
