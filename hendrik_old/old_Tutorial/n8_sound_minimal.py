from manimlib.imports import *

class Sounds(Scene):
    CONFIG = {
        "low_c": "sounds/marimba_c_major_low.wav",
        "high_c": "sounds/marimba_c_major.wav"
    }
    def construct(self):
        print("Start")
        dot = Dot()
        circle = Circle(radius= 1)
        self.wait(1)
        self.add(dot)
        self.add_sound(
            self.low_c,
            gain=-10,
            time_offset=-0.1
        )
        self.play(GrowFromCenter(circle))
        self.add_sound(
            self.high_c,
            gain=-10,
            time_offset = -0.1
        )
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p -c '#2B2B2B' "  + module_name+  " Sounds"
    os.system(command)
