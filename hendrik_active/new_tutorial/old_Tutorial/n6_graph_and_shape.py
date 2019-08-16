from manimlib.imports import *

class graph_shape(GraphScene):
    #Adding text on the screen
    CONFIG = {
        "col_A": BLUE
    }
    def construct(self):
        self.setup_axes()
        self.my_func = lambda x: x**2
        func_graph=self.get_graph(self.my_func, self.col_A)
        label= TexMobject(r"\text{Die Funktion lautet: }", r"x^2")
        label.set_color_by_tex("x^2", GREEN)
        label_coord=  self.input_to_graph_point(2,func_graph)
        vert_line = self.get_vertical_line_to_graph(2, func_graph, color= RED)
        label.next_to(label_coord,RIGHT + UP)
        new_point=self.input_to_graph_point(0,func_graph)
        new_text= TexMobject(r"o")
        new_text.next_to(new_point)
        self.add(new_text)
        self.add(func_graph)
        self.add(vert_line)
        self.add(label)
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -pl --leave_progress_bars -s -a " + module_name
    os.system(command)
