from manimlib.imports import *

class FourierTradeoff(Scene):
    CONFIG = {
        "show_text" : True,
        "complex_to_real_func" : lambda z : z.real,
        "widths" : [6, 0.02, 1],
    }
    def construct(self):
        #Setup axes
        time_mean = 4
        time_axes = Axes(
            x_min = 0,
            x_max = 2*time_mean,
            x_axis_config = {"unit_size" : 1.5},
            y_min = -2,
            y_max = 2,
            y_axis_config = {"unit_size" : 0.5}
        )
        time_label = TextMobject("Time")
        time_label.scale(1.5)
        time_label.next_to(
            time_axes.x_axis.get_right(), UP+LEFT,
            buff = MED_SMALL_BUFF,
                                          )
        time_axes.add(time_label)
        time_axes.center().to_edge(UP)
        time_axes.x_axis.add_numbers(*list(range(1, 2*time_mean)))

        frequency_axes = Axes(
            x_min = 0,
            x_max = 8,
            x_axis_config = {"unit_size" : 1.5},
            y_min = -0.025,
            y_max = 0.075,
            y_axis_config = {
                "unit_size" : 30,
                "tick_frequency" : 0.025,
            },
            color = TEAL,
        )
        frequency_label = TextMobject("Frequency")
        frequency_label.scale(1.5)
        frequency_label.next_to(
            frequency_axes.x_axis.get_right(), UP+LEFT,
            buff = MED_SMALL_BUFF,
                                               )
        frequency_label.set_color(YELLOW)
        frequency_axes.add(frequency_label)
        frequency_axes.move_to(time_axes, LEFT)
        frequency_axes.to_edge(DOWN, buff = LARGE_BUFF)
        frequency_axes.x_axis.add_numbers()
        self.add(frequency_axes,time_axes)
        self.wait(1)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "FourierTradeoff"
    os.system(command_A + command_B)
