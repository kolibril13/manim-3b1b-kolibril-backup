from manimlib.imports import *

class Text(Scene):
    def construct(self):
        t= TextMobject("Viel Freude beim \\\\ Ausprobieren!")
        t.scale(3)
        t.set_color_by_gradient(GREEN, BLUE)
        self.play(Write(t), run_time=5)
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Text"
    os.system(command_A + command_B)