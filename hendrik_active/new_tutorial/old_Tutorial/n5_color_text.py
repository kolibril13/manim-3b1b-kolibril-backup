from manimlib.imports import *

class Color_text(Scene):
    def construct(self):
        tex = TextMobject("Hello", "World")
        tex.set_color_by_tex("He" ,color=DARK_BLUE)
        tex.set_color_by_tex("Wo" ,color=GREEN)
        self.add(tex)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p  -s " + module_name + " Color_text"
    os.system(command)
