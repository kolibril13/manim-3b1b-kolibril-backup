from manimlib.imports import *
class S4_sauerstoff(GraphScene):
    CONFIG = {
        "y_axis_label": r"Sauerstoffgehalt[$\%$]",
        "x_axis_label": "Zeit [s]",
        "y_min": 0,
        "y_max": 101,
        "y_tick_frequency": 10,
        "y_labeled_nums": np.arange(0,101,10),
    }

    def construct(self):
        data= [20,19,2,23,4]
        squ = Rectangle(height=np.sum(TOP) * 2, width=np.sum(LEFT_SIDE) * 2,
                        fill_color=DRAC_GREY, fill_opacity=0.8)
        #make the intro of the plot
        self.play(FadeIn(squ))
        self.setup_axes(animate=True)
        dot_ALL = [Dot() for k in range(0,len(data))]
        for time , dot in enumerate(dot_ALL):
            dot.move_to(self.coords_to_point(time, data[time]))
            self.add(dot)
            self.wait(1)
            print(time)
        self.wait()

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    abspath = os.path.abspath(__file__)
    raw_file_name = abspath.split(".")[0]
    print("hier:" , raw_file_name)
    command = "python3.7 -m manim  -a  -p -t  -l -o " + raw_file_name + " " + module_name
    os.system(command)
