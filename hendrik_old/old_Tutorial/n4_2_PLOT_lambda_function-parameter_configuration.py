from manimlib.imports import *

class PlotFunctions(GraphScene):
    CONFIG = {
        "OFFSET": 1,
    }
    def construct(self):
        self.setup_axes()
        self.my_func = lambda x: np.exp(-np.exp(x))
        func_graph=self.get_graph(self.my_func)
        func_graph2=self.get_graph(self.my_func2)
        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(func_graph2))


    def shift(self,x, var):
        y= x+self.OFFSET
        return y

    def my_func2(self,x):
        var=2
        y=self.shift(x, var)
        return y



if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p  --leave_progress_bars -a " + module_name
    os.system(command)

