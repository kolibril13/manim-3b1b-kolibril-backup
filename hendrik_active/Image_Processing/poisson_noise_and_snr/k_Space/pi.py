from manimlib.imports import *

class piiii(PiCreatureScene):
    def construct(self):
        randy = self.pi_creature
        dot = Dot()
        self.add(dot)
        self.wait(2)
        self.add(randy)
    
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"piiii"
    os.system(command_A + command_B)