from manimlib.imports import *

class svg_datei(Scene):
    def construct(self):
        dot1 =SVGMobject("/home/jan-hendrik/Downloads/Snowflake.svg")
        dot2 =SVGMobject("/home/jan-hendrik/Downloads/flower.svg")
        self.play(Transform(dot1,dot2), path_arc=1,run_time=3)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim  -l -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"svg_datei"
    os.system(command_A + command_B)