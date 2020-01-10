from manimlib.imports import *

class Text(GraphScene):
    CONFIG = {
        "y_min": 0,
        "y_max": 10    }
    def construct(self):


        self.setup_axes(animate=True)
        dot=Dot()
        dot.move_to(self.coords_to_point(0, 0))
        self.my_func = lambda x: np.sin(x)
        func_graph=self.get_graph(self.my_func)
        self.my_func2 = lambda x: 5*np.sin(x)
        func_graph2=self.get_graph(self.my_func2)
        self.play(Write(func_graph),run_time=5)
        self.add(dot)
        self.wait(0.5)
        self.play(Transform(func_graph,func_graph2),run_time=10)
        self.wait(0.5)


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -l  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"Text"
    os.system(command_A + command_B)