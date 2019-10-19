from manimlib.imports import *

class MEIN(Dot,SVGMobject):
    def __init__(self):
        path="/home/jan-hendrik/Downloads/pylogo.svg"
        SVGMobject.__init__(self, path)

class svg_datei(Scene):
    def construct(self):
        dot = Dot()
        dot2= MEIN()
        self.add(dot,dot2)
        self.wait(2)

    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"svg_datei"
    os.system(command_A + command_B)