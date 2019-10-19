from manimlib.imports import *

class definition(Scene):
    def construct(self):
        definition_text_1=TextMobject("A sequence, $(x_n)$ is said to be a" ,"Cauchy", "Sequence if ","for all", "$\epsilon > 0$")
        definition_text_2=TextMobject("$\exists$ \ K($\epsilon$) such that ","for all m,n $\geq$ $ K(\epsilon)$,","$|x_m-x_n|<\epsilon$")
        definition_text_1.shift(UP)
        definition_text_1.set_color_by_tex_to_color_map({"Cauchy": YELLOW,"$\epsilon > 0$": BLUE,"for all":RED})
        definition_text_2.set_color_by_tex_to_color_map({"$|x_m-x_n|<\epsilon$": YELLOW," \ K($\epsilon$) ":BLUE,"for all m,n $\geq$ $ K(\epsilon)$,":BLUE})

        self.play(Write(definition_text_1))
        self.play(Write(definition_text_2))
        ##self.play(Applymethod())
        self.wait(3)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -m -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "definition"
    os.system(command_A + command_B)

