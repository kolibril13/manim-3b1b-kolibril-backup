from manimlib.imports import *

class PLOT(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$x$",
        "y_min": -10,
        "y_max": 10,

    }
    def construct(self):
        self.setup_axes()
        func_graph1=self.get_graph(lambda x: x**3-6*x**2+12*x-8)
        func_graph1.set_style(fill_opacity=0)
        self.add(func_graph1)
        self.play((self.get_graph(lambda  x: -8+12*x-6*x**2)), run_time=3)
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -m -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "PLOT"
    os.system(command_A + command_B)

