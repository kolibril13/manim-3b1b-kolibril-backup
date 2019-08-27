from manimlib.imports import *

class ll(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-60 * DEGREES)  # 2.5D
        dot = Dot()
        k_text = TextMobject(r"Hello world", fill_color=ORANGE).shift(DOWN ).scale(2)

        self.add(k_text)

        self.add_fixed_in_frame_mobjects(FadeIn(dot))
        dot.set_style(fill_opacity=0,stroke_opacity=0).scale(3)
        self.wait(2)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"ll"
    os.system(command_A + command_B)