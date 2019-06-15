from manimlib.imports import *


class Tattoo(Scene):
    def gaussian(self,x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    def construct(self):
        func = []
        func.append(ParametricFunction(lambda t:(t,    np.sin(t), 0) , t_min=0, t_max=TAU, color= BLACK))
        for f in func:
            self.add(f.move_to(LEFT))
        self.wait()


if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s -c '#2B2B2B' -o ~/Downloads/ Tattoo"
    com= "manim " + module_name + " Tattoo"
    os.system(com)
