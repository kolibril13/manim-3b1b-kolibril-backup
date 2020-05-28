from manimlib.imports import *
#class RegisterClass:
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



from pathlib import Path
if __name__ == "__main__":
    manim_main = Path.home() / "python/projects/manim/manim.py"
    command_A =   f"{manim_main}  -s -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = f"{Path(__file__).resolve()} " + " ".join(REGISTERED_CLASSES)
    print(command_A + command_B)
    os.system(command_A + command_B)