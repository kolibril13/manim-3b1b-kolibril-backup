from manimlib.imports import *

class LEFTRIGHT(Scene):
    def construct(self):
        list_from_csv = []
        dot = Circle()
        self.add(dot)
        def particle_updater(d,dt):
            d.shift(RIGHT*0.1)
            list_from_csv.append(d.get_center())
        np.save("my_Array", list_from_csv)
        dot.add_updater(particle_updater)
        self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p  -l -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"LEFTRIGHT"
    os.system(command_A + command_B)