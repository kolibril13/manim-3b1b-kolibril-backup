from manimlib.imports import *

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        Transform.CONFIG.update({
            "replace_mobject_with_target_in_scene": True
        })
        t_1= TextMobject("Hii")
        t_1.set_color(GREEN)
        t_1.to_edge(UP)
        t_1.scale(4)
        t_1.bg=BackgroundRectangle(t_1,fill_opacity=1, color= BLUE)
        t_group = VGroup(t_1.bg,t_1)
        t_group.rotate(TAU/8)
        t_2= TexMobject(r"\sin(x)^2+3+4+5")
        t_2.next_to(t_1,DOWN)
        self.add(t_group)
        self.add(t_2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p -s  --leave_progress_bars -a " + module_name
    os.system(command)
