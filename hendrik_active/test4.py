from manimlib.imports import *

# this part can go to some imports: #
#####   start   ########
class ClassesToRender:
    def __init__(self):
        self.registered_class = []

    def get_sting(self):
        return " ".join(self.registered_class)

    def set(self, class_name):
        self.registered_class.append(class_name)

classes_to_render = ClassesToRender()

def render(cls):
    classes_to_render.set(cls.__name__)
    return cls

#####  end    ##############

@render
class My_Scene(Scene):
    def construct(self):
        dot = Dot()
        self.play(Write(dot))

@render
class My_Scene2(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)

from pathlib import Path

if __name__ == "__main__":
    manim_main = Path.home() / "python/projects/manim/manim.py"
    command_A = f"{manim_main}  -s -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = " " f"{Path(__file__).resolve()} " + " " + classes_to_render.get_sting()
    print(command_A + command_B)
    os.system(command_A + command_B)
