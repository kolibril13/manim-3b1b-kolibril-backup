from manimlib.imports import *
class Ex(Scene):
    def construct(self):
        dot= Dot()
        self.add(dot)
        dot.set_style(  )
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -ls   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Ex"
    os.system(command_A + command_B)
