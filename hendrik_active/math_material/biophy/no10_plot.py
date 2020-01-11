from manimlib.imports import *

from scipy.constants import pi, c , g
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
plt.rcParams['figure.dpi'] = 300
class No10(Scene):
    def construct(self):
        sq= Rectangle(width=0.45*FRAME_WIDTH*2,height= 0.15*FRAME_HEIGHT*2)
        blue_dot = Dot(radius= 0.3, color= BLUE)
        self.add(sq)

        x= np.linspace(0,1,10000)
        kP_on = 11.6
        kP_off = 1.4

        def dnP(concentration):
            return kP_on*concentration- kP_off

        sns.set_context("talk")
        plt.plot(x, dnP(x) , label= r"Plus end  $\frac{dn^+}{dt}$" )
        plt.scatter(0, dnP(0) , marker="o" , s=200 )

        plt.ylabel("Growth Rate [1/s]")
        plt.xlabel("Concentration in [$\mu$mol/l]")
        plt.axhline(y=0, color="black", linestyle="--")
        plt.legend()
        plt.xlim(-0.1,1)
        plt.ylim(-2,4)
        plt.savefig("temp.png",bbox_inches="tight")
        self.add(ImageMobject("temp.png").scale(1.5).to_edge(DR))
        self.wait()
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p -s  -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"No10"
    os.system(command_A + command_B)
