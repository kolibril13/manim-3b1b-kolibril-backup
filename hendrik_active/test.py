from manimlib.imports import *
class No1(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait(2)

class LALA(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait(1)

if __name__ == "__main__":
    manim_main = Path.home() / "projects/manim/manim.py"
    command_A =   f"{manim_main}  -s -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = f"{Path(__file__).resolve()}   "
    os.system(command_A + command_B)