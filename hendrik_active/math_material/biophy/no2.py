from manimlib.imports import *

class No2(Scene):
    def construct(self):
        dot = Dot(point=LEFT_SIDE+RIGHT,radius= 0.3, color= RED)
        path = VMobject()
        #dot = Dot()
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([dot.get_center()])
            path.become(previus_path)
        path.add_updater(update_path)
        self.add(path,dot)
        self.play(dot.shift,RIGHT*10, run_time=3 ,rate_func= linear)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -m -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No2"
    os.system(command_A + command_B)

        #
        # self.play(
        # Rotating(
        #     dot,
        #     radians=PI,
        #     about_point=RIGHT,
        #     run_time=2
        # )
        # ,rate_func= linear