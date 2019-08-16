from manimlib.imports import *

class Shapes(Scene):
    def get_piano_sounds():
        piano_folder = "/home/jan-hendrik/python/projects/manim-master/projects_hendrik/small_piano/"
        all_files = []
        for (piano_folder, dirnames, filenames) in os.walk(piano_folder):
            for f in filenames:
                all_files.append(os.path.join(f))
        sounds = {str(element[4:-4]): piano_folder + str(element) for element in all_files}
        return sounds

    CONFIG = {
        "low_c": "sounds/marimba_c_major_low.wav",
        "high_c": "sounds/marimba_c_major.wav",
        "min_time_between_sounds" : 0.0,
        "global_time_offset": 0.1,
        "RISING1_colors": [WHITE,RED,BLUE,GREEN,WHITE]
    }
    CONFIG.update(get_piano_sounds())

    def construct(self):
        print("Start")
        dot = Dot()
        clack_data= []
        self.wait(0.1)
        bpm=2
        for i in range(0,5):
            self.piano_sound(clack_data)
            self.wait(3/16*bpm)
            self.piano_sound(clack_data)
            self.wait(3/16*bpm)
            self.piano_sound(clack_data)
            self.wait(2/16*bpm)
            self.piano_sound(clack_data)
            self.wait(3 / 16 * bpm)
            self.piano_sound(clack_data)
            self.wait(3 / 16 * bpm)
            self.piano_sound(clack_data)
            self.wait(2 / 16 * bpm)

            if i >0:
                self.add_sound(self.E2)
                dot.set_color(self.RISING1_colors[i])
                self.piano_sound(clack_data)
                self.add(dot)
                circle= Circle(radius=i)
                circle.set_color(self.RISING1_colors[i])
                self.add(circle)
                if i>1:
                    self.add_sound(self.G2)
                    if i == 3:
                        self.add_sound(self.Ais2)
                        print("DA")
                if i == 4:
                    self.add_sound(self.C3)
                    self.add_sound(self.C1)
                    self.para_func = lambda t: np.array((np.cos(1*t)-np.cos(80*t)**3, np.sin(1*t)-np.sin(80*t)**3, 0))
                    func = ParametricFunction(self.para_func, t_max=TAU, num_anchor_points=1000)
                    func2=func.copy().scale(3)
                    self.add(func)
                    self.play(Transform(func, func2),rate_func=rush_into)
                    self.play(Transform(func, circle))
                    ALL_objects= VGroup(func,circle)
                    self.play(Transform(ALL_objects,dot))
                    self.wait(0.5)


        print("yes")

        self.add_clack_sounds(clack_data)
    def piano_sound(self, clack_data):
        clack_data.append((self.get_time()))
        return clack_data

    def add_clack_sounds(self, clack_data):
        clack_file = self.C2
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
            self.add_sound(clack_file, time_offset=(time - total_time), gain=-10)
        return self




if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p  --leave_progress_bars " + module_name + " Shapes "
    os.system(command)
