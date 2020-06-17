from manimlib.imports import *

class No5(Scene):
    def construct(self):
        red_dot = Dot(radius= 0.6, color= RED)
        white_dot = Dot(point=RIGHT)

        self.add(red_dot)
       # self.add(wd)
        for i in range(0,20):
            wd= white_dot.copy()
            wd.rotate(np.random.uniform(-PI/2,PI/2) ,about_point= red_dot.get_center())
            self.play(wd.move_to, red_dot.get_center(),run_time=0.2)
            if i > 2:
                self.remove(self.mobjects[1])


if __name__ == "__main__":
    manim_main = Path.home() / "projects/manim/manim.py"
    command_A =   f"{manim_main}  -s -p -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = f"{Path(__file__).resolve()}   "
    os.system(command_A + command_B)