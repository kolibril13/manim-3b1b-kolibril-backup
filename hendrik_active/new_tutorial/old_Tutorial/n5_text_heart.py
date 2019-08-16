from manimlib.imports import *

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        Transform.CONFIG.update({
            "replace_mobject_with_target_in_scene": True
        })
        t = []  # implicit instantiation
        t.append(1)
        t.append(1)
        t.append(1)
        t.append(1)
        t.append(1)
        t.append(1)

        t[1]= TexMobject(r"\heartsuit")
        t[1].set_color(GREEN)
        t[1].to_edge(UP)
        t[2] = TexMobject(r"\heartsuit")
        t[2].set_color(RED)
        t[2].scale(3)
        t[3] = TexMobject(r"\heartsuit")
        t[3].set_color(RED)
        self.add(t[1])

        for i in range(1,3):
            self.play(Transform(t[i], t[i+1]))
            t[i].set_color(RED)
            t[i].scale(3)
            t[i+1] = TexMobject(r"\heartsuit")
            t[i+1].set_color(RED)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -pl   --leave_progress_bars -a " + module_name
    os.system(command)
