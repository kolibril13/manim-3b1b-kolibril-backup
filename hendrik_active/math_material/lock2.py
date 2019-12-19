from manimlib.imports import *

class Lock(Scene):
    def construct(self):
        an= Annulus().shift(UP)
        re = Rectangle(side_length=2, fill_color= BLACK, stroke_color=BLACK, fill_opacity=1)
        Head=VGroup(an, re)
        el=Head.get_center()+1.5*RIGHT
        rec=Rectangle(height=2, width= 1 , fill_color= WHITE, stroke_width=0, stroke_opacity=0, fill_opacity=1)
        rec.next_to(el, DOWN, buff=-0.5*SMALL_BUFF)
        Head=VGroup(Head, rec)
        self.add(Head)
        BIG_REC= Rectangle(height=2.5, width= 4,fill_color= WHITE,fill_opacity=1)
        BIG_REC.next_to(rec.get_corner(LEFT), RIGHT , buff=0).shift(DOWN*1.5)
        All= VGroup(Head, BIG_REC)
        self.add(BIG_REC)
        self.wait(2)
        self.play(Rotate(Head, 180 * DEGREES, axis=UP,about_point=el),run_time=0.2)
        self.play(Head.move_to, BIG_REC.get_corner(UP)+0.2*DOWN, run_time=0.2)
        self.play(FadeToColor(All, YELLOW), run_time=0.2)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Lock"
    os.system(command_A + command_B)