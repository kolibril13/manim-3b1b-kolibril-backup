from manimlib.imports import *

class EasyScence(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -o ~/temp/ -pl -a " + module_name
    os.system(command)

