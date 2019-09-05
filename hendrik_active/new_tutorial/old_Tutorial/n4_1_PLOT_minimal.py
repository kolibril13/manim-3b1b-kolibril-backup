from manimlib.imports import *

class Generation(GraphScene):
    def construct(self):
        self.setup_axes()
        self.my_func = lambda x: np.sin(x)
        func_graph=self.get_graph(self.my_func)
        func_graph.set_style(fill_opacity=0)
        self.play(FadeIn(func_graph))
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name + " " + "Generation"
    os.system(command_A + command_B)

