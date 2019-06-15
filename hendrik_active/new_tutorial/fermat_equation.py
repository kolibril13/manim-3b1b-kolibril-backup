from manimlib.imports import *

class UsingBracesConcise(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        eq1_text = ["s_{ges}","=", "s_1", "+"," s_2"]
        eq2_text = ["=", "\sqrt{(x-x_1)^2+y_1^2}","+", "\sqrt{(x_2-x)^2+y_2^2}" ]
        eq1= TexMobject(*eq1_text)
        eq1.set_color_by_tex("s_1", GREEN)
        eq1.set_color_by_tex("s_2", RED)

        eq2= TexMobject(*eq2_text)
        eq2.align_to(eq1.submobjects[1],LEFT)
        eq2.shift(DOWN)
        eq2.set_color_by_tex("x-x_1", GREEN)
        eq2.set_color_by_tex("x_2-x", RED)
        VGroup(eq1,eq2).scale(0.8)
        # self.play(Write(eq1),Write(eq2))
        print("ää")
        [print(str(e)) for e in eq1.submobjects]
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -s -m   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"UsingBracesConcise"
    os.system(command_A + command_B)