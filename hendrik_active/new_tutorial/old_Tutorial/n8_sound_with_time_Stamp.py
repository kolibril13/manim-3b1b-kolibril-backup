from manimlib.imports import *

class Shapes(Scene):
    CONFIG = {
        "low_c": "sounds/marimba_c_major_low.wav",
        "high_c": "sounds/marimba_c_major.wav",
        "min_time_between_sounds" : 0.0,
        "global_time_offset": 0.1
    }
    def construct(self):
        print("Start")
        dot = Dot()

        circle = Circle(radius= 1)
        circle2 = Circle(radius= 1.1)

        clack_data= []

        self.wait(2)
        clack_data.append((self.get_time()))
        self.add(dot)
        self.wait(4)
        clack_data.append((self.get_time()))
        self.add(circle2)
        self.play(GrowFromCenter(circle))
        # clack_data=[x**(1/2) for x in np.arange(0,100,0.1)]
        self.wait(2)
        self.add_clack_sounds(clack_data)


    def add_clack_sounds(self, clack_data):
        clack_file = self.low_c
        total_time = self.get_time()
        print(total_time)
        times = [
            time
            for time in clack_data
            if time < total_time
        ]
        print("Times are" ,times)
        last_time = 0
        for time in times:
            d_time = time - last_time
            if d_time < self.min_time_between_sounds:
                continue
            last_time = time
            self.add_sound(
                clack_file,
                time_offset=(time - total_time)-self.global_time_offset,
                gain=-20,
            )
        return self




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -pl  -o earth_sofi  --leave_progress_bars " + module_name + " Shapes "
    os.system(command)








