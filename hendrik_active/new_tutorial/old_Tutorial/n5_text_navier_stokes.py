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

        self.wait(2)




        # my_first_text=TextMobject("Writing with manim is fun")
        # second_line=TextMobject("and easy to do!")
        # second_line.next_to(my_first_text,DOWN)
        # third_line=TextMobject(r"for me and you!")
        # third_line.next_to(my_first_text,DOWN)
        # fourth_line=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        # fourth_line.next_to(my_first_text,DOWN)
        #
        # self.add(my_first_text, second_line)
        # self.wait(2)
        # self.play(Transform(second_line,third_line))
        # self.wait(2)
        # self.play(Transform(second_line,fourth_line))
        # self.wait(2)
        # second_line.shift(3*DOWN)
        # self.play(ApplyMethod(my_first_text.shift,3*UP))
        ###Try uncommenting the following###
        #self.play(ApplyMethod(second_line.move_to, LEFT_SIDE-2*LEFT))
        #self.play(ApplyMethod(my_first_text.next_to,second_line))
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    folder = "  -o  /home/jan-hendrik/python/projects/tricks_for_python/jupyter/videoC "
    command = "python3.7 -m manim  -p -a " + folder + module_name
    os.system(command)
