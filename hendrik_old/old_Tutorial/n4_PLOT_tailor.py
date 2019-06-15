from manimlib.imports import *
class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10.3,
        "num_graph_anchor_points": 100,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "taylor_color": WHITE,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
        "counter": 0

    }

    def construct(self):
        self.setup_axes()
        func_graph=self.get_graph(self.func)
        change=self.get_graph(self.func)

        self.play(ShowCreation(func_graph),ShowCreation(change))


        for i in range(0,4):
            self.counter= i
            taylor_graph = self.get_graph(self.taylor, self.taylor_color )
            self.play(Transform(change,taylor_graph))
            print(self.counter)

    def func(self,x):
        return np.cos(x)

    def taylor(self,x):
        print("SSSSS")
        print("self.counter")
        if self.counter == 0:
            return 1
        if self.counter == 1:
            return 1-1/2 *x**2
        if self.counter == 2:
            return 1-1/2 *x**2 +1/(1*2*3*4)*x**4
        if self.counter == 3:
            return 1-1/2 *x**2 +1/(1*2*3*4)*x**4-1/(1*2*3*4*5*6)*x**6
        if self.counter == 3:
            return 1-1/2 *x**2 +1/(1*2*3*4)*x**4-1/(1*2*3*4*5*6)*x**6+1/(1*2*3*4*5*6*7*8)*x**8


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p  --leave_progress_bars -a " + module_name
    os.system(command)

