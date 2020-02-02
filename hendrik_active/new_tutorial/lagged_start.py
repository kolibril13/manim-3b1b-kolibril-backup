from manimlib.imports import *

class lag(Scene):
    def construct(self):
        dot = Dot()
        t1=TextMobject("Hello Dot")
        self.play(FadeIn(dot, run_time=4),(Write(t1 , run_time=2)))
        self.wait(1)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"lag"
    os.system(command_A + command_B)