from manimlib.imports import *
import pandas as pd
class AddingText(Scene):
    CONFIG = {
        "alignment": "\\centering",
    }
    #Adding text on the screen
    def construct(self):
        t_2=pd.DataFrame([[1,2,3],[5,6,7]])
        t_2l= t_2.to_latex()
        text= r"""
\begin{table}[]
\centering
\begin{tabular}{ll}
a & b \\
1 & 33
\end{tabular}
\caption{}
\label{tab:my-table}
\end{table}
        """
        t_2_tex = TextMobject(text)
        Transform.CONFIG.update({
            "replace_mobject_with_target_in_scene": True
        })
        t_1=TexMobject(r"\frac{\partial \rho}{\partial t}+ \frac{\partial(\rho u_{i})}{\partial x_{i}} = 0")

        self.add(t_1)
        print(t_1)
        t_2_tex.next_to(t_1, UP)
        self.add(t_2_tex)
        self.wait(1)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "python3.7 -m manim  -p -s   --leave_progress_bars -a " + module_name
    os.system(command)
