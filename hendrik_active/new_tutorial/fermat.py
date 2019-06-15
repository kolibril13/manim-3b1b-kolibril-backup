from manimlib.imports import *

class Fermat(Scene):
    CONFIG = {
        "color": BLACK,
        "stroke_width": 0,
        "stroke_opacity": 0,
        "fill_opacity": 0.75,
        "buff": 0
    }

    def rot_Texobject(self,text,line):
        word = TexMobject(text)
        word.next_to(ORIGIN, UP, SMALL_BUFF)
        word.rotate(line.get_angle(), about_point=ORIGIN)
        word.shift(line.get_center())
        return word
    def make_angle(self, start, stop, point, text, color):
        print("yes")
        arc_alpha = Arc(
            start_angle=start,
            angle=stop,
            radius=1.3,
            arc_center=point,
            stroke_width=2,
            stroke_color=YELLOW,
            stroke_opacity=0.5,
        )

        text_alpha = TexMobject(text)
        text_alpha.next_to(arc_alpha.get_center(), DOWN, SMALL_BUFF*0.5)
        dot= Dot(arc_alpha.get_center())
        alpha = VGroup(arc_alpha,text_alpha)
        alpha.set_style(stroke_color=color, fill_color=color)
        return alpha
    def construct(self):
        # box
        ground = Polygon(DOWN+2*LEFT,DOWN*2+2*LEFT, DOWN*2+2*RIGHT,DOWN+2*RIGHT,fill_color=BLUE, fill_opacity=1)
        ground.set_style(stroke_color=GREY_BROWN, fill_color=GREY_BROWN)
        ##
        r1=4
        r2=5
        angle_num=TAU/8
        point_1 = [-r1*np.sin(angle_num),r1*np.cos(angle_num),0]+DOWN
        point_R = [0,0,0]+DOWN
        point_2 = [r2*np.sin(angle_num),r2*np.cos(angle_num),0]+DOWN
        A = Dot(point_1,color= BLUE)
        A_text = TexMobject("P_1(x_1, y_1)" , color= BLUE).next_to(point_1, DOWN)
        R = Dot(point_R, color = BLUE)
        R_text = TexMobject("R(x,0)" , color= BLUE).next_to(point_R, DOWN)

        B = Dot(point_2)
        B_text = TexMobject("P_2(x_2, y_2)" , color= BLUE).next_to(point_2, DOWN)



        line1 = Line(point_1, point_R, stroke_color= GREEN)
        line2 = Line(point_R,point_2, stroke_color= RED)
        line1_descr= VGroup(A, A_text , self.rot_Texobject("s_1",line1))
        line2_descr= VGroup(B, B_text , self.rot_Texobject("s_2",line2))

        dline = DashedLine(point_R, point_R+3*UP , stroke_color= YELLOW_D)
        brace1 = Brace(line1, UP)
        eq_text = brace1.get_tex("x-x_1")
        brace2 = Brace(line2, UP)
        eq_text2 = brace2.get_tex("x_2-x")

        angle_a= self.make_angle(TAU/4, angle_num, point_R, "\\alpha", GREEN)
        angle_b= self.make_angle(TAU/4, -angle_num, point_R, "\\beta", RED)

        self.add(ground)
        self.play(Write(line1))
        self.play(FadeIn(line1_descr))
        self.play(FadeIn(R_text, R))
        self.play(Write(line2))
        self.play(FadeIn(line2_descr))

        self.play(Write(VGroup(dline, angle_a, angle_b)))

        self.play(FadeIn(brace1), FadeIn(eq_text))
        self.play(FadeIn(brace2), FadeIn(eq_text2))

        ####
        eq1_text = ["s_{ges}", "=", "s_1", "+", " s_2"]
        eq2_text = ["=\sqrt{(x-x_1)^2+y_1^2}", "+\sqrt{(x_2-x)^2+y_2^2}"]
        eq1 = TexMobject(*eq1_text)
        eq1.set_color_by_tex("s_1", GREEN)
        eq1.set_color_by_tex("s_2", RED)

        eq2 = TexMobject(*eq2_text)
        eq2.align_to(eq1.submobjects[1], LEFT)
        eq2.shift(DOWN)
        eq2.set_color_by_tex("x-x_1", GREEN)
        eq2.set_color_by_tex("x_2-x", RED)
        gr=VGroup(eq1, eq2).scale(0.8)
        gr.next_to(ground,DOWN)
        self.play(Write(eq1))
        self.play(Write(eq2.submobjects[0]))
        self.play(Write(eq2.submobjects[1]))


num="10"
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p    -c '#2B2B2B' --video_dir ~/Downloads/ -n " + num + "," + str(int(num)+1) + " " + "-o 00" + num +" "
    command_B = module_name +" " +"Fermat"
    os.system(command_A + command_B)