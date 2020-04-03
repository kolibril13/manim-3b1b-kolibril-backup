from manimlib.imports import *
np.random.seed(42)
class No15(Scene):
    def construct(self):


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No15"
    os.system(command_A + command_B)
