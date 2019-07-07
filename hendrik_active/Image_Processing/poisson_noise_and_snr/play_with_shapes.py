from manimlib.imports import *

class lala(Scene):
    def construct(self):
        seq= Square(color= BLUE)
        seq.set_style(stroke_width=10)
        seq.move_to(2*UP+3*LEFT)
        dot = Dot()

        origin_point= Dot()
        origin_point.set_opacity(2)
        dot.move_to(seq)
        vert_line = Line(origin_point, seq.get_center(), color=RED, stroke_width=10)

        self.add(seq,dot)
        self.add(vert_line)
        # self.bring_to_back(vert_line)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -p  -s   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lala"
    os.system(command_A + command_B)