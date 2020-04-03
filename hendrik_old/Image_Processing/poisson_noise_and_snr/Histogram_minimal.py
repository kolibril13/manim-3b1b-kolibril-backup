from manimlib.imports import *

import numpy as np
from hendrik_active.resusable_hendrik.histograms import *
##Histogram like this:
## 0   2    2     1 ....
#0   1    2    3    4 ...... 255...  256

class MinimalHist(Scene):
    def construct(self):
        Circle()
        values= [1,1,1,1,0,0,0,0,5,5,8,9,23,3,3,3,23,235,234,2,1,212,12,3,255]
        max=256
        val = np.histogram(values, bins=[i for i in np.arange(0, max+1)])
        hist= Image_Histogram(val[1], val[0], x_scale= 4/max)
        self.add(hist)
        self.wait(0.2)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command = "manim -c '#2B2B2B' -p -s  " + module_name + " MinimalHist"
    os.system(command)
