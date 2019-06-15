from manimlib.imports import *

REGISTERED_CLASSES = []

def render(cls):
    REGISTERED_CLASSES.append(cls.__name__)
    return cls

@render
class My_Scene(Scene):
    def construct(self):
        dot= Dot()
        self.play(Write(dot))

@render
class My_Scene2(Scene):
    def construct(self):
        dot= Dot()
        self.add(dot)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    os.system("manim -pl " + module_name + " " + " ".join(REGISTERED_CLASSES))
    print()