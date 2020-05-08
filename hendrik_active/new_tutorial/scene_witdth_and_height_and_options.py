from manimlib.imports import *

class SceneInfo(Scene):
    def construct(self):
        dot = Dot(radius = 1)
        dot.move_to(RIGHT*500)
        self.add(dot)
        self.wait(2)
        print(DEFAULT_PIXEL_HEIGHT)
        print(DEFAULT_PIXEL_WIDTH)
        print(FRAME_HEIGHT)
        print(FRAME_WIDTH)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"SceneInfo"
    os.system(command_A + command_B)