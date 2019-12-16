from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        logo =SVGMobject("/home/jan-hendrik/Downloads/g42.svg")
        print(logo.submobjects)
        #logo.submobjects[0].set_style(fill_color=BLUE)
        # logo.submobjects[1].set_style(fill_color=YELLOW_D)
        # text1= TextMobject("Saturday")
        # text2= TextMobject("Shortcuts")
        # text1.to_edge(LEFT)
        # text2.to_edge(LEFT)
        # text2.next_to(text1,DOWN,buff=0)
        # text= VGroup(text1,text2).scale(3)
        # text.next_to(logo,RIGHT)
        # all= VGroup(text,logo).move_to(ORIGIN)
        # squ=Square(fill_color="#2B2B2B",fill_opacity=1).scale(10)
        # self.add(squ)

        # self.play(Write(text, rate_func= smooth),
        #self.play(        DrawBorderThenFill(logo, rate_func= smooth), run_time=5)
        self.add(logo)
        self.wait(0.1)
        # all2= all.copy()
        # all2.scale(0.3)
        # all2.to_edge(DL)
        # self.play(Transform(all, all2), FadeOut(squ))
        # self.play(FadeIn(all2.add_background_rectangle(color="#2B2B2B", buff=0.3)))
        # self.wait(1)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Intro"
    os.system(command_A + command_B)