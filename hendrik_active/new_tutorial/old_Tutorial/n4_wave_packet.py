from manimlib.imports import *
class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "num_graph_anchor_points": 100,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2)
    }

    def construct(self):
        self.setup_axes(animate=False)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        # func_graph2=self.get_graph(self.func_to_graph2)
        self.play(ShowCreation(func_graph))
        # self.play(Transform(func_graph,func_graph2))
        self.wait(2)

    # def gaussian(x, mu, sig):
    #     return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    global dispersion_relation
    def dispersion_relation(karray, x):
        # karray = np.power(karray,1.0)
        return karray

    def func_to_graph(self,x):
        wert = 0
        t = 0
        karray = np.arange(1, 5)
        for k in karray:
            wert += np.exp(1j * (k * x - dispersion_relation(k, x) * t)).real / len(karray)
        return wert





if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim -pl  --leave_progress_bars " + module_name + " PlotFunctions "
    os.system(command)
