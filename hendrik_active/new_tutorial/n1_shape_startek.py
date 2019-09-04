from manimlib.imports import *

class shape_k(Scene):
    def construct(self):
        dot=SVGMobject("arrow.svg",fill_color=BLUE)
        
        self.play(Write(dot))
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim   -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"shape_k"
    os.system(command_A + command_B)