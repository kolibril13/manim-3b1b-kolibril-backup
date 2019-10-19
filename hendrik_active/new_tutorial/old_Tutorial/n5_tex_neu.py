from manimlib.imports import *
class AddingText(Scene):
    def construct(self):
        text= TexMobject(
            "\\sqrt{",
            "dx}"
        )
        text2 = TexMobject(
            r"\begin{array}{c} 0 \\ ",
            r"0\\ 1 \end{array}"
        )
        self.add(text2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    print(module_name)
    command = "python3.7 -m manim  -p -s   --leave_progress_bars -a " + module_name
    print(command)
    os.system(command)
