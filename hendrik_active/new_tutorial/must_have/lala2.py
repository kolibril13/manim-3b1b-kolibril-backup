from manimlib.imports import *

class DrawScene(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(),dot.get_center()+UP*0.01])
        def update_path(path):
            previus_path = path.copy()
            previus_path.add_points_as_corners([dot.get_center()])
            path.become(previus_path)

        path.add_updater(update_path)

        self.add(path,dot)
        self.play(
            Rotating(
                dot,
                radians=PI,
                about_point=RIGHT,
                run_time=2
            )
        )
        self.wait()
        self.play(
            dot.shift,UP
        )
        self.play(
            dot.shift,LEFT
        )
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -s -c WHITE --video_dir ~/Downloads/  "
    command_B = module_name +" " +"DrawScene"
    os.system(command_A + command_B)