from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        logo =SVGMobject("/home/jan-hendrik/Downloads/bird-export.svg")
        print(logo.submobjects)
        logo.scale(3)
        logo.submobjects[0].set_style(fill_color=GREEN)

        self.play(        DrawBorderThenFill(logo.submobjects[0], rate_func= smooth), run_time=10)
        #self.wait(0.1)
        # all2= all.copy()
        # all2.scale(0.3)
        # all2.to_edge(DL)
        # self.play(Transform(all, all2), FadeOut(squ))
        # self.play(FadeIn(all2.add_background_rectangle(color="#2B2B2B", buff=0.3)))
        # self.wait(1)



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Intro"
    os.system(command_A + command_B)