from manimlib.imports import *
class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "num_graph_anchor_points": 100,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)", x_val=-10, direction=UP / 2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2), runtime=20)
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))
        self.wait()
    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p  --leave_progress_bars " + module_name + " PlotFunctions "
    os.system(command)

