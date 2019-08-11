from manimlib.imports import *

class elii(Scene):
    def construct(self):
        dot = VGroup(
            Ellipse(height=0.7),
            Ellipse(height=0.7).rotate(PI / 3),
            Ellipse(height=0.7).rotate(2 * PI / 3)
        )
        self.add(dot)
        dot2= VGroup(
            Ellipse(height=0.2),
            Ellipse(height=0.2).rotate(PI / 3),
            Ellipse(height=0.2).rotate(2 * PI / 3)
        )
        dot2.shift(DOWN*3)
        self.wait(2)
        self.add(dot2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"elii"
    os.system(command_A + command_B)