from manimlib.imports import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from skimage import io

class tomo2curve(Scene):
    def construct(self):
        t=TexMobject(r"\phi(x,y) = 2\pi F \mathcal{F}^{-1} \left( \frac{\mathcal{F}(I/I_0-1)}{|k^0_\bot|^2+\alpha}\right)")
        self.play(ShowIncreasingSubsets(t, lag_ratio=0.5))

        self.wait(2)
if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -p   -c '#2B2B2B' --video_dir ~/Downloads/  "
    command_B = module_name +" " +"tomo2curve"
    os.system(command_A + command_B)