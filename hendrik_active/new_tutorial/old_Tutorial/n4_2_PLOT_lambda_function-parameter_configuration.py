from manimlib.imports import *

class Generation(GraphScene):
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
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Generation"
    os.system(command_A + command_B)


