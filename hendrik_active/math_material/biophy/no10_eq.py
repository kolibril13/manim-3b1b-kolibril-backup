from manimlib.imports import *

class No10(Scene):
    def construct(self):
        eq1 = TexMobject(r"\frac{dn^+}{dt} = "," - k^+_{off}", " + c_A \cdot k^+_{on}")
        eq1.submobjects[2].set_style(fill_opacity=0)
        self.add(eq1.to_edge(DL))
        self.play(eq1.submobjects[2].set_opacity, 1)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No10"
    os.system(command_A + command_B)
