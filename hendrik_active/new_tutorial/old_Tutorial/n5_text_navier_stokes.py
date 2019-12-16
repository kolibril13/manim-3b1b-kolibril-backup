from manimlib.imports import *

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        Transform.CONFIG.update({
            "replace_mobject_with_target_in_scene": True
        })
        # my_dict.update({'corse': 'my new definition'})
        t_1= TextMobject("Hello World")
        t_2_move = TextMobject("Let's get interactive")
        t_2_move.next_to(t_1,DOWN)
        t_3=TextMobject("Topic 1: what is a sinus")
        t_3.next_to(t_2_move,DOWN)
        t_4=TexMobject(r"\frac{\partial \rho}{\partial t}+ \frac{\partial(\rho u_{i})}{\partial x_{i}} = 0")
        self.add(t_1)
        self.play(Transform(t_1, t_2_move))
        self.play(Transform(t_2_move, t_3))
        self.play(Transform(t_3, t_4))
        t_5 = TexMobject(r"\Rightarrow \Psi(x, t) = \sum_j C_j \cdot e^{-i( k_j \cdot x -  \frac{k_j}{c(k_j)} \cdot t )}")
        self.add(t_5.shift(DOWN))
        self.wait(2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    folder = "  -o  /home/jan-hendrik/python/projects/tricks_for_python/jupyter/videoC "
    command = "python3.7 -m manim  -p  -s -a " + folder + module_name
    os.system(command)
