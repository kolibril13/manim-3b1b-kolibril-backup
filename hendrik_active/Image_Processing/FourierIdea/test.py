from manimlib.imports import *

class laalaa(Scene):
    def construct(self):
        obj= SVGMobject(file_name="arrow.svg")
        dot = Dot()
        self.add(dot)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"laalaa"
    os.system(command_A + command_B)