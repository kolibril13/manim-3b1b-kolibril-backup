from manimlib.imports import *

class Color_text(Scene):
    def construct(self):
        tex = TextMobject("Hello ", "World")
        tex.set_color_by_tex("World" ,color=BLUE)
        self.add(tex)
        tex2= tex.copy()
        tex2.set_color_by_tex("World" ,color=RED)

        self.play(Transform(tex,tex2))

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p   " + module_name + " Color_text"
    os.system(command)
